# 執行 command 的時候用的
import os

# 整理 json, csv 使用的工具
import json, csv


# 建立儲存 csv 檔的資料夾
csvFolder = 'youbike1.0_csv'
if not os.path.exists(csvFolder):
    os.makedirs(csvFolder)

# 轉成 csv 使用的變數，檔名相同，差異只在.json or .csv  
def input_for_csv():
    while True:
        text = input("input exist jsonfile name only (without .json): ")
    
        # 要開啟的檔案路徑
        filepath = f"youbike1.0/{text}.json"
        
        # 檢查檔案是否存在
        if os.path.isfile(filepath):
            print("file exist, converting to csv...")
            return text # 存成 json 檔的時候會用到，所以要給回傳值
            break
        else:
            print("file doesn't exist, please try again")
            continue

# 讀取 json 使用的變數
def input_for_json():
    inputF = text + '.json'
    return inputF

def json_toCSV():
    with open(f"youbike1.0/{inputF}", encoding = "UTF-8") as json_file:
        jsondata = json.load(json_file)
    data_file = open(f'{csvFolder}/{text}.csv','w', encoding = "UTF-8", newline='')
    csv_writer = csv.writer(data_file)
    count = 0
    for data in jsondata:
        if count == 0:
            header = data.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(data.values())
    data_file.close()
    print('done!')

if __name__ == '__main__':
    text = input_for_csv() # 將回傳值丟給 text 全域變數，json_toCSV()才能夠使用
    inputF = input_for_json()
    json_toCSV()
    
    
    