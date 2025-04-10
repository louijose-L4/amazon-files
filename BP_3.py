import pandas as pd
import json
import re

gl_dict = {'Toys': '21', 'Electronics': '23', 'Batteries': '44', 'Home Improvement': '60', 'Baby': '75',
           'Kitchen': '79',
           'Lawn and Garden': '86', 'Wireless': '107', 'PC': '147', 'Apparel': '193', 'Beauty': '194',
           'Furniture': '196',
           'Jewelry': '197', 'Luggage': '198', 'Pet Products': '199', 'Sports': '200', 'Home': '201',
           'Office Products': '229', 'Misc SDP': '236', 'Watches': '241', 'Gourmet': '251',
           'Art and Craft Supplies': '261', 'Automotive': '263', 'Major Appliances': '265',
           'Musical Instruments': '267',
           'Tires': '293', 'Shoes': '309', 'Grocery': '325', 'Biss': '328', 'Wireless_Accessory': '353',
           'Personal_Care_Appliances': '364', 'Wine': '370', 'Prescription_Drugs': '394', 'Camera': '421',
           'Mobile_Electronics': '422', 'Entertainment_Collectibles': '441', 'Pantry': '467',
           'Outdoors': '468', 'Tools': '469', 'Home Entertainment': '504', 'Luxury_Beauty': '510',
           'Fresh_Perishable': '540', 'Fresh_Produce': '541', 'Fresh_Prepared': '542',
           'Fresh_Ambient': '543', 'Softlines_Private_Label': '641', 'Health & Personal Care': '364'}

df2 = pd.read_excel(r'C://Users//louijose//Desktop//LPD_BP//Input_US_44_2.xlsx')

pd_dic = {}
bp_dic = {}

invalid_df = pd.read_excel(r'C://Users//louijose//Desktop//LPD_BP//invalid_words_eng.xlsx')
invalid_df['Replace Value'] = invalid_df['Replace Value'].fillna('')
invalid_dic = dict(zip(invalid_df['Original Value '],invalid_df['Replace Value']))


iop_input = r'C://Users//louijose//Desktop//LPD_BP//part-00000-93e036e2-0ea1-48c3-88c5-97f1d5d43109-c000.json'

iop_df = pd.read_json(iop_input, lines=True)

for ind,itn_row in iop_df.iterrows():
    if not re.search('^en_',itn_row['language_tag']):
        continue
    if not pd.isna(itn_row['product_description']):
        if itn_row['item'] not in pd_dic: #product_description
            if not pd.isna(itn_row['pd_l_tag']):
                pd_dic[itn_row['item']] = [{itn_row['pd_l_tag']: [itn_row['product_description']]}]
        else:
            is_tag = False
            for itn in pd_dic[itn_row['item']]:
                if itn_row['pd_l_tag'] in itn:
                    itn[itn_row['pd_l_tag']].append(itn_row['product_description'])
                    is_tag = True
                    #cnt += 1
                    break
            if is_tag == False:
                pd_dic[itn_row['item']].append({itn_row['pd_l_tag']: [itn_row['product_description']]})

    bullets = []
    bull_str = ''


    for ky in ["bullet_point0","bullet_point1","bullet_point2","bullet_point3"]:
        #if re.search('bullet',ky):
        if not pd.isna(itn_row[ky]):
            bullets.append(itn_row[ky])
    if len(bullets) > 0:
        if itn_row['item'] not in bp_dic:
            if not pd.isna(itn_row['language_tag']):
                bp_dic[itn_row['item']] = [{itn_row['language_tag']: bullets}]
            else:
                bp_dic[itn_row['item']] = [{'Unknown': bullets}]
        else:
            is_tag = False
            is_unknown = False
            if not pd.isna(itn_row['language_tag']):
                for itn in bp_dic[itn_row['item']]:
                    if "Unknown" in itn:
                        is_unknown = True
                    if itn_row['language_tag'] in itn:
                        #itn[item_dic['language_tag']] += "," + bull_str
                        itn[itn_row['language_tag']] += bullets
                        is_tag = True
                        break
                if is_tag == False:
                    bp_dic[itn_row['item']].append({itn_row['language_tag']: bullets})
            elif is_unknown == True:
                bp_dic[itn_row['item']]['Unknown'] += bullets
            else:
                bp_dic[itn_row['item']].append({'Unknown': bullets})


bp_asin_list = []
pd_asin_list = []
desc_list = []

bullet_list = []
bp_context_list = []
pd_context_list = []
bp_gl_list = []
pd_gl_list = []
bul_1 = []
bul_2 = []
bul_3 = []


for ind,row in df2.iterrows():
    if row['CAPE_BP_AVAIL'] == 'N' or (row['CAPE_BP_AVAIL'] == 'Y' and row['bullet_point_count'] > 0 and row['bullet_point_count'] < 3):
        bp_exist = []
        try:
            if not pd.isna(row['BULLET_POINT']):
                bp_exist.append(row['BULLET_POINT'])
        except:
            bp_exist.append('')
        try:
            if not pd.isna(row['BULLET_POINT2']):
                bp_exist.append(row['BULLET_POINT2'])
        except:
            bp_exist.append('')
        #else:
            #bp_exist.append('')
            #bul_2.append('')
        try:
            if not pd.isna(row['BULLET_POINT3']):
                bp_exist.append(row['BULLET_POINT3'])
        except:
            bp_exist.append('')
        #else:
            #bp_exist.append('')
            #bul_3.append('')
        exist_bp_string = ''.join(bp_exist)
        exist_bp_string = exist_bp_string.replace(' ','')
        # if exist_bp_string != '':
        #     print(exist_bp_string)
        if len(exist_bp_string) < 50 or len(bp_exist) < 3:
            bp_org_no = len(bp_exist)

            is_bull = False
            bull_str = ''

            if row['ASIN'] in bp_dic:

                bp_list = bp_dic[row['ASIN']]
                for lang_dic in bp_list:
                    if "en_US" in lang_dic:
                        bull_pts = list(set(lang_dic["en_US"]))
                        bull_pts = [x for x in bull_pts if x != 'NULL']
                        for bp in bull_pts:
                            if bp in bp_exist:
                                continue
                            else:
                                bp_exist.append(bp)
                                if len(bp_exist) >= 3:
                                    break
                                break
                        if bp_org_no < len(bp_exist):
                            for bul in bp_exist:
                                bull_str += bul + ';'
                            bull_str = bull_str[:-1]

                            for ky,val in invalid_dic.items():
                                if ky in bull_str:
                                    bull_str = bull_str.replace(ky,val)

                            bullet_list.append(bull_str)
                            bp_asin_list.append(row['ASIN'])
                            #bul_1.append(row['BULLET_POINT'])
                            #bul_2.append(row['BULLET_POINT2'])
                            #bul_3.append(row['BULLET_POINT3'])
                            is_bull = True
                            #bp_cxt_dic['bp_iop'] = bull_str
                            #bullet_list.append(bull_pts)
                            #is_bull = True
                            break
                        else:
                            break


                if is_bull == False:
                    bullet_list.append("")

            else:
                bullet_list.append("")



#product_description

#for ind,row in df2.iterrows():
    #if row['CAPE_LPD_AVAIL'] == 'N':
    if row['Eternity Output LPD Len'] == 0:
        #is_lpd = False
        #pd_gl_list.append(gl_dict[row['GL']])
        #pd_cxt_dic = {'invl_chr': '', 'offer_type': '3P', 'lpd_iop': ''}
        #pd_asin_list.append(row['ASIN'])
        if row['ASIN'] in pd_dic:
            lpd_list = pd_dic[row['ASIN']]
            if not pd.isna(row['Eternity Output LPD']):
                #lpd_data = row['Eternity Output LPD']
                for lang_dic in lpd_list:
                    if "en_US" in lang_dic:
                        pd_list = list(set(lang_dic["en_US"]))
                        #pd_cxt_dic["lpd_iop"] = pd_list[0]
                        #pd_list = [x for x in pd_list if len(x) > 50]
                        prod_desc = ''
                        if len(pd_list) > 0:
                            for pd in pd_list:
                                #if len(pd) > 50:
                                prod_desc = pd
                                for ky,val in invalid_dic.items():
                                    if ky in prod_desc:
                                        prod_desc = prod_desc.replace(ky,val)
                                if len(prod_desc) > 50 and row['CAPE_LPD_AVAIL'] == 'Y':
                                    desc_list.append(prod_desc)
                                    pd_asin_list.append(row['ASIN'])
                                    break
                            if row['CAPE_LPD_AVAIL'] == 'N':
                                #if prod_desc != '':
                                desc_list.append(prod_desc)
                                pd_asin_list.append(row['ASIN'])
                            #break
                            #else:
                                #for ky,val in invalid_dic.keys():




                        #desc_list.append(pd_list[0])
                        #is_lpd = True
                        #break
                    #else:
                        #break

            #if is_lpd == False:
                #desc_list.append("")
        #else:
            #desc_list.append("")




print(len(bp_asin_list))
print(len(bullet_list))

#print(len(bul_1))
#print(len(bul_2))
#print(len(bul_3))

#df3 = pd.DataFrame({"ASIN":bp_asin_list,"bp":bullet_list,"bullet_1":bul_1,"bullet_2":bul_2,"bullet_3":bul_3})
df3 = pd.DataFrame({"ASIN":bp_asin_list,"bp":bullet_list})
df4 = pd.DataFrame({"ASIN":pd_asin_list,"pd":desc_list})
df3 = df3.append(df4,ignore_index=True)
df3.to_excel(r'C://Users//louijose//Desktop//LPD_BP//result.xlsx',index=False)


#print(bullet_list)

        #cxt_str = str(bp_cxt_dic)
        #bp_context_list.append(cxt_str)

# df3 = pd.DataFrame({"asin":bp_asin_list})
# df3["use_case"] = "FILE_UPLOAD_PASIN"
# df3["error_code"] = "bulletCorrectionDefect"
# df3["priority"] = "manual_upload"
# df3["type"] = "asinType"
# df3["marketplace_id"] = 771770
# df3["product_group_code"] = bp_gl_list
# df3["product_line"] = "default"
# df3["attribute_name"] = "bullet"
# df3["pasindefectType"] = "<a___>"
# df3["contextdata"] = bp_context_list
# #df3["bullet_points"] = bullet_list
#
# df4 = pd.DataFrame({"asin":pd_asin_list})
# df4["use_case"] = "FILE_UPLOAD_PASIN"
# df4["error_code"] = "lpdCorrectionDefect"
# df4["priority"] = "manual_upload"
# df4["type"] = "asinType"
# df4["marketplace_id"] = 771770
# df4["product_group_code"] = pd_gl_list
# df4["product_line"] = "default"
# df4["attribute_name"] = "lpd"
# df4["pasindefectType"] = "<a___>"
# df4["contextdata"] = pd_context_list
# df3 = df3._append(df4,ignore_index=False)
#
# bull_1 = []
# bull_2 = []
# bull_3 = []
# bull_4 = []
# lpd_val = []
#
# for ind,row in df3.iterrows():
#     conv_dic = eval(row['contextdata'])
#     if row["error_code"] == 'bulletCorrectionDefect':
#         if conv_dic['bp_iop'] != '':
#             val_bps = conv_dic['bp_iop'].split("\n")
#             try:
#                 bull_1.append(val_bps[0])
#             except:
#                 bull_1.append('')
#             try:
#                 bull_2.append(val_bps[1])
#             except:
#                 bull_2.append('')
#             try:
#                 bull_3.append(val_bps[2])
#             except:
#                 bull_3.append('')
#             try:
#                 bull_4.append(val_bps[3])
#             except:
#                 bull_4.append('')
#         else:
#             bull_1.append('')
#             bull_2.append('')
#             bull_3.append('')
#             bull_4.append('')
#         lpd_val.append('')
#     else:
#         if conv_dic['lpd_iop'] != '':
#             lpd_val.append(conv_dic['lpd_iop'])
#         else:
#             lpd_val.append('')
#
#         bull_1.append('')
#         bull_2.append('')
#         bull_3.append('')
#         bull_4.append('')
# df3["bp_1_validation"] = bull_1
# df3["bp_2_validation"] = bull_2
# df3["bp_3_validation"] = bull_3
# df3["bp_4_validation"] = bull_4
# df3["product_description"] = lpd_val



#df3.to_excel(r'C://Users//louijose//Desktop//LPD_BP//result-iop-mx.xlsx',index=False)




