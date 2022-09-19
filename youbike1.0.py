import requests as req

# 操作 browser 的 API
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 自動下載chrome，並且判斷瀏覽器版本
from webdriver_manager.chrome import ChromeDriverManager

# 處理逾時例外的工具
from selenium.common.exceptions import TimeoutException

# 面對動態網頁，等待某個元素出現的工具，通常與 exptected_conditions 搭配
from selenium.webdriver.support.ui import WebDriverWait

# 搭配 WebDriverWait 使用，對元素狀態的一種期待條件，若條件發生，則等待結束，往下一行執行
from selenium.webdriver.support import expected_conditions as EC

# 期待元素出現要透過什麼方式指定，通常與 EC、WebDriverWait 一起使用
from selenium.webdriver.common.by import By

# 強制等待 (執行期間休息一下)
from time import sleep

# 整理 json, csv使用的工具
import json, csv

# 執行 command 的時候用的
import os

# 子處理程序，用來取代 os.system 的功能
import subprocess

import numpy as np

# 建立儲存json檔的資料夾
folderPath = 'youbike1.0'
if not os.path.exists(folderPath):
    os.makedirs(folderPath)

# 放置爬取的資料
listData = []

# 輸入爬蟲日期或時間設為檔名
def inputTime():
    text = input("input date/time: ")
    return text # 存成 json 檔的時候會用到，所以要給回傳值

# 走訪頁面
def visit():
    url = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"
    r = req.get(url)
    obj = json.loads(r.text) # 將 json 檔變成文字檔
    for x in (1,2,3):
        if x==1:
            for n in range(1,10):
                try:
                    # print(obj['retVal']['000' + str(n)])
                    listData.append(obj['retVal']['000' + str(n)])
                except:
                    KeyError
        if x==2:
            for n in range(10,99):
                try:
                    # print(obj['retVal']['00' + str(n)])
                    listData.append(obj['retVal']['00' + str(n)])
                except:
                    KeyError
        if x==3:
            for n in range(99,406):
                try:
                    # print(obj['retVal']['0' + str(n)])
                    listData.append(obj['retVal']['0' + str(n)])
                except:
                    KeyError
    sleep(3)
    
# 顯示每次爬的時間點
def showTime():
    print(listData[count]['sna'],listData[count]['mday'])

# 存成 json 
def savejson():
    with open (f"{folderPath}/youbike1.0_{text}.json", "w", encoding = "utf-8") as file:
        file.write(json.dumps(listData, ensure_ascii = False, indent = 4))
        
# 計算爬取一次的站數，避免有站點撤站的情況，而使用者卻不知道
def countLen():
    with open(f"{folderPath}/youbike1.0_{text}.json", 'r', encoding='UTF-8') as file:
        data = json.load(file)
    items_num = len(data)
    return items_num


# ## *** 需要時可以在cmd輸入: jupyter notebook --NotebookApp.iopub_data_rate_limit=1.0e10，會開啟 jupyter 網頁才不會報錯 ***

if __name__ == '__main__':
    text = inputTime() # 將回傳值丟給 text 全域變數，savejson()才能夠使用
    count = 0 # 計數器，才能讓每次新爬取的資料顯現在螢幕上，確認爬到的資料完整以及觀看進度 > showTime()
    while True:
        visit()
        showTime()
        savejson()
        sleep(180) # 決定多久爬一次網頁，與網頁更新時間有關
        count = countLen()

