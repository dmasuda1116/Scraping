import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Line import LINE
from config import Config

def list_dif(list_1,list_2,name):
    first = [name + i.replace('を獲得', 'が復活しました(^^)') for i in list(set(list_1) -set(list_2))]
    second = [name + i.replace('を獲得', 'の配布は終了しました>_<') for i in list(set(list_2) -set(list_1))]
    return [first,second]

def jalan_coupon():
    #初期化
    all_coupon = []
    specific_coupon = []

    #クーポンurl
    all_facilities_url = 'https://www.jalan.net/discountCoupon/CAM4504742/'
    specific_facility_url = 'https://www.jalan.net/discountCoupon/CAM5078491/'
    
    #ブラウザ監視
    while True:
      #全施設クーポン
      all_coupon = coupon_check(all_coupon,all_facilities_url,"全国")
      time.sleep(5)
      #施設限定クーポン
      specific_coupon = coupon_check(specific_coupon, specific_facility_url,"施設限定")
      time.sleep(5)

def coupon_check(status_before, url, name):
    #初期設定
    config = Config()

    #ブラウザ非表示モード
    options = Options()
    options.add_argument('--headless')

    #クーポンページを取得
    driver = webdriver.Chrome(config.driver_path, options=options)
    driver.get(url) 

    #獲得可能クーポン状況を取得
    log = driver.find_elements_by_class_name("btn_01")
    status = list(map(lambda c: c.text, log))
    driver.quit()

    #クーポン復活の通知
    dif = list_dif(status,status_before,name)[0]
    if len(dif) != 0:
        for i in range(len(dif)):
            LINE(dif[i], config.access_token)

    return status

def main():
    jalan_coupon()

if __name__ == '__main__':
    main()
