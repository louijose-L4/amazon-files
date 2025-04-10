import pandas as pd
import glob

#df = pd.read_excel(r'C://Users//louijose//Desktop//Autotitle//Brand_validation_1.xlsx')
#df['offer'] = "Joseph"
#df.to_excel(r'C://Users//louijose//Desktop//Autotitle//joo.xlsx',index=False)
# cnt = 0
# for asin,brd,title in zip(df["ASIN"],df["BRAND"],df["ITEM_NAME"]):
#     title_small = title.lower()
#     brand_split = brd.split(' ')
#     for bnd in brand_split:
#         if bnd.lower() in title_small:
#             cnt += 1
#             print(asin)
#             break
#
# print(cnt)

comments = ["mismatch in predicted model/sable model","title > 199 characters","mismatch in predicted brand/sable brand","mismatch in predicted color/sable color","mismatch in predicted size/sable size",
 "brand already exist","restricted words in brand"," invalid model","model already exist","size already exist","color already exist",
 "latex predicted brand","latex predicted size","latex predicted size","brand already exists","restricted words in brand","color has restricted words","size has restricted words","model not required"]

#for fil in
error_dic = {}
total_asins = 0
patched_asins = 0
total_defects = 0
defect_dic = {}

for filename in glob.iglob(r'C://Users//louijose//Desktop//Autotitle//Output//EU//**/*'):
    if str(filename).endswith(r'\result.xlsx'):
        print(filename)
        df = pd.read_excel(filename)
        #total_asins += len(df)
        #df_success = df[df["is_autopatch"] == 'Y']
        #patched_asins += len(df_success)
        df = df[df["is_autopatch"] == 'N']
        df2 = df[["ASIN","Comments"]]
        df.dropna(subset=['Comments'], inplace=True)
        # Defect level
        #for itn, comment in zip(df["ASIN"], df["Comments"]):
        for com in comments:
            df2 = df[df["Comments"].str.contains(com)]
            if not df2.empty:
                print(com)
                total_defects += len(df2)
                if com in defect_dic:
                    defect_dic[com] = defect_dic[com] + len(df2)
                else:
                    defect_dic[com] = len(df2)
defect_dic_2 = {}
for ky,val in defect_dic.items():
    defect_dic_2[ky] = [val]

df3 = pd.DataFrame(defect_dic_2)
df3.to_excel(r'C://Users//louijose//Desktop//Autotitle//defectr_val_result.xlsx',index=False)
print(total_defects)

                #if com in defect_dic:



#ASIN LEVEL
#         for itn, comment in zip(df["ASIN"],df["Comments"]):
#             for ct in comments:
#                 if ct in comment:
#                     if ct not in error_dic:
#                         error_dic[ct] = 1
#                     else:
#                         error_dic[ct] = error_dic[ct] + 1
#                     break
#
# error_dic_2 = {}
# for ky,val in error_dic.items():
#     error_dic_2[ky] = [val]
#
# df3 = pd.DataFrame(error_dic_2)
# df3.to_excel(r'C://Users//louijose//Desktop//Autotitle//error_val_result.xlsx',index=False)
# print(total_asins)
# print(patched_asins)




#ASIN level
