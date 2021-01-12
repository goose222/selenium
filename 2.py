
#!/usr/bin/env python
# -*-coding:utf-8-*-
# @File:3.py
# !/usr/bin/env python
# -*-coding:utf-8-*-
# @File:2.py
import os
import time
from selenium import webdriver
import json
from selenium.webdriver.support.ui import Select

# 引入chromedriver.exe
driver = "C:/Users/63093/AppData/Local/Programs/Python/Python38/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = driver
browser = webdriver.Chrome(driver)

# 设置为开发者模式
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])

# 设置浏览器需要打开的url
url = "】】"
browser.get(url)
time.sleep(2)

SupportClass = ["218", "220", "222", "339", "429", "432", "433", "649", "579", "630", "631", "632", "635", "51", "52",
                "2699", "70", "7161"]
filename = 'data.txt'


#############################功能函数####################################
def dataget():  # 获取
    datas = browser.find_elements_by_class_name('row')
    # datas[0].text.split(',')
    del datas[0:9]
    for data in datas:
        print(data.text)
        txt = str(data.text)
        with open('data4.txt', 'a', encoding='utf-8-sig') as file_handle:  # .txt可以不自己新建,代码会自动新建
            file_handle.write(txt)  # 写入
            file_handle.write('\n')  # 有时放在循环里面需要自动转行，不然会覆盖上一条数据


browser.find_element_by_id('ratificationYear').click()
time.sleep(0.5)
date = '/html/body/div[7]/div[5]/table/tbody/tr/td/span'
date = date + '[' + str(1) + ']'
browser.find_element_by_xpath(date).click()
time.sleep(0.5)
#########################################################181512
for n in [9]:

    browser.find_element_by_id('ratificationYear').click()
    time.sleep(0.5)
    date = '/html/body/div[7]/div[5]/table/tbody/tr/td/span'
    date = date + '[' + str(n) + ']'
    browser.find_element_by_xpath(date).click()
    time.sleep(0.5)

    browser.find_element_by_id("projectCode").click()  # 点开类别
    servingCode = browser.find_element_by_class_name("list-group")

    lis2 = servingCode.find_elements_by_xpath('li')  # 选择一级目录
    ele = lis2[2].find_elements_by_xpath('span') # G类打开
    ele[0].click()
    time.sleep(0.5)

    start = 0
    end = 0

    lis3 = servingCode.find_elements_by_xpath('li')
    for k in range(len(lis3)):
        if len(lis3[k].find_elements_by_xpath('span')) == 3:
            start = k
            break
    for k in range(start, len(lis3)):
        if len(lis3[k].find_elements_by_xpath('span')) <= 2:
            end = k
            break
    print(start, end)
    for k0 in range(start+14, end):
        lis3 = servingCode.find_elements_by_xpath('li')
        ele = lis3[k0].find_elements_by_xpath('span')  # G类二层打开
        ele[1].click()
        time.sleep(0.5)

        start1 = 0
        end1 = 0

        lis4 = servingCode.find_elements_by_xpath('li')
        for k in range(len(lis4)):
            if len(lis4[k].find_elements_by_xpath('span')) == 4:
                start1 = k
                break
        for k in range(start1, len(lis4)):
            if len(lis4[k].find_elements_by_xpath('span')) <= 3:
                end1 = k
                break
        print(start1, end1)
        for k1 in range(start1, end1):
            lis4 = servingCode.find_elements_by_xpath('li')
            ele = (lis4[k1].find_elements_by_xpath('span'))[2]
            if "glyphicon-plus" in ele.get_attribute('class'):  # 点开加号第三层
                ele.click()
            else:
                continue
            ########################################

            start2 = 0
            end2 = 0
            time.sleep(0.5)
            lis5 = servingCode.find_elements_by_xpath('li')
            for k in range(len(lis5)):
                if len(lis5[k].find_elements_by_xpath('span')) == 5:
                    start2 = k
                    break
            for k in range(start2, len(lis5)):
                if len(lis5[k].find_elements_by_xpath('span')) <= 4:
                    end2 = k
                    break
            print(start2, end2)
            for k2 in range(start2, end2):
                lis5 = servingCode.find_elements_by_xpath('li')
                browser.execute_script('arguments[0].scrollIntoView();', lis5[k2])
                if(k2!=start2):
                    browser.find_element_by_id("projectCode").click()  # 点开类别
                lis5[k2].click()

            # 选择资助类别
                for SC in SupportClass:
                    selectSC = Select(browser.find_element_by_id('supportClass'))
                    selectSC.select_by_value(SC)
                    browser.find_element_by_xpath(
                     '/html/body/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/button').click()
                    time.sleep(0.5)  # 点击检索

                    q = 1
                    a = browser.find_element_by_id("queryNum")
                    b = a.text
                    num = 0
                    for x in b:
                        if x >= '0' and x <= '9':
                            num = num * 10 + int(x) - int('0')
                    page = 0
                    time.sleep(0.5)
                    if num != 0:
                        page = (num + 5 - num % 5) / 5
                        if num % 5 == 0:
                            page = num / 5
                        dataget()
                        time.sleep(1)
                    while q < page:
                        time.sleep(3)
                        ul = browser.find_element_by_xpath('//*[@id="pageNoUl"]')
                        lis3 = ul.find_elements_by_xpath('li/a')
                        lis3[-1].click()
                        time.sleep(1)
                        dataget()
                        q = q + 1
                    time.sleep(0.5)

            browser.find_element_by_id("projectCode").click()  # 打开类别
            lis4 = servingCode.find_elements_by_xpath('li')
            ele = (lis4[k1].find_elements_by_xpath('span'))[2]
            if "glyphicon-minus" in ele.get_attribute('class'):  # 关上加号
                ele.click()

        #browser.find_element_by_id("projectCode").click()  # 打开类别
        lis3 = servingCode.find_elements_by_xpath('li')
        ele = lis3[k0].find_elements_by_xpath('span')  # G类二层打开
        ele[1].click()
        time.sleep(0.5)


