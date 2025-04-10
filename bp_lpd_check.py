import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
service = Service(
    executable_path=r'C://Users//' + os.environ["USERNAME"] + '//Desktop//chromedriver-win64//chromedriver.exe')
bot = webdriver.Chrome(service=service, options=chrome_options)
df = pd.read_excel(r'C:\Users\louijose\Desktop\LPD_BP\BP_Check.xlsx')
bp_list = []
for index, pack in enumerate(zip(df['ASIN'],df['bullet_point_count'])):
    asin= pack[0]
    bp_len = pack[1]
    try:
        url = 'https://www.amazon.com/dp/' + str(asin) + '?th=1'
        bot.get(url)
        time.sleep(5)
        eles = bot.find_elements(By.XPATH,"//div[@id='feature-bullets']//li")
        bp_list.append(len(eles))
        if index % 10 == 0:
            print(asin,"shelock bp:",bp_len,"dp bp:",len(eles))
    except:
        bp_list.append("not avail")
df['dp_bp_length'] = bp_list
df.to_excel(r'C:\Users\louijose\Desktop\LPD_BP\dp_bp_result.xlsx',index=False)

