import time_post as driver
import json
import time

def main():
    success_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("结束运行:", success_time)
    
    # 写入运行成功的时间到 success.txt 文件
    with open('success.txt', 'w') as success_file:
 
        success_file.write(f"程序运行成功时间: {success_time}\n")
        
   
    with open('/root/time-driver/info.json', 'r') as f:
        data = json.load(f)

    for item in data:
        # print(item['license_id'], item['region_id'], item['price_per_month'], item['minimum_stay_month'], item['desc'])
        # 发送POST请求
        driver.Post(item['license_id'], item['region_id'], item['price_per_month'], item['minimum_stay_month'], item['desc'])
        time.sleep(15)
        print("等待15秒")
    print("结束运行:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    
if __name__ == '__main__':
    main()
# 测试1
