import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Line import LINE
from config import Config

def list_dif(list_1,list_2,name):
    first = [name + i.replace('を獲得', 'が復活しました(^^)') for i in list(set(list_1) -set(list_2))]
    second = [name + i.replace('を獲得', 'の配布は終了しました>_<') for i in list(set(list_2) -set(list_1))]
    return [first,second]

def web_access(url):
    #初期設定
    options = Options()

    #ブラウザ非表示モード
    options.add_argument('--headless')
    config = Config()

    #クーポンページを取得
    while True:
        driver = webdriver.Chrome(config.driver_path, options=options)
        driver.get(url)
        driver.implicitly_wait(10)
        print (driver.current_url)
        if driver.current_url == url:
            break
    return driver

def relux_coupon():
    coupon_relux = []
    #log = driver.find_elements_by_class_name("btn_01")

    url = "https://rlx.jp/users/coupon/"
    while True:
        coupon_relux = coupon_check(coupon_relux,url,"relux","couponBox")
        time.sleep(10)





def jalan_coupon():
    #初期化
    all_coupon = []
    specific_coupon = []

    #クーポンurl
    #all_facilities_url = 'https://www.jalan.net/discountCoupon/CAM4504742/'
    #specific_facility_url = 'https://www.jalan.net/discountCoupon/CAM5078491/'
    all_facilities_url = 'https://www.jalan.net/discountCoupon/CAM6003447/'
    specific_facility_url = 'https://www.jalan.net/discountCoupon/CAM6635735/'
    
    #ブラウザ監視
    while True:
      #全施設クーポン
      all_coupon = coupon_check(all_coupon,all_facilities_url,"全国","btn_01")
      time.sleep(5)
      #施設限定クーポン
      specific_coupon = coupon_check(specific_coupon, specific_facility_url,"施設限定","btn_01")
      time.sleep(5)

def coupon_check(status_before, url, name, class_name):
    #初期設定
    config = Config()

    #ブラウザ非表示モード
    options = Options()
    options.add_argument('--headless')

    #クーポンページを取得
    #driver = webdriver.Chrome(config.driver_path, options=options)
    #driver.get(url)
    driver = web_access(url) 
    print(driver)

    #獲得可能クーポン状況を取得
    log = driver.find_elements_by_class_name(class_name)
    status = list(map(lambda c: c.text, log))
    driver.quit()

    #クーポン復活の通知
    dif = list_dif(status,status_before,name)[0]
    if len(dif) != 0:
        for i in range(len(dif)):
            LINE(dif[i] + url, o9Ld67Aax4Bn452455CneBuZWCjeEHx9n5P7WNeq7Hw)
            #LINE(dif[i] + url, config.access_token)

    return status

def main():
    #jalan_coupon()
    relux_coupon()

if __name__ == '__main__':
    main()
