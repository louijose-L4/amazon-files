import json
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
import subprocess
import os
import re
from tkinter import *
from tkinter import filedialog
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import glob
from selenium.webdriver.common.keys import Keys
import shutil
import selenium.webdriver.support.ui as ui
import warnings
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

warnings.filterwarnings("ignore")

mp_dic = {"uk": "3", "de": "4", "fr": "5", "es": "44551", "it": "35691", "in": "44571", "jp": "6", "ca": "7",
               "br": "526970", "nl": "328451", "au": "111172", "ae": "338801", "sa": "338811", "mx": "771770",
               "eg": "623225021", "cn": "3240", "pl": "712115121", "se": "704403121", "338851": "tr","us":"1"}
lang_dic = {"3": "en", "4": "de", "5": "fr", "44551": "es", "35691": "it", "1": "en", "7": "en", "44571": "en",
                 "526970": "pt", "6": "ja", "328451": "nl", "111172": "en", "338801": "en", "338811": "en",
                 "771770": "es", "623225021": "en", "3240": "zh", "712115121": "pl", "704403121": "se", "338851": "tr","1":"us"}
lang_trans = {"uk": "en", "fr": "fr", "es": "es", "it": "it", "de": "de", "us": "en", "ca": "en", "jp": "ja",
                   "br": "es", "in": "en", "nl": "nl", "au": "en", "ae": "en", "sa": "en", "mx": "pt", "eg": "en",
                   "cn": "zh", "pl": "pl", "se": "se", "tr": "tr"}

lang_tag_dic = {3:"en_GB",4:"de_DE",5:"fr_FR",44551:"es_ES",35691:"it_IT",6:"ja_JP",7:"en_CA",526970:"pt_BR",
                328451:"nl_NL",111172:"en_AU",338801:"en_AE",338811:"ar_SA",771770:"es_MX",623225021:"ar_EG",3240:"zh_CN",
                712115121:"pl_PL",704403121:"sv_SE",338851:"tr_TR",1:"en_US"}

#mp_dic = {"uk": "3","de": "4", "fr": "5" ,"es" : "44551" ,"it":"35691"}
#lang_dic = {"3":"en","4":"de","5":"fr","44551":"es","35691":"it"}
#lang_trans = {"uk": "en","fr": "fr","es": "es","it": "it","de":"de"}
region_dic =  {"uk": "eu","de": "eu", "fr": "eu" ,"es" : "eu" ,"it":"eu","in":"eu","jp":"fe","ca":"na","br":"na","us":"na","au":"fe","ae":"eu","sa":"eu","nl":"eu","mx":"na","eg":"eu","cn":"cn","tr":"eu","se":"eu","pl":"eu"}



def gui_app():
    root = Tk()
    root.title("Demeter Application")

    def click():
        global fileNam
        fileNam = filedialog.askopenfilename()
        root.destroy()

    wid = root.winfo_screenwidth()/2
    heig = root.winfo_screenheight()/2
    x_cor = wid-125
    y_cor = heig-36
    root.geometry("%dx%d+%d+%d"%(250,100,x_cor,y_cor))
    frame_name = Frame(root,bg="#ADD8E6")
    label_1 = Label(frame_name,text = "Please choose a file path",width = "20",height="1",bg="#D3D3D3",font="Times 16")
    button_1= Button(frame_name,text = "Click",bg="#D3D3D3",font="Times 14",width = "4",height ="1",command=click)
    label_1.grid(row=1,column=1)
    button_1.grid(row=3,column=1)
    frame_name.grid(row=1,column=1)
    root.mainloop()

def browser_open():
    dir_path = os.path.dirname(fileNam)

    df = pd.read_excel(fileNam)
    attval_unit = df[['attribute', 'attribute_type']].apply(lambda x: '|'.join(x), axis=1)
    attributeList = list(set(attval_unit))
    attribute_dic = {}
    for att in attributeList:
        attHeadSplit = str(att).split(".")
        imv2 = str(attHeadSplit[0]).strip()
        attribute_dic[imv2] = att
    print(attribute_dic)
    f = open(dir_path + '//asin.txt', 'w+')

    for asin in df['ASIN']:
        f.write(str(asin) + "\n")

    f.close()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument(r"--user-data-dir=C:\Users\louijose\AppData\Local\Google\Chrome\User Data")
    service = Service(
        executable_path=r'C://Users//' + os.environ["USERNAME"] + '//Desktop//chromedriver-win64//chromedriver.exe')
    bot = webdriver.Chrome(service=service,options=chrome_options)
    #time.sleep(50)
    time.sleep(10)

    bot.maximize_window()
    wait = ui.WebDriverWait(bot, 300)
    dic = {}
    export_dic = {}
    region_list = []
    region_collections = {"eu": ["uk", "de", "fr", "es", "it", "in", "ae", "sa", "nl", "eg"], "fe": ["jp", "au"],
                               "na": ["ca", "br", "us", "mx"], "cn": ["cn"]}
    lang_columns = df.columns[6:]
    for mp in lang_columns:
        mp = mp.lower()
        print(mp)
        #url = "https://browse-query-editor-na.aka.amazon.com/?marketplaceId=" + mp_dic[mp]
        url = "https://browse-query-editor-" + region_dic[mp] + ".aka.amazon.com/?marketplaceId=" + mp_dic[mp]
        time.sleep(5)
        #url = "https://browse-query-editor-eu.aka.amazon.com/?marketplaceId=" + mp_dic[mp]
        bot.implicitly_wait(20)
        bot.get(url=url)
        time.sleep(5)
        while re.search("midway", bot.current_url):
            time.sleep(5)
        time.sleep(20)
        #bot.find_element(By.CLASS_NAME,"file-loading").send_keys(dir_path + '//asin.txt')
        bot.find_element(By.CLASS_NAME, "file-loading").send_keys(r'C:\Users\louijose\Desktop\Demeter\asin.txt')
        time.sleep(3)
        for ky in attribute_dic.keys():
            #attribute_sep = str(attribute_dic[ky]).split("|")
            #att_val = attribute_sep[0]
            #att_type = attribute_sep[1]

            bot.find_element(By.XPATH,"//span[@id='react-select-2--value']//input").send_keys(ky)
            time.sleep(3)
            bot.find_element(By.XPATH,"//span[@id='react-select-2--value']//input").send_keys(Keys.ENTER)
            bot.find_element(By.XPATH,"//span[@id='react-select-2--value']//parent::div//span[@class='Select-arrow-zone']").click()

        bot.find_element(By.XPATH,"//button[contains(text(),'Export')]").click()
        time.sleep(5)
        bot.find_element(By.XPATH,"//label[contains(text(),'Enhanced')]//parent::div//span[text()='OFF']").click()
        time.sleep(4)
        #bot.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/div[6]/div[1]/div/div/div/div[5]/div/pre').click()
        bot.find_element(By.XPATH,"//div[@class='CodeMirror-gutter-wrapper']//parent::div//pre").click()
        time.sleep(3)
        for cn, ky in enumerate(attribute_dic.keys()):
            attribute_sep = str(attribute_dic[ky]).split("|")
            att_val = attribute_sep[0]
            att_type = attribute_sep[1]

            bot.find_elements(By.TAG_NAME,'textarea')[3].send_keys(att_val)
            #if re.search("height|length|width|weight", attribute_dic[ky], flags=re.IGNORECASE):
            if re.search("unit", att_type, flags=re.IGNORECASE):
                attributeUnitVal = str(att_val).replace(".value", "")
                attributeUnitVal += ".unit"
                bot.find_elements(By.TAG_NAME, 'textarea')[3].send_keys(Keys.ENTER)
                time.sleep(2)
                bot.find_elements(By.TAG_NAME,'textarea')[3].send_keys(attributeUnitVal)
            if not cn == len(attribute_dic) - 1:
                bot.find_elements(By.TAG_NAME, 'textarea')[3].send_keys(Keys.ENTER)
        time.sleep(3)
        btn = bot.find_element(By.XPATH,"//button[text()='Export']")
        location = btn.location["y"] - 100
        bot.execute_script("window.scrollTo(0,%d);" % location)
        btn.click()
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Exports UI Link']")))
        bot.find_element(By.XPATH,"//a[text()='Exports UI Link']").click()
        time.sleep(3)
        bot.find_element(By.XPATH,"//button[text()='Close']").click()
        chld = bot.window_handles[1]
        parnt = bot.window_handles[0]
        bot.switch_to.window(chld)
        time.sleep(3)
        wait.until(EC.presence_of_element_located((By.XPATH, "//tbody//tr//td[4]")))
        export_id = bot.find_element(By.XPATH,"//tbody//tr//td[1]").text
        #result = bot.find_element_by_xpath("//tbody//tr//td[4]").text
        export_dic[mp] = export_id

        if not region_dic[mp] in export_dic:
            export_dic[mp] = export_id
        if not region_dic[mp] in region_list:
           region_list.append(region_dic[mp])
        bot.close()
        time.sleep(2)
        bot.switch_to.window(parnt)

        print(export_dic)
        print(region_list)
    for reg in region_list:
        url = "https://browse-query-editor-" + reg + ".aka.amazon.com/exportTaskList"
        bot.get(url=url)
        mp_list = region_collections[reg]
        for ex_mp in mp_list:
            if ex_mp in export_dic:
                exprt_id = export_dic[ex_mp]
                my_ele = bot.find_element(By.XPATH,"//td[text()='" + str(exprt_id)+ "']//parent::tr//td[10]")
                location = my_ele.location["y"] - 100
                bot.execute_script("window.scrollTo(0,%d);" % location)
                result = str(bot.find_element(By.XPATH,"//td[text()='" + str(exprt_id)+ "']//parent::tr//td[10]").text).strip()
                while result != "Click here":
                    time.sleep(5)
                    bot.refresh()
                    result = bot.find_element(By.XPATH,"//td[text()='" + str(exprt_id)+ "']//parent::tr//td[10]").text
                    print(result)
                if result == "Click here":
                   bot.find_element(By.XPATH,"//td[text()='" + str(exprt_id)+ "']//parent::tr//td[10]//a").click()
                time.sleep(5)
                while not os.path.exists(r'C://Users//' + os.environ["USERNAME"] + '//Downloads//decoder-export-results-' + exprt_id + '.csv'):
                    time.sleep(2)
                latest_file = r'C://Users//' + os.environ["USERNAME"] + '//Downloads//decoder-export-results-' + exprt_id + '.csv'
                shutil.copyfile(latest_file,dir_path + '//' + ex_mp + '.csv')
                dic[ex_mp] = dir_path + '//' + ex_mp + '.csv'
    return attribute_dic, df, dic, bot, dir_path

def translation_func(attribute_dic,df,dic):
    filestamp = str(time.time()).split(".")[0]
    source_lang_list = []
    source_list_asins = []
    source_list_values = []
    source_list_pt = []
    dest_lang_list = []
    att_name_list = []


    lang_columns = df.columns[6:]
    src_mp_id = df.iloc[0,0]
    #src_lang = lang_trans[lang_dic[str(src_mp_id)]]
    src_lang = lang_dic[str(src_mp_id)]
    for mp in lang_columns:
        col_index = df.columns.get_loc(mp)
        mp = mp.lower()
        #print(mp)
        dest_lang = lang_trans[mp]
        #lang = mp
        mpData = pd.read_csv(dic[mp])
        for ky in attribute_dic.keys():
            att_name = str(attribute_dic[ky]).split("|")[0]
            mpData_2 = mpData[pd.isnull(mpData[att_name])]
            invalid_Data = mpData[mpData[att_name]== "INVALID DATA"]
            mpData_2 = mpData_2._append(invalid_Data,ignore_index= False)
            asinLen = len(mpData_2['ASIN'])

            for i, cols in enumerate(zip(mpData_2['ASIN'], mpData_2[mpData_2.columns[1]])):
                #valid = cols[1]
                #print(cols)
                asin = cols[0]
                valid = cols[1]
                if str(valid) == "INVALID ASIN":
                     continue
                if i % 100 == 0:
                    print(asin, str(i) + "---> out of " + str(asinLen) + "--->" + str(mp))
                ind = df.index[(df["ASIN"] == asin) & (df["attribute"] == att_name)].tolist()
                attVal = str(df.iloc[ind[0],5])
                df.iloc[ind[0],col_index] = attVal
                if src_lang != dest_lang:
                    source_lang_list.append(src_lang)
                    source_list_asins.append(asin)
                    source_list_pt.append(str(df.iloc[ind[0],2]))
                    source_list_values.append(attVal)
                    dest_lang_list.append(dest_lang)
                    att_name_list.append(att_name)

    if len(source_list_asins) != 0:
        translation_df = pd.DataFrame({"source_lang":source_lang_list,"asin":source_list_asins,"pt":source_list_pt,"source_values":source_list_values,"destination_lang":dest_lang_list})
        translation_df["enrichment"] = "enrichment"
        file_name = os.environ["USERNAME"] + "-"  + filestamp
        translation_df.to_csv(dir_path + "//" + str(file_name) + ".csv",index=False,header=False)
        translation_df["attribute"] = att_name_list
        #translation_df.to_excel(dir_path + "//" + str(file_name) + "-test.xlsx",index=False)
    else:
        translation_df = pd.DataFrame()
        #file_name = os.environ["USERNAME"] + "-" + filestamp
    #df.to_excel(r'C://Users//louijose//Desktop//EU-Localization//HIP-40//test-1.xlsx',index=False)
    return df,translation_df
    # dfVal = df[df["ASIN"] == asin]
                # attVal = dfVal.iloc[0, 3]
                # # transVal = findTransVal(asin,desMpDf)
                # df.iloc[ind[0], col] = transVal

# def s3_translation(output_df,bot,dir_path,s3_input_df,file_name):
#     wait = ui.WebDriverWait(bot, 300)
#
#     lang_trans = {"uk": "en","fr": "fr","es": "es","it": "it","de":"de","us":"en","ca":"en","jp":"ja","br":"es","in":"en","nl":"nl","au":"en","ae":"en","sa":"en","mx":"pt","eg":"en","cn":"zh"}
#
#
#     s3_file = file_name + '.json'
#     s3_input_df.to_csv(dir_path + '//' + s3_file,header=False,index=False)
#     bot.get("https://s3.console.aws.amazon.com/s3/buckets/selection-translate-service?region=us-east-1&prefix=input/enrichment/&showversions=false")
#     time.sleep(3)
#     bot.find_element(By.XPATH,"//span[text()='Upload']").click()
#     time.sleep(2)
#
#     bot.find_element(By.XPATH,"//input[@class='upload-file-table__file-input']").send_keys(dir_path + '//' + s3_file)
#
#     bot.find_element(By.XPATH,"//span[text()='" + s3_file + "']//parent::span//parent::td//preceding-sibling::td//awsui-checkbox").click()
#     ele = bot.find_element(By.XPATH,"//button//span[text()='Upload']")
#     location = ele.location["y"] - 100
#     bot.execute_script("window.scrollTo(0,%d);" % location)
#
#     ele.click()
#     time.sleep(5)
#     while not bot.find_element(By.XPATH,"//div[text()='Upload succeeded']").is_displayed():
#         time.sleep(3)
#     bot.get("https://s3.console.aws.amazon.com/s3/buckets/selection-translate-service-output?region=us-east-1&prefix=output/&showversions=false")
#     time.sleep(3)
#     isLinkFound = False
#     s3_file_out = s3_file + ".out"
#     while True:
#         objLinks = bot.find_elements(By.XPATH,"//span[@class='object-link']//a//span")
#         for link in objLinks:
#             if link.text == s3_file_out:
#                 isLinkFound = True
#                 bot.get("https://s3.console.aws.amazon.com/s3/object/selection-translate-service-output?region=us-east-1&prefix=output/" + str(link.text))
#                 time.sleep(2)
#                 wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Download']")))
#                 bot.find_element(By.XPATH, "//span[text()='Download']").click()
#                 time.sleep(5)
#                 latest_file = "downloadfile"
#
#                 while re.search("download(?!s)", str(latest_file)):
#                     # list_of_files = glob.glob(self.dir_path +'//*')
#                     list_of_files = glob.glob(r'C://Users//' + os.environ["USERNAME"] + '//Downloads//*')
#                     time.sleep(3)
#                     latest_file = max(list_of_files, key=os.path.getctime)
#                     # print(latest_file)
#                 print(latest_file)
#                 shutil.copyfile(latest_file, dir_path + "//" + file_name  + ".csv.out")
#                 break
#         if isLinkFound == True:
#             break
#         else:
#             time.sleep(20)
#             bot.find_element(By.XPATH, "//awsui-button[@id='refresh']//button").click()
#
#
#     s3_data = open(dir_path + "//" + str(file_name) + ".csv.out","r",encoding='utf-8',errors='ignore')
#     nlines = s3_data.readlines()
#     translated_values = []
#     for nl in nlines:
#         trans_data = nl.split("translated_text")
#         dest_data = trans_data[1].replace("\n", "").replace("': ", "").replace('}"', "")
#         if re.search(r"\\u[a-zA-Z0-9]{4}", dest_data, flags=re.IGNORECASE):
#             matches = re.findall(r"\\u[a-zA-Z0-9]{4}", dest_data, flags=re.IGNORECASE)
#             for match in matches:
#                 match_updated = match[2:]
#                 match_updated = chr(int(match_updated, 16))
#                 dest_data = dest_data.replace(match, match_updated)
#                 print(dest_data)
#         translated_values.append(str(dest_data))
#     s3_input_df["translated_values"] = translated_values
#     #print(s3_input_df)
#     nrows = len(output_df)
#     ncolumns = len(output_df.columns)
#     for rn in range(nrows):
#         att = output_df.iloc[rn, 3]
#         for col in range(5, ncolumns):
#             if not pd.isna(output_df.iloc[rn, col]):
#                 asin = str(output_df.iloc[rn, 1])
#                 target_lang = lang_trans[str(output_df.columns[col]).lower()]
#                 translated_df = s3_input_df[(s3_input_df["asin"] == asin) & (s3_input_df["destination_lang"] == target_lang) & (s3_input_df["attribute"] == att)]
#                 trans_value = translated_df.iloc[0, 7]
#                 trans_value = trans_value[1:-1]
#                 output_df.iloc[rn, col] = trans_value
#     output_df.to_excel(dir_path + "//Output.xlsx",index=False)
#     return output_df



def s3_translation(output_df,bot,dir_path,s3_input_df):
    wait = ui.WebDriverWait(bot, 300)

    filestamp = str(time.time()).split(".")[0]
    #print(filestamp)

    lang_trans = {"uk": "en","fr": "fr","es": "es","it": "it","de":"de","us":"en","ca":"en","jp":"ja","br":"es","in":"en","nl":"nl","au":"en","ae":"en","sa":"en","mx":"pt","eg":"en","cn":"zh","pl":"pl","se":"se","tr":"tr"}
    lang_dic = {"3": "en", "4": "de", "5": "fr", "44551": "es", "35691": "it", "1": "en", "7": "en", "44571": "en",
                     "526970": "pt", "6": "ja", "328451": "nl", "111172": "en", "338801": "en", "338811": "en",
                     "771770": "es", "623225021": "en", "3240": "zh","712115121":"pl","704403121":"se","338851":"tr"}


    nrows = len(output_df)
    ncolumns = len(output_df.columns)
    values_in_source = []
    source_lang = []
    destination = []
    pt_list = []
    asin_list = []
    attribute_name_list = []
    find_source_lang = lang_dic[str(output_df.iloc[0, 0])]
    for rn in range(nrows):
        for col in range(6,ncolumns):
            if not pd.isna(output_df.iloc[rn,col]):
                target_lang = lang_trans[str(output_df.columns[col]).lower()]
                if target_lang != find_source_lang:
                    attribute_name_list.append(str(output_df.iloc[rn, 3]))
                    values_in_source.append(str(output_df.iloc[rn,col]))
                    #source_lang.append(lang_trans[str(output_df.columns[col]).lower()])
                    source_lang.append(lang_dic[str(output_df.iloc[rn,0])])
                    #destination.append(lang_dic[str(output_df.iloc[rn,0])])
                    destination.append(lang_trans[str(output_df.columns[col]).lower()])
                    pt_list.append(str(output_df.iloc[rn,2]))
                    asin_list.append(str(output_df.iloc[rn,1]))
    if len(asin_list) > 0:
        s3_input_df = pd.DataFrame(
            {"asin": asin_list, "product_type": pt_list, "attribute": attribute_name_list, "source_lang": source_lang,
             "target_lang": destination, "attribute_value": values_in_source})
        #s3_input_df.to_excel(dir_path + "//result-1.xlsx",index=False)
        #s3_input_df = pd.DataFrame({"source_lang":source_lang,"asin":asin_list,"pt":pt_list,"source_values":values_in_source,"destination_lang":destination})
        #s3_input_df["enrichement"] = "enrichement"
        s3_file = os.environ["USERNAME"] + '-' + filestamp + '.json'
        #dict_list = s3_input_df.to_dict('records')
        dict_list = s3_input_df.T.to_dict().values()
        #print(dict_list)
        s3_write_file = open(dir_path + '//' + s3_file, "w",encoding='utf-8')
        for dic in dict_list:
            json.dump(dic, s3_write_file)
            # if len(dict_list)-1 == cnt:
            #     s3_write_file.writelines(dict_list[cnt])
            # else:
            #     s3_write_file.writelines(dict_list[cnt] + "\n")
            s3_write_file.write("\n")
        s3_write_file.close()

        #s3_input_df.to_csv(dir_path + '//' + s3_file,header=False,index=False)
        bot.get("https://s3.console.aws.amazon.com/s3/buckets/selection-translate-service?region=us-east-1&prefix=input/enrichment/&showversions=false")
        time.sleep(10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Upload']")))
        bot.find_element(By.XPATH,"//span[text()='Upload']").click()
        time.sleep(2)

        bot.find_element(By.XPATH,"//input[@class='upload-file-table__file-input']").send_keys(dir_path + '//' + s3_file)

        #bot.find_element(By.XPATH,"//span[text()='" + s3_file + "']//parent::span//parent::td//preceding-sibling::td//awsui-checkbox").click()
        ele = bot.find_element(By.XPATH,"//button//span[text()='Upload']")
        location = ele.location["y"] - 100
        bot.execute_script("window.scrollTo(0,%d);" % location)

        ele.click()
        time.sleep(5)
        while not bot.find_element(By.XPATH,"//div[text()='Upload succeeded']").is_displayed():
            time.sleep(3)
        bot.get("https://s3.console.aws.amazon.com/s3/buckets/selection-translate-service-output?region=us-east-1&prefix=output/&showversions=false")
        time.sleep(3)
        isLinkFound = False
        s3_file_out = s3_file + ".out"
        while True:
            objLinks = bot.find_elements(By.XPATH,"//span[@class='object-link']//a//span")
            for link in objLinks:
                if link.text == s3_file_out:
                    isLinkFound = True
                    bot.get("https://s3.console.aws.amazon.com/s3/object/selection-translate-service-output?region=us-east-1&prefix=output/" + str(link.text))
                    time.sleep(2)
                    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Download']")))
                    bot.find_element(By.XPATH, "//span[text()='Download']").click()
                    time.sleep(5)
                    #latest_file = "downloadfile"
                    while not os.path.exists(r'C://Users//' + os.environ["USERNAME"] + '//Downloads//' + s3_file_out):
                        time.sleep(2)
                    latest_file = r'C://Users//' + os.environ["USERNAME"] + '//Downloads//' + s3_file_out
                    # while re.search("download(?!s)", str(latest_file)):
                    #     # list_of_files = glob.glob(self.dir_path +'//*')
                    #     list_of_files = glob.glob(r'C://Users//' + os.environ["USERNAME"] + '//Downloads//*')
                    #     time.sleep(3)
                    #     latest_file = max(list_of_files, key=os.path.getctime)
                    #     # print(latest_file)
                    # print(latest_file)
                    shutil.copyfile(latest_file, dir_path + "//" + s3_file_out)
                    break
            if isLinkFound == True:
                break
            else:
                time.sleep(20)
                #bot.find_element(By.XPATH, "//awsui-button[@id='refresh']//button").click()
                bot.find_element(By.XPATH,"//button[@data-testid='refresh']").click()
        #DELETING THE S3 TRANSLATED OUTPUT FILE

        bot.get("https://s3.console.aws.amazon.com/s3/buckets/selection-translate-service-output?region=us-east-1&prefix=output/&showversions=false")
        time.sleep(3)
        check_length = bot.find_elements(By.XPATH,"//input[@placeholder='Find objects by prefix']")
        while len(check_length) == 0:
            time.sleep(2)
            check_length = bot.find_elements(By.XPATH, "//input[@placeholder='Find objects by prefix']")
        bot.find_element(By.XPATH,"//input[@placeholder='Find objects by prefix']").send_keys(s3_file_out)
        time.sleep(2)
        bot.find_element(By.XPATH,"//input[@placeholder='Find objects by prefix']").send_keys(Keys.ENTER)
        time.sleep(2)
        ele = bot.find_element(By.XPATH,"//span[text()='" + s3_file_out + "']/ancestor::tr//input")
        location = ele.location["y"]-100
        bot.execute_script("window.scrollTo(0,%d);" % location)
        ele.click()
        time.sleep(2)

        bot.find_element(By.XPATH,"//span[text()='Delete']").click()
        check_length_2 = bot.find_elements(By.XPATH,"//input[@placeholder='delete']")
        while len(check_length_2) == 0:
            check_length_2 = bot.find_elements(By.XPATH,"//input[@placeholder='delete']")
        bot.find_element(By.XPATH,"//input[@placeholder='delete']").send_keys("delete")
        time.sleep(1)
        delete_ele = bot.find_element(By.XPATH,"//button//span[text()='Delete objects']")
        location = delete_ele.location["y"] - 100
        bot.execute_script("window.scrollTo(0,%d);" % location)
        delete_ele.click()
        #bot.find_element(By.XPATH,"//span[text()='Delete objects']").click()
        time.sleep(5)

        #DELETING THE S3 TRANSLATED INPUT FILE

        bot.get("https://s3.console.aws.amazon.com/s3/buckets/selection-translate-service?region=us-east-1&prefix=input/enrichment/&showversions=false")
        time.sleep(3)
        check_length = bot.find_elements(By.XPATH,"//input[@placeholder='Find objects by prefix']")
        while len(check_length) == 0:
            time.sleep(2)
            check_length = bot.find_elements(By.XPATH, "//input[@placeholder='Find objects by prefix']")
        bot.find_element(By.XPATH,"//input[@placeholder='Find objects by prefix']").send_keys(s3_file)
        time.sleep(2)
        bot.find_element(By.XPATH,"//input[@placeholder='Find objects by prefix']").send_keys(Keys.ENTER)
        time.sleep(2)
        ele = bot.find_element(By.XPATH,"//span[text()='" + s3_file + "']/ancestor::tr//input")
        location = ele.location["y"]-100
        bot.execute_script("window.scrollTo(0,%d);" % location)
        ele.click()
        time.sleep(2)

        bot.find_element(By.XPATH,"//span[text()='Delete']").click()
        check_length_2 = bot.find_elements(By.XPATH,"//input[@placeholder='delete']")
        while len(check_length_2) == 0:
            check_length_2 = bot.find_elements(By.XPATH,"//input[@placeholder='delete']")
        bot.find_element(By.XPATH,"//input[@placeholder='delete']").send_keys("delete")
        time.sleep(1)
        delete_ele = bot.find_element(By.XPATH,"//button//span[text()='Delete objects']")
        location = delete_ele.location["y"] - 100
        bot.execute_script("window.scrollTo(0,%d);" % location)
        delete_ele.click()


        #bot.find_element(By.XPATH,"//span[text()='Delete objects']").click()


        #OPENING THE DOWNLOADED S3 TRANSLATED FILE

        s3_data = open(dir_path + "//" + os.environ["USERNAME"] + "-"  + filestamp + ".json.out","r",encoding='utf-8',errors='ignore')
        nlines = s3_data.readlines()
        translated_values = []
        for nl in nlines:
            trans_data = nl.split("translated_value")
            dest_data = trans_data[1].replace("\n", "").replace("': ", "").replace('}"', "")
            if re.search(r"\\u[a-zA-Z0-9]{4}|", dest_data, flags=re.IGNORECASE):
                matches = re.findall(r"\\u[a-zA-Z0-9]{4}|\\x[a-zA-Z0-9]{3}", dest_data, flags=re.IGNORECASE)
                for match in matches:
                    match_updated = match[2:]
                    match_updated = chr(int(match_updated, 16))
                    dest_data = dest_data.replace(match, match_updated)
                    #print(dest_data)
            translated_values.append(str(dest_data))
        s3_input_df["translated_values"] = translated_values
    #nrows = len(output_df)
    #ncolumns = len(output_df.columns)
    #find_source_lang = lang_dic[str(output_df.iloc[0,0])]
        for rn in range(nrows):
            for col in range(6, ncolumns):
                if not pd.isna(output_df.iloc[rn, col]):
                    target_lang = lang_trans[str(output_df.columns[col]).lower()]
                    if find_source_lang == target_lang:
                        output_df.iloc[rn, col] = str(output_df.iloc[rn, col]).encode('utf-8', 'replace').decode('utf-8')
                    else:
                        asin = str(output_df.iloc[rn, 1])
                        attribute_name = str(output_df.iloc[rn, 3])
                        translated_df = s3_input_df[(s3_input_df["asin"] == asin) & (s3_input_df["target_lang"] == target_lang) & (s3_input_df["attribute"] == attribute_name)]
                        trans_value = translated_df.iloc[0,6]
                        trans_value = trans_value[1:-1]
                        trans_value = str(trans_value).encode('utf-8', 'replace').decode('utf-8')
                        output_df.iloc[rn, col] = trans_value
        #output_df.to_excel(r'C://Users//louijose//Desktop//EU-Localization//HIP-55//result.xlsx',index=False)
        output_df.to_excel(dir_path + "//Output.xlsx",index=False)
        return output_df
    else:
        print("It does not require translation")
        output_df.to_excel(dir_path + "//Output.xlsx", index=False)
        return output_df
    bot.close()
    #os.kill(proc.pid, signal.SIGTERM)

def FRPG_sheet_creation(output_df,dir_path):
    code = '+++'
    codePlus = "'''"
    idx = 0
    output = []
    nrows_output_df = len(output_df)
    for cl in range(6, len(output_df.columns)):
        mp = str(output_df.columns[cl]).lower()
        for rn in range(nrows_output_df):
            if not pd.isna(output_df.iloc[rn, cl]):
                mp = output_df.columns[cl]
                attribute_complexity = str(output_df.iloc[rn, 3]).split(".")
                frpg_data = [output_df.iloc[rn, 1]]
                frpg_data.append(int(mp_dic[mp.lower()]))
                frpg_data.append(attribute_complexity[0])

                if len(attribute_complexity) == 2:
                    frpg_data.append(output_df.iloc[rn, cl])
                    val_dict = frpg_simStr(idx,frpg_data)
                else:
                    frpg_data.append(attribute_complexity[1])
                    frpg_data.append(output_df.iloc[rn, cl])
                    val_dict = frpg_comStr(idx,frpg_data)


                output.append(json.dumps(val_dict, indent=4, sort_keys=True, ensure_ascii=False)
                              .replace('\\', '')
                              .replace('"', '')
                              .replace(code, '"')
                              .replace(codePlus, "'"))

                idx += 1
        # col += 1
        if len(output) > 0:
            with open(dir_path + '//FRPG_Upload_Feed_' + str(mp) + '.txt', 'w', encoding='utf8') as handle:
                # w.write(json.dumps(output))
                for line in output:
                    # print(line)
                    handle.write(line + "\n")


def frpg_simStr(idx,frpg_data):
    code = '+++'
    codePlus = "'''"
    ASIN = frpg_data[0]
    MP_ID = frpg_data[1]
    asin = code + ASIN + code
    attr = str(frpg_data[2])
    attr_value = frpg_data[3]
    marketplaces = [MP_ID]
    language_tag = lang_tag_dic[MP_ID]

    product = {
    'item_id': [{'value': asin}],
    'merchant_suggested_asin': [{'value': asin}]
        }

    value = (code + attr_value + code).replace(';', ', ')
    product[attr] = [
        {'language_tag': code + language_tag + code ,'value': value}
    ]
    payload = {
    'marketplace_ids': marketplaces,
    'product': json.dumps(product,ensure_ascii=False)
    }
    val_dict = {
        'message_id': idx + 1,
        'sku': asin,
        'operation': 'partial_update',
        'payload_type': 'product_ion_2_0',
        'payload': codePlus + 'com.amazon.item_master.SkuSubmission@2.0' + codePlus + '::' + json.dumps(payload, ensure_ascii=False)
    }
    return val_dict

def frpg_comStr(idx,frpg_data):
    code = '+++'
    codePlus = "'''"
    ASIN = frpg_data[0]
    MP_ID = frpg_data[1]
    asin = code + ASIN + code
    imv2 = str(frpg_data[2])
    extraAtt = frpg_data[3]
    attr_value = frpg_data[4]
    marketplaces = [MP_ID]
    language_tag = lang_tag_dic[MP_ID]

    product = {
        'item_id': [{'value': asin}],
        'merchant_suggested_asin': [{'value': asin}]
    }

    value = (code + attr_value + code).replace(';', ', ')
    product[imv2] = [
        {
            extraAtt:
                [
                    {
                        'language_tag': code + language_tag + code,
                        'value': value,
                    }
                ]
        }
    ]
    value = (code + attr_value + code).replace(';', ', ')
    product[imv2] = [
        {
            extraAtt:
                [
                    {
                        'language_tag': language_tag,
                        'value': value,
                    }
                ]
        }

    ]
    payload = {
        'marketplace_ids': marketplaces,
        'product': json.dumps(product, ensure_ascii=False)
    }

    val_dict = {
        'message_id': idx + 1,
        'sku': asin,
        'operation': 'partial_update',
        'payload_type': 'product_ion_2_0',
        'payload': codePlus + 'com.amazon.item_master.SkuSubmission@2.0' + codePlus + '::' + json.dumps(payload,
                                                                                                        ensure_ascii=False)
    }
    return val_dict


if __name__ == '__main__':
    gui_app()
    attribute_dic, df, dic, bot, dir_path = browser_open()
    output_df,s3_input_df = translation_func(attribute_dic,df,dic)
    to_frpg_df = s3_translation(output_df,bot,dir_path,s3_input_df)
    FRPG_sheet_creation(to_frpg_df,dir_path)

    print("Completed!!!")






#
# def frpg_upload():
#     bot.execute_script("window.open('https://frpg-operations.amazon.com/index.html#/feed/submit?region=EU&realm=prod');")
#
#     chld = bot.window_handles[1]
#     bot.switch_to.window(chld)
#     for ifil in glob.glob(dir_path + '/FRPG*.txt'):
#         #if cnt >0:
#         print(ifil)
#         bot.get("https://frpg-operations.amazon.com/index.html#/feed/submit?region=EU&realm=prod")
#         time.sleep(5)
#         while re.search("midway", bot.current_url):
#             time.sleep(5)
#         time.sleep(3)
#         wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Account ID']")))
#         time.sleep(2)
#         bot.find_element(By.XPATH,"//input[@placeholder='Account ID']").send_keys("102886471312")
#         time.sleep(2)
#         bot.find_element(By.XPATH,"//button[contains(@class,'multiSelectButton')] ").click()
#         time.sleep(2)
#         #4113_POST_ION+LISTINGS_DATA
#         bot.find_element(By.XPATH,"//span[contains(text(),'4113')]").click()
#         time.sleep(2)
#         bot.find_element(By.XPATH,"//button[text()='Choose File']").click()
#         time.sleep(2)
#         autoit.win_active("Open")
#         ifil2 = str(ifil).replace('/','\\')
#         autoit.control_send("Open","Edit1",ifil2)
#         autoit.control_send("Open","Edit1","{ENTER}")
#         #bot.find_element(By.XPATH,"//input[@type='file']").send_keys(r'C://Users//louijose//Desktop//EU-Localization//HIP-3//FRPG_Upload_Feed_en.txt')
#         time.sleep(2)
#         bot.find_element(By.XPATH,"//button[text()='Submit']").click()
#         time.sleep(10)
#
#

