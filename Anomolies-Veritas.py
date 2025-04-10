import re
import unicodedata
import string
import pandas as pd
#from langdetect import detect
#import goslate
#gs = goslate.Goslate()
def language_selection(words,language_tag):
    lang_tag = str(language_tag)[: 2]
    if lang_tag == "en":
        return re_clean(words, language_tag='en_US')
    elif lang_tag in ["fr","es","it","de","zh","ja",'pt','pl','ar','sv','tr']:
        return Other_Lang(words, language_tag)
def search_word(val,syn,res):
    try:
        lis = []
        for wor in res:
            if wor in val:
                lis.append(val)
            else:
                synonym = re.sub("[/{/}/']+","",syn)
                for wor_2 in synonym.split(','):
                    if wor in wor_2:
                        lis.append(wor_2)
        if len(lis) == 0:
            return "Not Applicable"
        else:
            return set(lis)
    except:
        return "Error in fixing"
def unicode_to_english(s):
    return unicodedata.normalize('NFKD', s).encode('ASCII', 'ignore').decode('utf-8')


def re_clean(words, language_tag):
    #print(words)
    if str(language_tag)[0:2] == "en":
        anomoly_list = []
        for x in words.split():
            if language_tag != 'ja_JP':
                # if len(x) < 3:
                #     #return False
                #     anomoly_list.append(x)
                #     continue
                scent_en = unicode_to_english(x)
                len_eq = len(x) == len(scent_en)

                if not len_eq:
                    anomoly_list.append(x)
                    continue
                    #return False

                match = re.search('[a-z0-9°\'\"]+', scent_en.lower())

                if match != None:
                    #anomoly_list.append(x)
                    if len(match.group(0)) == len(x):
                        continue
                    else:
                        anomoly_list.append(x)
                else:
                    anomoly_list.append(x)
                    continue
                    #return False
            else:
                if x.isdigit() or any(i.isdigit() for i in x) or re.search('[a-z]', x.lower()):
                    #return False
                    anomoly_list.append(x)
                    continue

                if x.translate(string.punctuation).isalnum():
                    continue
                else:
                    anomoly_list.append(x)
                    continue
        if len(anomoly_list) == 0:
            return "Not Applicable"

        return anomoly_list
    else:
        return "Language Discrepancy"
# def lang_detect(x):
#     return gs.detect(str(x))

def Other_Lang(words,language_tag):
    anomoly_list = []
    for x in words.split():
        if str(language_tag)[0:2] == "fr":
            catch = re.fullmatch("[a-zA-Z0-9àâäèéêëîïôœùûüÿçÀÂÄÈÉÊËÎÏÔŒÙÛÜŸÇ’\'°]+", str(x),flags=re.IGNORECASE)
            if catch == None:
                anomoly_list.append(str(x))
        elif str(language_tag)[0:2] == "es":
            catch = re.fullmatch("[a-zA-Z0-9ñáéíóúü’\'°]+", str(x),flags=re.IGNORECASE)
            if catch == None:
                anomoly_list.append(str(x))
        elif str(language_tag)[0:2] == "de":
            catch = re.fullmatch("[a-zA-Z0-9äöüÄÖÜß°]+", str(x),flags=re.IGNORECASE)
            if catch == None:
                anomoly_list.append(str(x))
        elif str(language_tag)[0:2] == "it":
            catch = re.fullmatch("[a-zA-Z0-9áàèéìíîòóùú’\'\"°]+", str(x),flags=re.IGNORECASE)
            if catch == None:
                anomoly_list.append(str(x))
        elif str(language_tag)[0:2] == "zh":
            catch = re.fullmatch(r'[\u4e00-\u9fff]+', str(x))
            if catch == None:
                anomoly_list.append(str(x))
        elif str(language_tag)[0:2] == "ja":
            catch = re.fullmatch(r'[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf]+', str(x))
            if catch == None:
                anomoly_list.append(str(x))
        elif str(language_tag)[0:2] == "pt":
            catch = re.fullmatch(r'[\'\"°0-9A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ]+', str(x))
            if catch == None:
                anomoly_list.append(str(x))
        elif str(language_tag)[0:2] == "pl":
            catch = re.fullmatch(r'[\'\"°0-9AaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrSsŚśTtUuWwYyZzŹźŻż]+', str(x))
            if catch == None:
                anomoly_list.append(str(x))
        elif str(language_tag)[0:2] == "sv":
            catch = re.fullmatch(r'[0-9a-zA-ZäöåÄÖÅ\'\"°]+', str(x))
            if catch == None:
                anomoly_list.append(str(x))
        elif str(language_tag)[0:2] == "tr":
            catch = re.fullmatch(r'[a-zA-Z0-9ğüşöçİĞÜŞÖÇ\'\"°]+', str(x))
            if catch == None:
                anomoly_list.append(str(x))
        elif str(language_tag)[0:2] == "ar":
            catch = re.fullmatch(r"[ء-ي]+", str(x))
            if catch == None:
                anomoly_list.append(str(x))

    return anomoly_list

df  = pd.read_excel(r'C:\Users\louijose\Desktop\Anomiles\all_gls_ar.xlsx')
#result = []
#for val,syn in zip(df['Valid'],df['Synonyms']):
    #result.append(re_clean((val,syn)))
#df['result_1'] = df.Valid.str.cat(df['Synonyms'])
#df['result'] = df[['Valid', 'Synonyms']].agg(' '.join, axis=1)
#df['result'] = df[['Valid', 'Synonyms']].apply(lambda x: ' '.join(x), axis=1)
df['result'] = df['Valid'].astype(str)+ " " + df['Synonyms'].astype(str)
# df["result_1"] =
df['result'] = df['result'].apply(lambda x:x.translate(
                        str.maketrans(string.punctuation,' '*len(string.punctuation))))
#df['result'] = df['result'].apply(lambda x:x.translate(
                        #str.maketrans("'{}",' '*len("'{}"))))

#df['result_2'] = df['result_1'].apply(lambda x: re.sub("[\{\}\']+",'',str(x)))
df['result'] = df['result'].apply(lambda x:re.sub(' {2,}',' ',str(x)))
df['result'] = df[['result','MP']].apply(lambda x:language_selection(x['result'],x['MP']),axis=1)
final_list = []
for val,syn,res in zip(df['Valid'],df['Synonyms'],df['result']):
    if res == "Not Applicable":
        final_list.append("Not Applicable")
    else:
        final_list.append(search_word(val,syn,res))
df['result'] = final_list
#df['anomily'] = df['Valid'].apply(lambda x : re_clean(x))
df.to_excel(r'C:\Users\louijose\Desktop\Anomiles\results_ar.xlsx',index=False)