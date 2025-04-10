from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
from bs4 import BeautifulSoup
import requests
import urllib.request
import pandas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from PIL import Image
import time
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import *
#from selenium.webdriver.common.by import By
import os
import datetime
import logging
from dateutil.relativedelta import relativedelta
import re

#def ContentWar():
    #wait = WebDriverWait(bot,5,poll_frequency=1,ignored_exceptions=NoSuchElementException)
    #conWar = wait.until(EC.presence_of_element_located(By.XPath("//div[@style='padding: 0px 1rem 1rem;']//a")))
    #conWar.click()
    #WebDriverWait(bot,5).until(EC.alert_is_present())
    #alert = bot.switch_to.alert
    #alert.dismiss()

def module12(ASIN,l):
    try:
        mod12 = bot.find_element_by_xpath("//span[text()='Add Module']")
        location = mod12.location["y"]-100
        bot.execute_script("window.scrollTo(0,%d);" %location)
        mod12.click()
        time.sleep(2)
        bot.find_element_by_xpath("//h4[text()='Standard Image & Light Text Overlay']").click()
        time.sleep(2)
        image = modinfo.find('img').get("data-src")
        kw = modinfo.find('img').get("alt")
        if not kw:
            kw = " "
        try:
            head3 =  modinfo.find('h3').text.strip()
            bot.find_element_by_xpath("//div[@data-module-id='module-12'][" + str(l) + "]//div[@data-component-id='title']//input").send_keys(head3)
        except:
            pass
        try:
            paras = modinfo.find_all('p')
            for para in paras:
                ptext = para.text
                bot.find_element_by_xpath("//div[@data-module-id='module-12'][" + str(l) + "]//div[@data-component-id='description']//div[starts-with(@aria-describedby,'placeholder')]").send_keys(ptext)
        except:
             pass
        urllib.request.urlretrieve(image,imagePath + '/Module12-image' + str(l) +'.jpg')
        nimg = Image.open(imagePath + '/Module12-image' + str(l) +'.jpg')
        nimg = nimg.resize((970,300))
        nimg.save(imagePath + '/Module12-image' + str(l) +'.jpg')
        model12= bot.find_element_by_xpath("//div[@data-module-id='module-12'][" + str(l) + "]//span[contains(text(),'+ Add background image')]//parent::span//parent::button")
        location = model12.location["y"]-100
        bot.execute_script("window.scrollTo(0,%d);" %location)
        model12.click()
        bot.find_element_by_xpath("//input[@type='file']").send_keys(imagePath + '/Module12-image' + str(l) + '.jpg')
        bot.find_element_by_xpath("//input[@placeholder='Enter image keywords']").send_keys(kw)
        bot.find_element_by_xpath("//span[(text()='Add')]//parent::span//parent::button").click()
        #try:
            #bot.find_element_by_xpath("//p[contains(text(),'This content fails to pass validation')]")
            #bot.find_element_by_xpath("//div[@style='padding: 0px 1rem 1rem;']//a").click()
        #except:
            #pass
        #ContentWar()

    except:
        logging.info("ASIN: " + ASIN + "Error in Module 12")
        pass
def module11(ASIN,k):
    try:
         mod11 = bot.find_element_by_xpath("//span[text()='Add Module']")
         location = mod11.location["y"]-100
         bot.execute_script("window.scrollTo(0,%d);" %location)
         mod11.click()
         time.sleep(2)
         modin11 = bot.find_element_by_xpath("//h4[text()='Standard Image & Dark Text Overlay']")
         location = modin11.location["y"]-100
         bot.execute_script("window.scrollTo(0,%d);" %location)
         modin11.click()
         try:
             head3 = modinfo.find('h3').text
             bot.find_element_by_xpath("//div[@data-module-id='module-11'][" + str(k) + "]//div[@data-component-id='title']//input").send_keys(head3)
         except:
             pass
         img = modinfo.find('img').get('data-src')
         kw = modinfo.find('img').get('alt')
         if not kw:
             kw = " "
         urllib.request.urlretrieve(img,imagePath + '/Module11-image' + str(k) + '.jpg')
         nimg = Image.open(imagePath + '/Module11-image' + str(k) + '.jpg')
         nimg = nimg.resize((970,300))
         nimg.save(imagePath + '/Module11-image' + str(k) + '.jpg')
         model11= bot.find_element_by_xpath("//div[@data-module-id='module-11'][" + str(k) + "]//span[contains(text(),'+ Add background image')]//parent::span//parent::button")
         location = model11.location["y"]-100
         bot.execute_script("window.scrollTo(0,%d);" %location)
         model11.click()
         bot.find_element_by_xpath("//input[@type='file']").send_keys(imagePath + '/Module11-image' + str(k) + '.jpg')
         bot.find_element_by_xpath("//input[@placeholder='Enter image keywords']").send_keys(kw)
         bot.find_element_by_xpath("//span[(text()='Add')]//parent::span//parent::button").click()
         for para in modinfo.find_all('p'):
            ptext = para.text
            bot.find_element_by_xpath("//div[@data-module-id='module-11'][" + str(k) + "]//div[@data-component-id='description']//div[starts-with(@aria-describedby,'placeholder')]").send_keys(ptext)
         #ContentWar()
    except:
        logging.info("ASIN: " + ASIN + "Error in Module 11")
        pass

def module10(ASIN,j):
    try:
         n=1
         mod10 = bot.find_element_by_xpath("//span[text()='Add Module']")
         time.sleep(2)
         location = mod10.location["y"]-100
         bot.execute_script("window.scrollTo(0,%d);" %location)
         mod10.click()
         time.sleep(2)
         bot.find_element_by_xpath("//h4[text()='Standard Four Image/Text Quadrant']").click()
         time.sleep(2)
         images = modinfo.find_all('img')
         try:
             for img, n in zip(images,range(1,5)):
                image = img.get('data-src')
                imageky = img.get('alt')
                if not imageky:
                    imageky = " "
                urllib.request.urlretrieve(image,imagePath + '/Module10-image-' + str(j) + str(n) + '.jpg')
                nimg = Image.open(imagePath + '/Module10-image-' + str(j) + str(n) + '.jpg')
                nimg = nimg.resize((135,135))
                nimg.save(imagePath + '/Module10-image-' + str(j) + str(n) + '.jpg')
                bot.find_element_by_xpath("//div[@data-module-id='module-10'][" + str(j) + "]//div[@data-component-id='block" + str(n) + "-image']//a[@role='button']").click()
                bot.find_element_by_xpath("//input[@type='file']").send_keys(imagePath + '/Module10-image-' + str(j) + str(n) + '.jpg')
                bot.find_element_by_xpath("//input[@placeholder='Enter image keywords']").send_keys(imageky)
                bot.find_element_by_xpath("//span[(text()='Add')]//parent::span//parent::button").click()
         except:
             pass
         try:
                header3 = modinfo.find_all('h3')
                for head3s,n in zip(header3,range(1,5)):
                    head3 = head3s.text
                    bot.find_element_by_xpath("//div[@data-module-id='module-10'][" + str(j) + "]//div[@data-component-id='block" + str(n) + "-header']//input").send_keys(head3)
         except:
            pass
         try:
                paras = modinfo.find_all('p')
                for para,n in zip(paras,range(1,5)):
                    ptext = para.text
                    bot.find_element_by_xpath("//div[@data-module-id='module-10'][" + str(j) + "]//div[@data-component-id='block" + str(n) + "-description']//div[starts-with(@aria-describedby,'placeholder')]").send_keys(ptext)
         except:
            pass
         #ContentWar()
    except:
        logging.info("ASIN: " + ASIN + "Error in Module 10")
        pass
def module9(ASIN,i):
    try:
         mod9 = bot.find_element_by_xpath("//span[text()='Add Module']")
         time.sleep(2)
         location = mod9.location["y"]-100
         bot.execute_script("window.scrollTo(0,%d);" %location)
         mod9.click()
         time.sleep(2)
         bot.find_element_by_xpath("//h4[text()='Standard Three Images & Text']").click()
         time.sleep(2)
         try:
            header3 = modinfo.find("h3").get_text().strip()
            bot.find_element_by_xpath("//div[@data-module-id='module-9'][" + str(i) + "]//div[@data-component-id='header']//input").send_keys(header3)
         except:
            pass
         try:
             for img_grp,n in zip(modinfo.find_all('img'),range(1,4)):
                 imagelink=img_grp.get('data-src')
                 imageky = img_grp.get('alt')
                 if not imageky:
                     imageky = " "
                 urllib.request.urlretrieve(imagelink,imagePath +  '/Module9-image-' + str(i) + str(n) + '.jpg')
                 nimg = Image.open(imagePath + '/Module9-image-' + str(i) + str(n) + '.jpg')
                 nimg = nimg.resize((300,300))
                 nimg.save(imagePath + '/Module9-image-' + str(i)+ str(n) + '.jpg')
                 bot.find_element_by_xpath("//div[@data-module-id='module-9'][" + str(i) + "]//div[@data-component-id='section" + str(n) +"-image']//a[@role='button']").click()
                 bot.find_element_by_xpath("//input[@type='file']").send_keys(imagePath + '/Module9-image-' + str(i) + str(n) + '.jpg')
                 bot.find_element_by_xpath("//input[@placeholder='Enter image keywords']").send_keys(imageky)
                 bot.find_element_by_xpath("//span[(text()='Add')]//parent::span//parent::button").click()
         except:
            pass
         try:
            for head4_grp,n in zip(modinfo.find_all('h4',class_='a-spacing-mini'),range(1,4)):
                header4 = head4_grp.get_text().strip()
                bot.find_element_by_xpath("//div[@data-module-id='module-9'][" + str(i) + "]//div[@data-component-id='section" + str(n) + "-header']//input").send_keys(header4)
         except:
            pass
         try:
             for paras,n in zip(modinfo.find_all('td',class_='apm-top'),range(1,4)):
                for para in paras.find_all('p'):
                    ptext = para.text.strip()
                    bot.find_element_by_xpath("//div[@data-module-id='module-9'][" + str(i) + "]//div[@data-component-id='description" + str(n) + "']//div[starts-with(@aria-describedby,'placeholder')]").send_keys(ptext)
         except:
             pass
         #ContentWar()
    except:
        logging.info("ASIN: " + ASIN + "Error in Module 9")
        pass
def module8(ASIN,h):
    try:
         mod8 = bot.find_element_by_xpath("//span[text()='Add Module']")
         n=1
         location = mod8.location["y"]-100
         bot.execute_script("window.scrollTo(0,%d);" %location)
         mod8.click()
         time.sleep(2)
         bot.find_element_by_xpath("//h4[text()='Standard Single Image & Highlights']").click()
         time.sleep(2)
         imager = modinfo.find('div',class_="apm-leftimage")
         imageLink = imager.img.get('data-src')
         kw = imager.img.get('alt')
         if not kw:
             kw = " "
         urllib.request.urlretrieve(imageLink,imagePath + '/Module8-image-' + str(h) + '1.jpg')
         nimg = Image.open(imagePath + '/Module8-image-' +str(h) + '1.jpg')
         nimg = nimg.resize((300,300))
         nimg.save(imagePath + '/Module8-image-' + str(h) + '1.jpg')
         bot.find_element_by_xpath("//div[@data-component-id='main-image']//a[@role='button']").click()
         bot.find_element_by_xpath("//input[@type='file']").send_keys(imagePath + '/Module8-image-' + str(h) + '1.jpg')
         bot.find_element_by_xpath("//input[@placeholder='Enter image keywords']").send_keys(kw)
         bot.find_element_by_xpath("//span[(text()='Add')]//parent::span//parent::button").click()
         try:
             head3 = modinfo.find('h3').get_text().strip()
             bot.find_element_by_xpath("//div[@data-module-id='module-8'][" + str(h) + "]//div[@data-component-id='header']//input").send_keys(head3)
         except:
             pass
         paras = modinfo.find('div',class_='apm-centerthirdcol').find_all("p")
         for para,n in zip(paras,range(1,4)):
              try:
                 header5 = para.find_previous_sibling('h5')
                 head5 = header5.text
                 bot.find_element_by_xpath("//div[@data-module-id='module-8'][" + str(h) + "]//div[@data-component-id='description-subheader" + str(n) + "']//input").send_keys(head5)
              except:
                 pass
              ptext = para.text
              bot.find_element_by_xpath("//div[@data-module-id='module-8'][" + str(h) + "]//div[@data-component-id='description" + str(n) + "']//div[starts-with(@aria-describedby,'placeholder')]").send_keys(ptext)

         info4= modinfo.find('div',class_='apm-rightthirdcol')
         try:
             bot.find_element_by_xpath ("//div[@data-module-id='module-8']//div[@data-component-id='techspecs-header']//input").send_keys(info4.h4.text.strip('\n').strip())
         except:
             pass
         try:
             ulist = info4.find('ul',class_='a-unordered-list').find_all('li')
             n=0
             for lis in range(len(ulist)):
                  bullets = bot.find_elements_by_xpath("//div[@data-module-id='module-8']//input[@placeholder='Enter bullet point text']")
                  bullets[n].send_keys(ulist[lis].text.strip('\n').strip())
                  if lis==len(ulist)-1:
                      break
                  butt = bot.find_element_by_xpath("//div[@data-module-id='module-8'][" + str(h) + "]//span[text()='+ Add bullet point']//parent::span//parent::button")
                  location = butt.location["y"]-100
                  bot.execute_script("window.scrollTo(0,%d);" %location)
                  butt.click()
                  n+=1
         except:
            pass
         #ContentWar()
    except:
        logging.info("ASIN: " + ASIN + "Error in Module 8")
        pass
def module7(ASIN,g):
    try:
        n=0
        mod7 = bot.find_element_by_xpath("//span[text()='Add Module']")
        location = mod7.location["y"]-100
        bot.execute_script("window.scrollTo(0,%d);" %location)
        mod7.click()
        time.sleep(2)
        bot.find_element_by_xpath("//h4[text()='Standard Single Image & Specs Detail']").click()
        time.sleep(2)
        image = modinfo.find('img').get('data-src')
        kw = modinfo.find('img').get('alt')
        if not kw:
            kw = " "
        urllib.request.urlretrieve(image,imagePath + '/Module7-image-' + str(g) + '1.jpg')
        nimg = Image.open(imagePath + '/Module7-image-' +str(g) + '1.jpg')
        nimg = nimg.resize((300,300))
        nimg.save(imagePath + '/Module7-image-' + str(g) + '1.jpg')
        bot.find_element_by_xpath("//div[@data-module-id='module-7'][" + str(g) + "]//div[@data-component-id='main-image']//a[@role='button']").click()
        bot.find_element_by_xpath("//input[@type='file']").send_keys(imagePath + '/Module7-image-' +str(g) +'1.jpg')
        bot.find_element_by_xpath("//input[@placeholder='Enter image keywords']").send_keys(kw)
        bot.find_element_by_xpath("//span[(text()='Add')]//parent::span//parent::button").click()
        header4 = modinfo.find('div',class_='apm-centerthirdcol').h4.get_text()
        bot.find_element_by_xpath("//div[@data-module-id='module-7'][" + str(g) + "]//div[@data-component-id='description-header']//input").send_keys(header4)
        hd=1
        for head5 in modinfo.find('div',class_='apm-centerthirdcol').find_all('h5'):
             head5 = head5.get_text()
             bot.find_element_by_xpath("//div[@data-module-id='module-7'][" + str(g) + "]//div[@data-component-id='description-subheader" + str(hd) + "']//input").send_keys(head5)
             hd+=1
        pd = 1
        for  paras in modinfo.find('div',class_='apm-centerthirdcol').find_all('p'):
             ptext =  paras.get_text()
             bot.find_element_by_xpath("//div[@data-module-id='module-7'][" + str(g) + "]//div[@data-component-id='description" + str(pd) + "']//div[starts-with(@aria-describedby,'placeholder')]").send_keys(ptext)
             pd += 1
        head5 = modinfo.find('div',class_='apm-rightthirdcol-inner').find_all('h5')
        header5a = head5[0].get_text()
        bot.find_element_by_xpath("//div[@data-module-id='module-7'][" + str(g) + "]//div[@data-component-id='techspecs-list-subheader']//input").send_keys(header5a)
        bot.find_element_by_xpath("//div[@data-module-id='module-7'][" + str(g) + "]//div[@data-component-id='techspecs-list-subheader']//input").send_keys(header5a)
        ulist = modinfo.find('div',class_='apm-rightthirdcol-inner').find_all('li')
        for lis in range(len(ulist)):
             bullets = bot.find_elements_by_xpath("//div[@data-module-id='module-7'][" + str(g) + "]//input[@placeholder='Enter bullet point text']")
             bullets[n].send_keys(ulist[lis].text.strip('\n').strip())
             if lis==len(ulist)-1:
                 break
             butt = bot.find_element_by_xpath("//div[@data-module-id='module-7'][" + str(g) + "]//span[text()='+ Add bullet point']//parent::span//parent::button")
             location = butt.location["y"]-100
             bot.execute_script("window.scrollTo(0,%d);" %location)
             butt.click()
             n+=1
        header5b = head5[1].get_text()
        bot.find_element_by_xpath("//div[@data-module-id='module-7'][" + str(g) + "]//div[@data-component-id='techspecs-subheader1']//input").send_keys(header5b)
        paras = modinfo.find('div',class_='apm-rightthirdcol-inner').find_all('p')
        for para in paras:
           ptext = para.get_text()
           bot.find_element_by_xpath("//div[@data-component-id='techspecs-description1']//div[starts-with(@aria-describedby,'placeholder')]").send_keys(ptext)
        #ContentWar()
    except:
         logging.info("ASIN: " + ASIN + "Error in Module 7")
         pass

def module6(ASIN,f):
    try:
        n=1
        mod6 = bot.find_element_by_xpath("//span[text()='Add Module']")
        location = mod6.location["y"]-100
        bot.execute_script("window.scrollTo(0,%d);" %location)
        mod6.click()
        time.sleep(2)
        bot.find_element_by_xpath("//h4[text()='Multiple Image Module A']").click()
        time.sleep(2)
        for imgdes,intext in zip(modinfo.find_all('div',class_="apm-hovermodule-image"),modinfo.find_all('div',class_="apm-hovermodule-slides-inner")):
               image = imgdes.img.get('data-src')
               kw = imgdes.img.get('alt')
               if not kw:
                   kw = " "
               urllib.request.urlretrieve(image,imagePath + '/Module6-image-' + str(f) + str(n) + '.jpg')
               nimg = Image.open(imagePath + '/Module6-image-' + str(f) + str(n) + '.jpg')
               nimg = nimg.resize((300,400))
               nimg.save(imagePath + '/Module6-image-' + str(f) + str(n) + '.jpg')
               bot.find_element_by_xpath("//div[@data-module-id='module-6'][" + str(f) + "]//div[@data-component-id='image" + str(n) + "']//div[@role='button']").click()
               bot.find_element_by_xpath("//div[@data-module-id='module-6'][" + str(f) + "]//div[@data-component-id='image" + str(n) + "']//a[@role='button']").click()
               bot.find_element_by_xpath("//input[@type='file']").send_keys(imagePath + '/Module6-image-' + str(f) +str(n) + '.jpg')
               bot.find_element_by_xpath("//input[@placeholder='Enter image keywords']").send_keys(kw)
               bot.find_element_by_xpath("//span[(text()='Add')]//parent::span//parent::button").click()
               head3 = intext.h3.text.strip()
               time.sleep(2)
               bot.find_element_by_xpath("//div[@data-module-id='module-6'][" + str(f) + "]//div[@data-component-id='title" + str(n) + "']//input[@placeholder='Enter headline text']").send_keys(head3)
               para = intext.p.text
               time.sleep(2)
               parainfo = bot.find_element_by_xpath("//div[@data-module-id='module-6'][" + str(f) + "]//div[@data-component-id='description" + str(n) +"']//div[starts-with(@aria-describedby,'placeholder')]")
               parainfo.send_keys(para)
               n+=1
               time.sleep(2)
        #ContentWar()
    except:
        logging.info("ASIN: " + ASIN + "Error in Module 6")
        pass
def module5(ASIN,e):
    try:
        n=1
        mod5 = bot.find_element_by_xpath("//span[text()='Add Module']")
        time.sleep(2)
        location = mod5.location["y"]-100
        bot.execute_script("window.scrollTo(0,%d);" %location)
        mod5.click()
        time.sleep(2)
        bot.find_element_by_xpath("//h4[text()='Standard Comparison Chart']").click()
        time.sleep(2)
        info1= modinfo.find('table',class_='apm-tablemodule-table').find_all('th',class_='apm-tablemodule-image')
        info2= modinfo.find('table',class_='apm-tablemodule-table').find_all('tr',class_='apm-tablemodule-imagerows')[1].find_all('a')
        try:
            for r,q in zip(info1,info2):
                      image = r.img.get('data-src')
                      kw = r.img.get('alt')
                      if not kw:
                          kw = ' '
                      urllib.request.urlretrieve(image,imagePath + '/Module5-image-' + str(e) + str(n) + '.jpg')
                      nimg = Image.open(imagePath + '/Module5-image-' + str(e) + str(n) + '.jpg')
                      nimg = nimg.resize((150,300))
                      nimg.save(imagePath + '/Module5-image-' + str(e) + str(n) + '.jpg')
                      bot.find_element_by_xpath("//div[@data-module-id='module-5'][" + str(e) + "]//div[@data-component-key='image']//a[@role='button']").click()
                      bot.find_element_by_xpath("//input[@type='file']").send_keys(imagePath + '/Module5-image-' + str(e) + str(n) + '.jpg')
                      bot.find_element_by_xpath("//input[@placeholder='Enter image keywords']").send_keys(kw)
                      bot.find_element_by_xpath("//span[(text()='Add')]//parent::span//parent::button").click()
                      n+=1
                      time.sleep(5)
            lis1=[]
            lis2=[]
            n=1
            titleInfo = modinfo.find_all('tr',class_='apm-tablemodule-imagerows')
            keyval={}
            keycount=1
            for name in titleInfo[1].find_all('th'):
                try:
                    keyval[name.a.get('href').split("/")[2]]=name.a.text.strip()
                    keycount+=1
                except:
                    continue
            firvals= bot.find_elements_by_xpath("//div[@data-module-id='module-5'][" + str(e) + "]//input[@placeholder='Enter title']")
            seconvals = bot.find_elements_by_xpath("//div[@data-module-id='module-5'][" + str(e) + "]//input[@placeholder='Enter ASIN']")
            for key,val, title,ASIN in zip(keyval.keys(),keyval.values(),firvals,seconvals):
                    title.send_keys(val)
                    ASIN.send_keys(key)
        except:
              pass

        tablevalues = modinfo.find('table',class_='apm-tablemodule-table').find_all('tr',class_='apm-tablemodule-keyvalue')
        for sel,high in zip(tablevalues[0].find_all('td',class_='apm-tablemodule-valuecell'),bot.find_elements_by_xpath("//div[@data-module-id='module-5'][" + str(e) + "]//input[@type='checkbox']")):
            if "selected" in sel['class']:
                high.click()
        for count in range(1,len(keyval.keys())+1):
            lis1.append("Data " + str(count))
        df = pd.DataFrame(index = range(len(tablevalues)),columns=lis1)
        for i,tabval in zip(range(len(tablevalues)),tablevalues):
            for j,val in zip(lis1,tabval.find_all('td',class_='apm-tablemodule-valuecell')):
                df.loc[i,j]= val.span.text.strip()
        for rowheaders in tablevalues:
            for row in rowheaders.find_all('th',class_='apm-tablemodule-keyhead'):
                lis2.append(row.span.text.strip())
        df.insert(0,column='RowHead',value=lis2)
        xlocation = bot.find_element_by_xpath("//div[@data-module-id='module-5'][" + str(e) + "]//span[text()='Add metric']//parent::span//parent::button")
        bot.execute_script("arguments[0].scrollIntoView(true);", xlocation)
        for i in range(len(tablevalues)):
            abc = bot.find_element_by_xpath("//div[@data-module-id='module-5'][" + str(e) + "]//span[text()='Add metric']//parent::span//parent::button")
            location= abc.location["y"]-100
            bot.execute_script("window.scrollTo(0,%d);" %location)
            abc.click()
            time.sleep(2)
            n=0
            k=0
        for ele in bot.find_elements_by_xpath("//div[@data-module-id='module-5'][" + str(e) + "]//div[contains(@style,'0px 14px 18px 0px') and contains(@style,'width: 16.6667%')][1]//input[@placeholder='Enter metric']"):
                ele.send_keys(df.iloc[n,0])
                n+=1
        for k,l in zip(range(2,keycount+1),range(1,keycount+1)):
            eles = bot.find_elements_by_xpath("//div[@data-module-id='module-5'][" + str(e) + "]//div[contains(@style,'0px 14px 18px 0px') and contains(@style,'width: 16.6667%')][" + str(k) + "]//button")
            abcs = bot.find_elements_by_xpath("//div[@data-module-id='module-5'][" + str(e) + "]//div[contains(@style,'0px 14px 18px 0px') and contains(@style,'width: 16.6667%')][" + str(k) + "]//span//div[text()='✔']")
            defs = bot.find_elements_by_xpath("//div[@data-module-id='module-5'][" + str(e) + "]//div[contains(@style,'0px 14px 18px 0px') and contains(@style,'width: 16.6667%')][" + str(k) + "]//span//div[text()='Text']")
            xyzz = bot.find_elements_by_xpath("//div[@data-module-id='module-5'][" + str(e) + "]//div[contains(@style,'0px 14px 18px 0px') and contains(@style,'width: 16.6667%')][" + str(k) + "]//span//div[text()='(none)']")
            for p,ele,mat,des,ghi in zip(range(0,len(tablevalues)),eles,abcs,defs,xyzz):
                        ele.click()
                        if  df.iloc[p,l] == "✓":
                            location= mat.location["y"]-100
                            bot.execute_script("window.scrollTo(0,%d);" %location)
                            mat.click()
                        elif df.iloc[p,l]=="-":
                            location= ghi.location["y"]-100
                            bot.execute_script("window.scrollTo(0,%d);" %location)
                            ghi.click()
                        else:
                            location= des.location["y"]-100
                            bot.execute_script("window.scrollTo(0,%d);" %location)
                            des.click()
                            time.sleep(2)

        for num,col in zip(lis1,range(2,keycount+1)):
                df2 = df[num]
                mask1 = df2!="-"
                mask2 = df2!="✓"
                df2 = df2[mask1 & mask2]
                df2 = df2.reset_index(drop=True)
                z=0
                #print(df2)
                for ele in bot.find_elements_by_xpath("//div[@data-module-id='module-5'][" + str(e) + "]//div[contains(@style,'0px 14px 18px 0px') and contains(@style,'width: 16.6667%')][" + str(col) + "]//input"):
                    data = df2[z]
                    ele.send_keys(data)
                    z+=1
        #ContentWar()
    except:
        logging.info("ASIN: " + ASIN + "Error in Module 5")
        pass

def module4(ASIN,d):
    try:
        mod4 = bot.find_element_by_xpath("//span[text()='Add Module']")
        location = mod4.location["y"]-100
        bot.execute_script("window.scrollTo(0,%d);" %location)
        mod4.click()
        time.sleep(2)
        bot.find_element_by_xpath("//h4[text()='Standard Four Image & Text']").click()
        time.sleep(2)
        try:
             head3 = modinfo.find('h3',class_='a-spacing-small').text.strip()
             bot.find_element_by_xpath("//div[@data-module-id='module-4'][" + str(d) + "]//div[@data-component-id='module-title']//input").send_keys(head3)
        except:
            pass
        n = 1
        for img_grp in modinfo.find_all('img'):
                   image = img_grp.get('data-src')
                   kw = img_grp.get('alt')
                   if not kw:
                       kw = ' '
                   urllib.request.urlretrieve(image,imagePath + '/Module4-image-' + str(d) + str(n) + '.jpg')
                   nimg = Image.open(imagePath + '/Module4-image-' + str(d) + str(n) + '.jpg')
                   nimg = nimg.resize((220,220))
                   nimg.save(imagePath + '/Module4-image-' + str(d) + str(n) + '.jpg')
                   time.sleep(2)
                   bot.find_element_by_xpath("//div[@data-module-id='module-4'][" + str(d) + "]//div[@data-component-id='block" + str(n) + "-image']//a[@role='button']").click()
                   bot.find_element_by_xpath("//input[@type='file']").send_keys(imagePath + '/Module4-image-' + str(d) + str(n) + '.jpg')
                   bot.find_element_by_xpath("//input[@placeholder='Enter image keywords']").send_keys(kw)
                   bot.find_element_by_xpath("//span[(text()='Add')]//parent::span//parent::button").click()
                   n+=1

        n=1
        for head4_group in modinfo.find_all('h4',class_='a-spacing-mini'):
             bot.find_element_by_xpath("//div[@data-module-id='module-4'][" + str(d) + "]//div[@data-component-id='block" + str(n) + "-title']//input[@placeholder='Enter headline text']").send_keys(head4_group.text.strip("\n").strip())
             n+=1

        n=1
        desc = modinfo.find_all('td',class_='apm-top')
        for info in desc:
                 infor = info.div.p.text
                 bot.find_element_by_xpath("//div[@data-module-id='module-4'][" + str(d) + "]//div[@data-component-id='block" + str(n) + "-description']//div[starts-with(@aria-describedby,'placeholder')]").send_keys(infor)
                 n+=1
        #ContentWar()
    except:
         logging.info("ASIN: " + ASIN + "Error in Module 4")
         pass
def module3(ASIN,c):
    try:
        mod3 = bot.find_element_by_xpath("//span[text()='Add Module']")
        location = mod3.location["y"]-100
        bot.execute_script("window.scrollTo(0,%d);" %location)
        mod3.click()
        time.sleep(2)
        bot.find_element_by_xpath("//h4[text()='Standard Single Right Image']").click()
        time.sleep(2)
        bot.find_element_by_xpath("//div[@data-module-id='module-3'][" + str(c) +"]//div[@data-component-id='image']//a[@role='button']").click()
        image3 = modinfo.find('img').get('data-src')
        kw = modinfo.find('img').get('alt')
        if not kw:
            kw = " "
        urllib.request.urlretrieve(image3,imagePath + '/Module-3-image' + str(c) + '.jpg')
        nimg = Image.open(imagePath + '/Module-3-image' +str(c) + '.jpg')
        nimg = nimg.resize((300,300))
        nimg.save(imagePath + '/Module-3-image' +str(c) +'.jpg')
        bot.find_element_by_xpath("//input[@type='file']").send_keys(imagePath + '/Module-3-image' +str(c) + '.jpg')
        bot.find_element_by_xpath("//input[@placeholder='Enter image keywords']").send_keys(kw)
        bot.find_element_by_xpath("//span[(text()='Add')]//parent::span//parent::button").click()
        try:
           head3 = modinfo.find('h3').text.strip()
           header3 = bot.find_element_by_xpath("//div[@data-module-id='module-3'][" + str(c) +"]//input[@placeholder='Enter headline text']")
           header3.send_keys(head3)
        except:
           pass
        for para in modinfo.find_all('p'):
           desc = para.text
           bot.find_element_by_xpath("//div[@data-module-id='module-3'][" + str(c) +"]//div[starts-with(@aria-describedby,'placeholder')]").send_keys(desc)
        #ContentWar()
    except:
        logging.info("ASIN: " + ASIN + "Error in Module 3")
        pass
def module2(ASIN,b):
    try:
        mod2 = bot.find_element_by_xpath("//span[text()='Add Module']")
        location = mod2.location["y"]-100
        bot.execute_script("window.scrollTo(0,%d);" %location)
        mod2.click()
        time.sleep(2)
        mod2 = bot.find_element_by_xpath("//h4[text()='Standard Single Left Image']")
        location = mod2.location["y"]-100
        bot.execute_script("window.scrollTo(0,%d);" %location)
        mod2.click()
        time.sleep(2)
        bot.find_element_by_xpath("//div[@data-module-id='module-2'][" + str(b) + "]//div[@data-component-id='image']//a[@role='button']").click()
        image3 = modinfo.find('img').get('data-src')
        kw = modinfo.find('img').get('alt')
        if not kw:
            kw = ' '
        urllib.request.urlretrieve(image3,imagePath + '/Module2-image' + str(b) + '.jpg')
        nimg = Image.open(imagePath + '/Module2-image' + str(b) + '.jpg')
        nimg = nimg.resize((300,300))
        nimg.save(imagePath + '/Module2-image' +str(b) + '.jpg')
        bot.find_element_by_xpath("//input[@type='file']").send_keys(imagePath + '/Module2-image' +str(b) + '.jpg')
        bot.find_element_by_xpath("//input[@placeholder='Enter image keywords']").send_keys(kw)
        bot.find_element_by_xpath("//span[(text()='Add')]//parent::span//parent::button").click()
        try:
           head3 = modinfo.find('h3').text.strip()
           bot.find_element_by_xpath("//div[@data-module-id='module-2'][" + str(b) + "]//input[@placeholder='Enter headline text']").send_keys(head3)
        except:
           pass
        for para in modinfo.find_all('p'):
            ptext = para.text
            bot.find_element_by_xpath("//div[@data-module-id='module-2'][" + str(b) + "]//div[starts-with(@aria-describedby,'placeholder')]").send_keys(ptext)
        #ContentWar()
    except:
       logging.info("ASIN: " + ASIN + "Error in Module 2")
       pass

def module1(ASIN,a):
    try:
         mod1=bot.find_element_by_xpath("//span[text()='Add Module']")
         location = mod1.location["y"]-100
         bot.execute_script("window.scrollTo(0,%d);" %location)
         mod1.click()
         time.sleep(2)
         bot.find_element_by_xpath("//h4[text()='Standard Single Image & Sidebar']").click()
         time.sleep(2)
         lima = modinfo.find('div',class_='apm-leftimage').find('img').get('data-src')
         lkw = modinfo.find('div',class_='apm-leftimage').find('img').get('alt')
         if not lkw:
             lkw = " "
         urllib.request.urlretrieve(lima,imagePath + '/Module1-Left-image' + str(a) + '.jpg')
         nimg = Image.open(imagePath + '/Module1-Left-image' + str(a) + '.jpg')
         nimg = nimg.resize((300,400))
         nimg.save(imagePath + '/Module1-Left-image' + str(a) + '.jpg')
         bot.find_element_by_xpath("//div[@data-module-id='module-1'][" + str(a) +"]//div[@data-component-id='main-image']//a[@role='button']").click()
         bot.find_element_by_xpath("//input[@type='file']").send_keys(imagePath + '/Module1-Left-image' + str(a) + '.jpg')
         bot.find_element_by_xpath("//input[@placeholder='Enter image keywords']").send_keys(lkw)
         bot.find_element_by_xpath("//span[(text()='Add')]//parent::span//parent::button").click()
         rtext = modinfo.find('div',class_='apm-leftimage').find('p').text.strip('\n').strip()
         bot.find_element_by_xpath("//div[@data-component-id='main-image-caption']//input[@placeholder='Enter image caption text']").send_keys(rtext)
         rimg = modinfo.find('div',class_='apm-rightthirdcol-inner').find('img').get('src')
         rkw = modinfo.find('div',class_='apm-rightthirdcol-inner').find('img').get('alt')
         if not rkw:
             rkw = " "
         bot.find_element_by_xpath("//div[@data-component-id='about-image' ]//a[@role='button']").click()
         urllib.request.urlretrieve(rimg,imagePath + '/Module1-Right-image' + str(a) +'.jpg')
         nimg = Image.open(imagePath + '/Module1-Right-image' + str(a) + '.jpg')
         nimg = nimg.resize((350,175))
         nimg.save(imagePath + '/Module1-Right-image' + str(a) +'.jpg')
         bot.find_element_by_xpath("//input[@type='file']").send_keys(imagePath + '/Module1-Right-image' + str(a) + '.jpg')
         bot.find_element_by_xpath("//input[@placeholder='Enter image keywords']").send_keys(lkw)
         bot.find_element_by_xpath("//span[(text()='Add')]//parent::span//parent::button").click()
         try:
             head3= modinfo.find('div',class_='apm-centerthirdcol').h3.text.strip('\n').strip()
             bot.find_element_by_xpath("//div[@data-module-id='module-1'][" + str(a) +"]//div[@data-component-id='header']//input").send_keys(head3)
         except:
            pass
         try:
             head4= modinfo.find('div',class_='apm-centerthirdcol').h4.text.strip('\n').strip()
             bot.find_element_by_xpath("//div[@data-module-id='module-1'][" + str(a) +"]//div[@data-component-id='sub-header']//input").send_keys(head4)
         except:
            pass
         try:
             paras = modinfo.find('div',class_='apm-centerthirdcol').find_all('p')
             for para in paras:
                 pltext = para.text
                 bot.find_element_by_xpath("//div[@data-module-id='module-1'][" + str(a) +"]//div[@data-component-id='description']//div[starts-with(@aria-describedby,'placeholder')]").send_keys(pltext)
         except:
             pass
         try:
             bullen = modinfo.find("div",class_="amp-centerthirdcol-listbox").find_all("li")
             for count in range(1,len(bullen)):
                 click1=bot.find_element_by_xpath("//div[@data-module-id='module-1'][" + str(a) +"]//div[@data-component-id='list']//span[text()='+ Add bullet point']//parent::span//parent::button")
                 location = click1.location["y"]-100
                 bot.execute_script("window.scrollTo(0,%d);" %location)
                 click1.click()
             for info,ele in zip(bullen,bot.find_elements_by_xpath("//div[@data-module-id='module-1'][" + str(a) +"]//div[@data-component-id='list']//input")):
                 bulpnt = info.find("span",class_="a-size-base a-color-secondary").get_text()
                 ele.send_keys(bulpnt)
         except:
             pass
         try:
             head5 = modinfo.find('div',class_='apm-rightthirdcol-inner').find('h5').text.strip('\n').strip()
             bot.find_element_by_xpath("//div[@data-module-id='module-1'][" + str(a) +"]//div[@data-component-id='about-header']//input").send_keys(head5)
         except:
             pass
         paras = modinfo.find('div',class_='apm-rightthirdcol-inner').find_all('p')
         for para in paras:
             prtext= para.text
             bot.find_element_by_xpath("//div[@data-module-id='module-1'][" + str(a) +"]//div[@data-component-id='about-description']//div[starts-with(@aria-describedby,'placeholder')]").send_keys(prtext)
         #ContentWar()
    except:
        logging.info("ASIN: " + ASIN + "Error in Module 1")
        pass
root = Tk()
root.title("A+Content")
def click():
    global filename
    filename = filedialog.askopenfilename()
    root.destroy()

wid = root.winfo_screenwidth()/2
heig = root.winfo_screenheight()/2
x_cor = wid-125
y_cor = heig-36
root.geometry("%dx%d+%d+%d"%(250,72,x_cor,y_cor))
frame_name = Frame(root,bg="#ADD8E6")
label_1 = Label(frame_name,text = "Please choose a file path",width = "20",height="1",bg="#D3D3D3",font="Times 16")
button_1= Button(frame_name,text = "Click",bg="#D3D3D3",font="Times 14",width = "4",height ="1",command=click)
label_1.grid(row=1,column=1)
button_1.grid(row=2,column=1)
frame_name.grid(row=1,column=1)
root.mainloop()
AList=[]
TList=[]
TFDict={}

modulelist = ['module-12','module-11','module-10','module-9','module-8','module-7','module-6','module-5','module-4','module-3','module-2','module-1']
dname = datetime.datetime.now().microsecond
dname = "A+ Content" + str(dname)
#creating list
bot = webdriver.Chrome("C:\\Program Files (x86)\\SeleniumWrapper\\chromedriver.exe")
bot.maximize_window()
bot.implicitly_wait(50)
####################################

noSheets = pd.ExcelFile(filename)
for sht in noSheets.sheet_names:
    data = pd.read_excel(filename,sheet_name = sht)
    Asins = ""
    try:
        for ASIN2 in data['CHILD']:
            Asins += ", " + ASIN2
    except:
        break
    Asins = Asins[2:]
    Pasin = data.iloc[0,0]
    ProName = str(data.iloc[0,2])

####################################
#for ASIN1,ASIN2 in zip(data['PARENT'],data['CHILD']):
    #try:
    source = requests.get('https://www.amazon.com/dp/' + str(Pasin) + '?isDebug=1').text
    soup = BeautifulSoup(source,'lxml')
    all = soup.find_all('div',class_='aplus-module')
    if not all:
        if os.path.exists(os.environ['USERPROFILE'] + '/Desktop/' + dname):
            logging.basicConfig(filename = os.environ['USERPROFILE'] + '/Desktop/' + dname + '/my_log.log',level = logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s',datefmt = '%m/%d/%Y %H:%M:%S')
            logging.info("Parent ASIN does not have standard modules")
            continue
        else:
            os.makedirs(os.environ['USERPROFILE'] + '/Desktop/' + dname)
            logging.basicConfig(filename = os.environ['USERPROFILE'] + '/Desktop/' + dname + '/my_log.log',level = logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s',datefmt = '%m/%d/%Y %H:%M:%S')
            logging.info("Parent ASIN does not have standard modules")
            continue

    if all[0].attrs['class'][2] not in modulelist:
        logging.basicConfig(level = logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s',datefmt = '%m/%d/%Y %H:%M:%S')
        logging.info("Parent ASIN does not have standard modules")
        continue
    os.makedirs(os.environ['USERPROFILE'] + '/Desktop/' + dname + '/'+ ProName)
    imagePath = os.environ['USERPROFILE'] + '/Desktop/' + dname +'/'+ ProName
    logging.basicConfig(filename = os.environ['USERPROFILE'] + '/Desktop/' + dname + '/my_log.log',level = logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s',datefmt = '%m/%d/%Y %H:%M:%S')
    #logging.basicConfig(level = logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s',datefmt = '%m/%d/%Y %H:%M:%S')
    logging.info("ASIN: " + ProName + " Start Time")
    start = datetime.datetime.now()
    bot.get("https://sota-us.amazon.com/manager/")

    try:
        alert1 = bot.switch_to.alert
        alert1.accept()
    except:
        pass

    if re.search("midway", bot.current_url):
        while re.search("midway", bot.current_url):
            time.sleep(1)
    time.sleep(5)

    #window = Tk()
    #window.withdraw()
    #messagebox.showinfo("Click Start creating A+ content ")
    #time.sleep(5)
    try:
        bot.find_element_by_xpath("//span[text()='Start creating A+ content']").click()
        bot.find_element_by_xpath("//input[@class='awsui-input awsui-input-type-text'][1]").send_keys(ProName)
    except:
        bot.find_element_by_xpath("//span[text()='Start creating A+ content']").click()
        bot.back()
        lert1 = bot.switch_to.alert
        alert1.accept()
        bot.find_element_by_xpath("//span[text()='Start creating A+ content']").click()
        bot.find_element_by_xpath("//input[@class='awsui-input awsui-input-type-text'][1]").send_keys(ProName)

    bot.find_element_by_class_name("awsui-select-keyboard-area").click()
    bot.find_element_by_xpath("//span[text()='US English']").click()

    a=b=c=1
    d=e=f=1
    g=h=i=1
    j=k=l=1
    for x in range(len(all)):
        clasname = all[x].attrs['class'][2]
        modname = clasname.split('-')
        modnum = modname[1]
        modinfo = all[x]
        if clasname =='module-12':
            module12(ASIN2,l)
            l+=1
        elif clasname=='module-11':
            module11(ASIN2,k)
            k+=1
        elif clasname=='module-10':
            module10(ASIN2,j)
            j+=1
        elif clasname=='module-9':
            module9(ASIN2,i)
            i+=1
        elif clasname=='module-8':
            module8(ASIN2,h)
            h+=1
        elif clasname=='module-7':
            module7(ASIN2,g)
            g+=1
        elif clasname=='module-6' :
            module6(ASIN2,f)
            f+=1
        elif clasname=='module-5':
            module5(ASIN2,e)
            e+=1
        elif clasname=='module-4':
            module4(ASIN2,d)
            d+=1
        elif clasname=='module-3':
            module3(ASIN2,c)
            c+=1
        elif clasname=='module-2':
            module2(ASIN2,b)
            b+=1
        elif clasname=='module-1':
            module1(ASIN2,a)
            a+=1
    #bot.find_element_by_xpath("//span[text()='Save for later']//parent::span//parent::button").click()
    bot.find_element_by_xpath("//span[text()='Next: Apply ASINs']").click()
    bot.find_element_by_xpath("//input[@placeholder='Search for ASINs']").send_keys(Asins)
    time.sleep(5)
    bot.find_element_by_xpath("//input[@placeholder='Search for ASINs']").send_keys(Keys.ENTER)
    #bot.implicitly_wait(5)
    try:
        bot.find_element_by_xpath("//span[text()='Apply content']").click()
        time.sleep(2)
    except:
        window = Tk()
        window.withdraw()
        messagebox.showinfo("Apply ASINs")
        time.sleep(5)
        #bot.find_element_by_id("awsui-autosuggest-4").send_keys(Keys.ENTER)
        #bot.implicitly_wait(5)
        #bot.find_element_by_id("awsui-autosuggest-4").click()
        bot.find_element_by_xpath("//span[text()='Apply content']").click()
        time.sleep(2)
    #try:
        #bot.find_element_by_class_name("awsui-modal-hidden")
    #except:
    bot.find_element_by_xpath("//span[text()='Override']").click()
    time.sleep(2)
    bot.find_element_by_xpath("//span[text()='Save as draft']").click()
    logging.info("ASIN: " + ASIN2 + " End Time")
    end = datetime.datetime.now()
    t_diff= relativedelta(end,start)
    t_delta = '{h}:{m}:{s}'.format(h=t_diff.hours,m=t_diff.minutes,s=t_diff.seconds)
    AList.append(ASIN2)
    TList.append(str(t_delta))
    #except:
      #pass
    TFDict["ASIN"]=AList
    TFDict["Time"]=TList
    Tf = pd.DataFrame(TFDict)
    Tf.to_csv(os.environ['USERPROFILE'] + '/Desktop/' + dname +"/TimeSheet.csv",index=False)
window = Tk()
window.withdraw()
messagebox.showinfo("Completed")
