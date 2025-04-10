import json
import re

import pandas as pd
import datetime
import array as arr
# a = arr.array('i',[1,2,3])
# for i in range(0,3):
#     print(a[i])
# a.insert(1,4)
# for i in (a):
#     print(i)
# b = arr.array("d",[2.5,3.2,3.3])
# for i in range(0,3):
#     print(b[i])
# print("check")
# print(b.pop(2))
# b.remove(2)


#df_latex = pd.read_csv(r'C://Users//louijose//Desktop//Autotitle-files//Latex-Input//NA//1//NA-1-20230917', delimiter="\t")
#df_latex.to_csv(r'C://Users//louijose//Desktop//Autotitle-files//Latex-Input//NA//1//output.csv',index=False)
#Myset = frozenset(["a","b","e"])
#Myset2 = {"c","d","a"}
#print(type(Myset))

#a = "hello"
#print(list(a))
#cal_data = datetime.datetime.today().isocalendar()
#wk = cal_data[1]
#print(wk)


# yr = 2023
# wk = 30
# market = 'US'
# df_3p = pd.read_excel(r'//DESKTOP-N47RP8H//Users//khabiyaa//cape//CAPE WW//' + str(yr) + '_3P_allocation\WEEK ' + str(wk) + '\\SHERLOCK\\3P_CAPE_SHERLOCK_OUPUT_WEEK_' + str(wk) + '_' + market +'.xlsx')
#
#
# df_3p = df_3p[((df_3p['GL'].isin(['Apparel','Shoes'])) & (pd.isna(df_3p["variation_theme_description"]))) | ~df_3p['GL'].isin(['Apparel','Shoes'])]
# df_3p = df_3p[["ASIN","CAPE_TITL_BRAND","CAPE_TITL_SIZE","CAPE_TITL_COLOR","CAPE_TITL_MODEL_NO"]]
#
# df_1p = pd.read_excel(r'//DESKTOP-N47RP8H//Users//khabiyaa//cape//CAPE WW//2023//WEEK 30//SHERLOCK//CAPE_SHERLOCK_OUPUT_WEEK_30_US.xlsx')
# df_1p = df_1p[((df_1p['GL'].isin(['Apparel','Shoes'])) & (pd.isna(df_1p["variation_theme_description"]))) | ~df_1p['GL'].isin(['Apparel','Shoes'])]
# df_1p = df_1p[["ASIN","CAPE_TITL_BRAND","CAPE_TITL_SIZE","CAPE_TITL_COLOR","CAPE_TITL_MODEL_NO"]]
#
#
# df_cape_final = df_3p._append(df_1p,ignore_index=False)
#
# df_latex = pd.read_csv(r'C://Users//louijose//Desktop//Autotitle-files//Latex-Input//NA//1//NA-1-20230723',delimiter="\t",header=None)
# df_latex = df_latex.iloc[:,7:21]
# df_latex.rename(columns={7:"mp_id",9:"gl_id",10:"ASIN"},inplace=True)
# df_final = pd.merge(df_cape_final,df_latex,how="inner",on="ASIN")
#
# df_final = df_final.drop_duplicates(subset=["ASIN"])
# df_iop = pd.read_json(r"C://Users//louijose//Desktop//Autotitle-files//IOP-Input//NA//1//part-00000-da4ca50c-db1b-48ae-b0f0-54b55da2ff14-c000.json",lines=True)
# #df_iop = df_iop.dropna(thresh=7)
# #df_iop = df_iop.drop(['MerchantID'],axis=1)
#
# #df_iop = df_iop.drop_duplicates(subset=["ASIN"])
# #df_iop = df_iop[:104800]
# #df_iop.to_excel(r'C://Users//louijose//Desktop//CAPE//iop-df.xlsx',index=False)
#
# df_test = pd.merge(df_final,df_iop,how="outer",on="ASIN")
#
#
# # cols = list(range(1,23))
# # df_test.drop(df_test.columns[cols], axis=1,inplace=True)
#
# df_test.to_excel(r'C://Users//louijose//Desktop//CAPE//result-7.xlsx',index=False)
# import re
# def titleExtract(attrDatas):
#     for attdat in attrDatas:
#         if pd.isna(attdat):
#             continue
#         result = re.findall("\[(.*?)\]", attdat)
#         if len(result) > 0:
#             if result[2] != '':
#                 return result[2][1:-1]
#             return result[2]
#     return ''
#
# titleExtract(["[5Packs]ORICO 2.5 SSD SATA to 3.5 Hard Drive Adapter Internal Drive Bay Converter Mounting Bracket Caddy Tray for 7 / 9.5 / 12.5mm 2.5 inch HDD / SSD with SATA III Interface(1125SS-5)]")

# try:
#
#     num1 = int(input())
#
#     num2 = int(input())
#
#     result = num1 / num2
#
#     print("The result is:", result)
#
# except ZeroDivisionError:
#
#     print("Error: Cannot divide by zero.")

def length(n):
    length = 0
    while (n!=0):
        length = length + 1
        n = n // 10
    return length

# num = int(input("Enter a number: "))
# rem = sum_num = 0
# len = length(num)
# n= num
# while (num > 0):
#     rem = num % 10
#     sum_num = sum_num + int(rem**len)
#     num = num//10
#     len = len-1
#
# if (sum_num==n):
#     print(str(n) + " is disarium")
# else:
#     print(str(n) + " is not disarium")

# updated_title = "Moustiquaire Porte Fenetre Magnétique 235x260 cm，Moustiquaire pour Portes，Fermeture Automatique,Facile à Installer,pour Porte de Balcon, Portes de Salon,Porte de Terrasse, Portes Extérieures,Blanc"
# sable_size = "235.4x260cm"
# size_update = str(sable_size).lower().replace("-", " ").replace("x", " ")
# print(size_update)
# size_check = [x for x in size_update.split() if " " + x + " " in " " + updated_title.lower() + " "]
# #print(size_check)
# numeric_matches = re.findall('[0-9\.]+',sable_size)
# print(numeric_check)


# def merge_lists(lst1, lst2):
#     i, j = 0, 0
#
#     merged = []
#
#     while i < len(lst1) and j < len(lst2):
#
#         if lst1[i] <= lst2[j]:
#
#             merged.append(lst1[i])
#
#             i += 1
#
#         else:
#
#             merged.append(lst2[j])
#
#             j += 1
#     #return merged
#     # if i < len(lst1):
#     #     merged.extend(lst1[i:])
#     #
#     # if j < len(lst2):
#     #     merged.extend(lst2[j:])
#
#     return merged


#print(merge_lists([1, 3, 5], [2, 4, 6]))

# def max_subarray(nums):
#
#     max_sum = current_sum = nums[0]
#
#     for num in nums[1:]:
#         print(current_sum)
#         print(num)
#         current_sum = max(num, current_sum+num)
#         print(current_sum)
#         #max_sum = max(max_sum, current_sum)
#
#     #return max_sum
#
# nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
#
# result=max_subarray(nums)
#
# print
# import pandas as pd
# iop_input = r'C://Users//louijose//Desktop//LPD_BP//part-00000-ff39a0da-7f73-4071-9b43-d07bfd219973-c000.json'
#
# iop_df = pd.read_json(iop_input, lines=True)
#
# for ind,itn_row in iop_df.iterrows():
#     if not pd.isna(itn_row['Product_dercription']):
#         print(itn_row['Product_dercription'])

#iop_df.to_excel(r'C://Users//louijose//Desktop//LPD_BP//result-iop-mx-2.xlsx')

#with open('C://Users//louijose//Desktop//LPD_BP//part-00000-ff39a0da-7f73-4071-9b43-d07bfd219973-c000.json',errors='ignore') as user_f:
    #print(len(user_f.readlines()))

# tup = (1,2,3,4)
# tup1 = (4,5,6,7)
# tup = tup.__add__(tup1)
# print(tup)

#stt = 'BJBJJIU Kit de Pintura de Diamante ArtÃ­stico, Conjunto de ImÃ¡genes de Pintura de Diamante, Bordado de PedrerÃ­a de Pintura de Diamante para Adultos, NiÃ±os, Hogar, DecoraciÃ³n de Pared 40x30cm - Caballo'
#stt1 = 'BJBJJIU Kit de Pintura de Diamante Artístico, Conjunto de Imágenes de Pintura de Diamante, Bordado de Pedrería de Pintura de Diamante para Adultos, Niños, Hogar, Decoración de Pared 40x30cm - Caballo'
#print(len(stt1))
count = 0
#with open(r'C://Users//louijose//Desktop//LPD_BP//part-00000-93e036e2-0ea1-48c3-88c5-97f1d5d43109-c000.json','r',errors='ignore') as fil:
    #fill = fil.readlines()
    #for f in fill:

# cnt = 0
# df = pd.read_json(r'C://Users//louijose//Desktop//LPD_BP//part-00000-93e036e2-0ea1-48c3-88c5-97f1d5d43109-c000.json',lines=True)
# for ind,itn_row in df.iterrows():
#     if not re.search('^en_',itn_row['language_tag']):
#         continue
#     if itn_row['item'] == 'B0CB9JTCY7':
#         if itn_row['bullet_point2'] == '':
#             print("Joseph1")
#         elif pd.isna(itn_row['bullet_point2']):
#             print("Joseph2")
#         elif itn_row['bullet_point2'] is None:
#             print("Joseph3")
#         elif itn_row['bullet_point2'] == 'NULL':
#             print("Joseph4")
#         else:
#             print("Not Found")
#         break
    #print(itn_row['bullet_point3'])
    #cnt += 1
    #if cnt == 100:
        #break
        # dic = json.dumps(f)
        # print(type(dic))
        # print(dic)
        # count += 1
        # if count == 100:
        #     break
        #break

# invalid_df = pd.read_excel(r'C://Users//louijose//Desktop//LPD_BP//invalid_words_eng.xlsx')
# invalid_df['Replace Value'] = invalid_df['Replace Value'].fillna('')
# invalid_dic = dict(zip(invalid_df['Original Value '],invalid_df['Replace Value']))
# print(abc)
import ast
asin_list = []
confidence_list = []
browse_list = []

df = pd.read_excel(r'C://Users//louijose//Desktop//ITK//itk_defects_44.xlsx')
for inp, out in zip(df["input"],df["output"]):
    input_dic = json.loads(inp)
    input_dic_2 = input_dic["input"]['payload']['ITKModelOutput']['output']['response']
    input_dic_3 = json.loads(json.loads(input_dic_2))
    #print(input_dic_3)
    asin_list.append(input_dic_3['asin'])
    #bp_1 = input_dic_3['bullet_point1'].replace("'",'"')
    #print(bp_1)
    # bp_2 = json.dumps(bp_1)
    # bp_3 = json.loads(bp_2)
    # print(type(json.loads(bp_3)))
    #bp_1 = dict(bp_1)
    #print(bp_1)
    #json_data = ast.literal_eval(json.dumps(bp_1))
    #print(json_data['value'])
    #bp_1 = bp_1.replace("\'", "\"")
    #bp_1_1 = json.loads(bp_1)
    #print(type(bp_1_1))
    #print(bp_1)
    dic_1 = json.loads(out)
    dic_2 = json.loads(dic_1["executionDetail"]["ruleOutput"])
    confidence_list.append(dic_2["confidence_score"])
    browse_list.append(dic_2["patching"]["recommended_browse_nodes"][0]["value"])

df2 = pd.DataFrame({"ASIN":asin_list,"confidence_score":confidence_list,"predicted_BN":browse_list})
df2.to_excel(r'C://Users//louijose//Desktop//ITK//ITK_Validation_2.xlsx',index=False)

