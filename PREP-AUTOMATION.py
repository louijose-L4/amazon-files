from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
import json
from tkinter import *
from tkinter import filedialog
import warnings
import re
import datetime
import logging
#import shutup
#warnings.filterwarnings("ignore")

amz_fragile_no = ["Asin Stickering", "Bagging", "Set Creation","Sold as set stickering"]
amz_fragile_yes = ["Asin Stickering", "Bubble wrap/Bubble bag", "Set Creation","Sold as set stickering"]
prep_frg_no = {"Asin Stickering":"asinstk","Bagging":"bagging","Set Creation":"setcreat","Sold as set stickering":"setstk"}
prep_frg_yes = {"Asin Stickering":"asinstk","Bubble wrap/Bubble bag":"bubble","Set Creation":"setcreat","Sold as set stickering":"setstk"}



#df = pd.read_excel(r'C://Users//louijose//Desktop//RBS_Defect_Reduction//Prep_Automation_3.xlsx')

def gui_app():
    global fileNam
    fileNam = filedialog.askopenfilename()
    #root = Tk()
    #root.title("Prep Application")

    # def click():
    #     global fileNam
    #     fileNam = filedialog.askopenfilename()
    #     root.destroy()
    #
    # wid = root.winfo_screenwidth()/2
    # heig = root.winfo_screenheight()/2
    # x_cor = wid-125
    # y_cor = heig-36
    # root.geometry("%dx%d+%d+%d"%(250,100,x_cor,y_cor))
    # frame_name = Frame(root,bg="#ADD8E6")
    # label_1 = Label(frame_name,text = "Please choose a file path",width = "20",height="1",bg="#D3D3D3",font="Times 16")
    # button_1= Button(frame_name,text = "Click",bg="#D3D3D3",font="Times 14",width = "4",height ="1",command=click)
    # label_1.grid(row=1,column=1)
    # button_1.grid(row=3,column=1)
    # frame_name.grid(row=1,column=1)
    # root.mainloop()







def prep_update(bot,reason):
    select = Select(bot.find_element(By.ID, 'context'))
    select.select_by_visible_text("Other")
    time.sleep(1)
    if reason == 'no_prep':
        bot.find_element(By.XPATH,"//input[@id='comment']").send_keys('Based on the IBQ logic, since the ASIN IBQ value in the catalog is set to 1, prep instructions are removed and marked as "No Prep"')
    elif reason == 'fragile_n':
        bot.find_element(By.XPATH, "//input[@id='comment']").send_keys('Based on the IBQ logic, since the ASIN is not fragile and the IBQ value in the catalog is set greater than 1, prep instructions are updated according to Set Creation/Hard Bundle requirements')
    elif reason == 'fragile_y':
        bot.find_element(By.XPATH, "//input[@id='comment']").send_keys('Based on the IBQ logic, since the ASIN is fragile and the IBQ value in the catalog is set greater than 1, prep instructions are updated according to Set Creation/Hard Bundle requirements')

    bot.find_element(By.XPATH,"//input[@value='Save']").click()
    return bot

def no_prep(bot):
    bot.find_element(By.ID, "edit-instructions-link").click()
    time.sleep(2)
    bot.find_element(By.XPATH, "//input[@value='no_prep']").click()
    time.sleep(2)
    return bot

def prep_instructions_check(prep_check_list,frg_check_list):
    if len(prep_check_list) == len(frg_check_list):
        for item in frg_check_list:
            if item in prep_check_list:
                prep_check_list.remove(item)
        return len(prep_check_list)
    return 1

def main_app():
    marketplace = []
    asin_list = []
    ibq_list = []
    vendor_list = []
    pg_rollup = []
    #lifecycle = []
    item_name = []
    size_name = []
    channel_list = []
    org_prep_list = []
    up_prep_list = []
    org_state_list = []
    up_state_list = []
    fragile_list = []

    dir_path = os.path.dirname(fileNam)
    df = pd.read_excel(fileNam)

    logging.getLogger("selenium").setLevel(logging.CRITICAL)
    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument(
        r"--user-data-dir=C://Users//" + os.environ["USERNAME"] + "//AppData//Local//Google//Chrome//User Data")
    chrome_options.add_argument("--log-level=OFF")
    # chrome_options.add_experimental_option("detach", True)
    service = Service(
        executable_path=r'C://Users//' + os.environ["USERNAME"] + '//Desktop//chromedriver-win64//chromedriver.exe')
    bot = webdriver.Chrome(service=service, options=chrome_options)

    bot.maximize_window()

    try:
        time_cap = datetime.datetime.now().microsecond
        for ind,row in df.iterrows():
            asin = row['asin']
            print(asin)
            ibq = row['ibq']
            vendor = row['distributor_id']
            is_fragile = row['is_fragile']
            marketplace.append(row['marketplace_id'])
            asin_list.append(asin)
            ibq_list.append(ibq)
            vendor_list.append(vendor)
            pg_rollup.append(row['pg_rollup'])
            #lifecycle.append(row['lifecycle_categories'])
            channel_list.append(row['channel'])
            item_name.append(row['item_name'])
            size_name.append(row['size_name'])
            fragile_list.append(is_fragile)

            prep_instructions = []
            to_update = []

            asin_url = f"https://prepmanager-iad.amazon.com/view/{asin}?region=NA"
            vendor_url = f"https://prepmanager-iad.amazon.com/vendor/{vendor}/{asin}/?region=NA"

            if ibq == 0 or pd.isna(ibq):
                up_state_list.append("VENDOR QUERY")
                org_prep_list.append('')
                up_prep_list.append('')
                org_state_list.append('')
                continue

            bot.get(url=asin_url)
            time.sleep(5)
            while re.search("midway", bot.current_url):
                time.sleep(5)

            try:
                cert_status = bot.find_element(By.XPATH,"//div[@id='instructions']//span[@class='certified-level']").text
            except:
                cert_status = "NOT AVAILABLE"


            if str(cert_status).lower() == "locked":
                up_state_list.append("LOCKED")
                org_prep_list.append('')
                up_prep_list.append('')
                org_state_list.append('')

                continue

            try:
                eles = bot.find_elements(By.XPATH, "//div[@id='instructions']//p")
                prep_instructions.append(eles[2].text)
            except:
                eles = bot.find_elements(By.XPATH,"//div[@id='instructions']//ul")
                for ele in eles:
                    prep_instructions = str(ele.text).split("\n")

            org_prep_list.append(','.join(prep_instructions))
            #print(prep_instructions)
            if ibq == 1:
                if len(prep_instructions) == 1:
                    if "no" in str(prep_instructions[0]).lower(): #and "prep" in str(prep_instructions[0]).lower():
                        up_prep_list.append("NIL")
                    else:
                        bot = no_prep(bot)
                        '''Reason for Prep Instructions to be updated '''
                        bot = prep_update(bot,"no_prep")
                        up_prep_list.append('Certified_No_Prep')
                else:
                    no_prep(bot)
                    prep_update(bot,"no_prep")
                    up_prep_list.append('Certified_No_Prep')

            elif ibq > 1 and is_fragile == "N":
                require_update = prep_instructions_check(prep_instructions, amz_fragile_no)
                if require_update > 0:
                    '''If the prep instructions for No fragile list does not match with already existing in PIM tool'''
                    no_prep(bot)
                    hidden_list = []
                    temp_list = []

                    for itn in amz_fragile_no:
                        try:
                            bot.find_element(By.XPATH, "//input[@value='" + amz_fragile_no[itn] + "']").click()
                            time.sleep(1)
                            temp_list.append(itn)
                        except:
                            hidden_list.append(itn)

                    #print(hidden_list)
                    if len(hidden_list) > 0:
                        bot.find_element(By.ID, "show-all").click()
                        time.sleep(2)
                        for itn in hidden_list:
                            bot.find_element(By.XPATH, "//input[@value='" + amz_fragile_no[itn] + "']").click()
                            time.sleep(1)
                            temp_list.append(itn)
                            #print(itn)
                    '''Reason for Prep Instructions to be updated '''
                    prep_update(bot,"fragile_n")
                    perf_prep_st = ','.join(temp_list)
                    up_prep_list.append(perf_prep_st)

                else:
                    up_prep_list.append("NIL")


            elif ibq > 1 and is_fragile == "Y":
                #print(prep_instructions)
                #print(amz_fragile_yes)
                require_update = prep_instructions_check(prep_instructions, amz_fragile_yes)
                if require_update > 0:
                    '''If the prep instructions for Yes fragile list does not match with already existing in PIM tool'''
                    bot = no_prep(bot)
                    hidden_list = []
                    temp_list = []

                    for itn in amz_fragile_yes:
                        # print(prep_dic[itn])
                        try:
                            bot.find_element(By.XPATH, "//input[@value='" + prep_frg_yes[itn] + "']").click()
                            time.sleep(1)
                            temp_list.append(itn)
                        except:
                            hidden_list.append(itn)

                    #print(hidden_list)
                    if len(hidden_list) > 0:
                        bot.find_element(By.ID, "show-all").click()
                        time.sleep(2)
                        for itn in hidden_list:
                            bot.find_element(By.XPATH, "//input[@value='" + prep_frg_yes[itn] + "']").click()
                            time.sleep(1)
                            temp_list.append(itn)
                            #print(itn)

                    '''Reason for Prep Instructions to be updated '''
                    bot = prep_update(bot,"fragile_y")
                    perf_prep_st = ','.join(temp_list)
                    up_prep_list.append(perf_prep_st)
                else:
                    up_prep_list.append('NIL')
            time.sleep(5)

            #print("Vendor_url",vendor_url)
            #print(bot.current_url)
            bot.get(url=vendor_url)
            #print(bot.current_url)
            time.sleep(2)
            try:
                eles = bot.find_elements(By.XPATH,"//h3//parent::div//b")
                state = eles[2].text
                org_state_list.append(state)
            except:
                state = "NA"
            #print("State",state)

            if state == "NA":
                up_state_list.append("UNKNOWN")
            elif (state != "NA" and state != "VENDOR_PERFORMED") and ibq == 1:
                #print("Joseph 1")
                select = Select(bot.find_element(By.ID,'vendor-state-select'))
                select.select_by_visible_text("VENDOR_PERFORMED")
                bot.find_element(By.XPATH,"//input[@value='Update']").click()
                up_state_list.append("VENDOR_PERFORMED")
                time.sleep(2)
            elif (state != "NA" and state != "AMAZON_PERFORMED") and ibq > 1:
                #print("Joseph 2")
                select = Select(bot.find_element(By.ID, 'vendor-state-select'))
                select.select_by_visible_text("AMAZON_PERFORMED")
                bot.find_element(By.XPATH, "//input[@value='Update']").click()
                up_state_list.append("AMAZON_PERFORMED")
                time.sleep(2)
            else:
                up_state_list.append("NIL")


        # print(len(asin_list))
        # print(len(marketplace))
        # print(len(ibq_list))
        # print(len(vendor_list))
        # print(len(pg_rollup))
        # #print(len(lifecycle))
        # print(len(item_name))
        # print(len(size_name))
        # print(len(channel_list))
        # print(len(org_prep_list))
        # print(len(up_prep_list))
        # print(len(org_state_list))
        # print(len(up_state_list))
        # print(org_prep_list)
        # print(up_prep_list)

        df_output = pd.DataFrame({"asin":asin_list,"marketplace":marketplace,"ibq":ibq_list,"vendor":vendor_list,"product_group":pg_rollup,
                                  "is_fragile":fragile_list,"item_name":item_name,"size":size_name,"channel":channel_list,"Orig_Prep":org_prep_list,"Updated_Prep":up_prep_list,
                                  "Org_State":org_state_list,"Updated_State":up_state_list})
        df_output.to_excel(dir_path + '//PREP-Output-' + str(time_cap) + '.xlsx',index=False)

    except Exception as err:
        print(err)
        json_output = {"asin":asin_list,"marketplace":marketplace,"ibq":ibq_list,"vendor":vendor_list,"product_group":pg_rollup,
                                  "item_name":item_name,"size":size_name,"channel":channel_list,"Orig_Prep":org_prep_list,"Updated_Prep":up_prep_list,
                                  "Org_State":org_state_list,"Updated_State":up_state_list}
        with open(dir_path + "//PREP-Output-Error" + str(time_cap) + ".json", "w") as outfile:
            json.dump(json_output, outfile, indent=4, sort_keys=False)

if __name__ == '__main__':
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
    gui_app()
    main_app()
    print("Completed!!!")


# import pandas as pd
# import requests
# from requests_kerberos import HTTPKerberosAuth, OPTIONAL
# import os
# import shutil
# import time
# import json
# from datetime import datetime, timedelta
# import browser_cookie3
#
# # cookie = browser_cookie3.firefox()
#
# def get_mwinit_cookie():
#
#     username = os.getlogin()
#     soruce="C:\\Users\\"+username+"\\.midway\\cookie"
#     destination ="C:\\Users\\"+username+"\\.midway\\cookie1"
#     if os.path.exists(destination):
#         os.remove(destination)
#     shutil.copy(soruce, destination)
#
#     username = username.replace("\n", "")
#     MidwayConfigDir = os.path.join(os.path.expanduser("~"), ".midway")
#     MidwayCookieJarFile = os.path.join(MidwayConfigDir, "cookie1")
#     fields = []
#     keyfile = open(MidwayCookieJarFile, "r")
#     for line in keyfile:
#         # parse the record into fields (separated by whitespace)
#         fields = line.split()
#         if len(fields) != 0:
#             # get the yubi session token and expire time
#             if fields[0] == "#HttpOnly_midway-auth.amazon.com":
#                 session_token = fields[6].replace("\n", "")
#                 expires = fields[4]
#
#             # get the user who generated the session token
#             elif fields[0] == "midway-auth.amazon.com":
#                 username = fields[6].replace("\n", "")
#     keyfile.close()
#     # make sure the session token hasn't expired
#     if time.gmtime() > time.gmtime(int(expires)):
#         raise SystemError("Your Midway token has expired. Run mwinit to renew")
#     # construct the cookie value required by calls to k2
#     cookie = {"username": username, "session": session_token}
#     return cookie
#
# cookie = get_mwinit_cookie()
#
#
# kerberos_auth = HTTPKerberosAuth(mutual_authentication=OPTIONAL)
#
# headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
#             ,'accept': 'application/json'
#             }
#
#
# PIM_URL_WITH_VENDOR = f"https://prepmanager-iad.amazon.com/vendor/INXHM/B0CHJXT31G?region=NA"
# PIM_URL = f'https://prepmanager-iad.amazon.com/view/B0CHJXT31G?region=NA'
#
#
# r = requests.get(PIM_URL_WITH_VENDOR, headers=headers, auth=kerberos_auth, verify=False,
#                                           cookies=cookie)
#
# print(r.status_code)
# print(r.content.decode())