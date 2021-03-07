import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Line import LINE
from config import Config


def jalan_coupon(key):
    #初期化
    all_coupon = []
    specific_coupon = []

    #クーポンurl
    all_facilities_url = 'https://www.jalan.net/discountCoupon/CAM4504742/'
    specific_facility_url = 'https://www.jalan.net/discountCoupon/CAM5078491/'
    
    #ブラウザ監視
    while True:
      #全施設クーポン
      all_coupon = coupon_check(all_coupon,all_facilities_url,"全国",key)
      time.sleep(5)
      #施設限定クーポン
      specific_coupon = coupon_check(specific_coupon, specific_facility_url,"施設限定",key)
      time.sleep(5)

 
def coupon_check(status_before, url, name,key):
    #ブラウザ非表示モード
    options = Options()
    options.add_argument('--headless')

    #クーポンページを取得
    driver = webdriver.Chrome('../chromedriver', options=options)
    driver.get(url) 

    #獲得可能クーポン状況を取得
    log = driver.find_elements_by_class_name("btn_01")
    status = list(map(lambda c: c.text, log))

    #クーポン状況に変更があれば
    if status != status_before:
      #獲得可能クーポンがあれば
      if len(status) != 0:
          for j in range(len(status)):
              print(name +status[j].replace('を獲得', 'が復活しました(^^)'))
              LINE(name+status[j].replace('を獲得', 'が復活しました(^^)'),key)
    return status

def main():
  config = Config()
  KEY = config.access_token
  jalan_coupon(KEY)

if __name__ == '__main__':
  main()
