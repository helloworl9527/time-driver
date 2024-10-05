import time_post as driver
import json
import time

def main():
    with open('info.json', 'r') as f:
        data = json.load(f)

    for item in data:
        # print(item['license_id'], item['region_id'], item['price_per_month'], item['minimum_stay_month'], item['desc'])
        # 发送POST请求
        driver.Post(item['license_id'], item['region_id'], item['price_per_month'], item['minimum_stay_month'], item['desc'])
        time.sleep(15)
        print("等待15秒")
    print("结束运行:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

main()
