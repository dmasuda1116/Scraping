import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from Line import LINE
from config import Config

import os

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
    relux_login()


    url = "https://rlx.jp/users/coupon/"
    while True:
        coupon_relux = coupon_check(coupon_relux,url,"relux","couponBox")
        time.sleep(10)



def relux_login():

    #初期設定
    config = Config()

    #ブラウザ非表示モード
    options = Options()
    #options.add_argument('--headless')

    #ログイン情報
    login_url = "https://connect.auone.jp/net/vwc/cca_lg_eu_nets/login?targeturl=https%3A%2F%2Fconnect.auone.jp%2Fnet%2Fid%2Fhny_rt_net%2Fcca%3FeventController%3Ddi.protocol.OpenIDSequencePluginChain%26event_doChain%26seqID%3DauOneOpenIDCollab%26windowId%3D414304151%26%40EntryPlugin%3DCookieCheckMgrPlugin.authVtkt&svc=id&cpkey=Pofd2Fqa3_1zVyRXJUWadTR6VXUxa2x5NnZ5ZFNVREE"
    login = config.id
    password = config.pw

    #chrome起動
    driver = webdriver.Chrome(config.driver_path, options=options)
    driver.get(login_url)

    # ログオン処理
    # ユーザー名入力
    driver.find_element_by_id("loginAliasId").send_keys(login)
    driver.find_element_by_id('btn_idInput').send_keys(Keys.ENTER)

    time.sleep(10)

    # パスワード入力
    driver.find_element_by_id("loginAuonePwd").send_keys(password)
    driver.find_element_by_id("btn_pwdLogin").send_keys(Keys.ENTER)
    time.sleep(30)
    driver.close()

def jalan_coupon():
    #初期化
    all_coupon = []
    specific_coupon = []
    coupon_log = []
    

    #クーポンurl
    #all_facilities_url = 'https://www.jalan.net/discountCoupon/CAM4504742/'
    #specific_facility_url = 'https://www.jalan.net/discountCoupon/CAM5078491/'
    all_facilities_url = 'https://www.jalan.net/discountCoupon/CAM9639471/'

    specific_facility_url = 'https://www.jalan.net/discountCoupon/CAM6635735/'
    
    #ブラウザ監視
    while True:
      #全施設クーポン
      all_coupon = coupon_check(all_coupon,all_facilities_url,"全国","btn_01")
      time.sleep(5)
      #施設限定クーポン
      coupon_log = jalan_fes(coupon_log)
      #specific_coupon = coupon_check(specific_coupon, specific_facility_url,"施設限定","btn_01")
      time.sleep(5)
      

def jalan_fes(coupon_log_before):
    #初期設定
    config = Config()

    #ブラウザ非表示モード
    options = Options()
    options.add_argument('--headless')

    #クーポンページを取得
    #driver = webdriver.Chrome(config.driver_path, options=options)
    #driver.get(url)
    coupon_log = [] 
    coupon_list = [500,1000,2000,3000,5000,20000]
    url = {}
    url[500] = "https://www.jalan.net/discountCoupon/CAM3189928/"
    url[1000] = "https://www.jalan.net/discountCoupon/CAM1914750/"
    url[2000] = "https://www.jalan.net/discountCoupon/CAM8531003/"
    url[3000] = "https://www.jalan.net/discountCoupon/CAM3961441/"
    url[5000] = "https://www.jalan.net/discountCoupon/CAM0776422/"
    url[20000] = "https://www.jalan.net/discountCoupon/CAM8075508/"
    for i in range(len(coupon_list)):
        driver = web_access(url[coupon_list[i]]) 
        elems = driver.find_elements_by_xpath("//a[@href]")
        for elem in elems:
            #print(type(elem.get_attribute("href")))
            if "javascript:doGetYadDisp" in elem.get_attribute("href"):
                coupon_log.append(str(coupon_list[i])+"円クーポン") 

    #クーポン復活の通知
    print(coupon_log)
    #dif = list_dif(coupon_log,coupon_log_before,coupon_log)[0]
    if len(dif) != 0:
        for i in range(len(dif)):
            LINE(dif[i] + url, "o9Ld67Aax4Bn452455CneBuZWCjeEHx9n5P7WNeq7Hw")
            #LINE(dif[i] + url, config.access_token)

    return coupon_log
                

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
            LINE(dif[i] + url, "o9Ld67Aax4Bn452455CneBuZWCjeEHx9n5P7WNeq7Hw")
            #LINE(dif[i] + url, config.access_token)

    return status

def test():
    config = Config()
    userdata_dir = 'test'  
    os.makedirs(userdata_dir, exist_ok=True)
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=' + userdata_dir)
    driver = webdriver.Chrome(config.driver_path, options=options)
    login_url = "https://connect.auone.jp/net/vwc/cca_lg_eu_nets/login?targeturl=https%3A%2F%2Fconnect.auone.jp%2Fnet%2Fid%2Fhny_rt_net%2Fcca%3FeventController%3Ddi.protocol.OpenIDSequencePluginChain%26event_doChain%26seqID%3DauOneOpenIDCollab%26windowId%3D414304151%26%40EntryPlugin%3DCookieCheckMgrPlugin.authVtkt&svc=id&cpkey=Pofd2Fqa3_1zVyRXJUWadTR6VXUxa2x5NnZ5ZFNVREE"
    driver.get(login_url)
    time.sleep(30)
def test2():
    config = Config()
    options = webdriver.chrome.options.Options()
    profile_path = 'test'
    options.add_argument('--user-data-dir=' + profile_path)
    driver = webdriver.Chrome(config.driver_path, options=options)
    login_url = "https://connect.auone.jp/net/vwc/cca_lg_eu_nets/login?targeturl=https%3A%2F%2Fconnect.auone.jp%2Fnet%2Fid%2Fhny_rt_net%2Fcca%3FeventController%3Ddi.protocol.OpenIDSequencePluginChain%26event_doChain%26seqID%3DauOneOpenIDCollab%26windowId%3D414304151%26%40EntryPlugin%3DCookieCheckMgrPlugin.authVtkt&svc=id&cpkey=Pofd2Fqa3_1zVyRXJUWadTR6VXUxa2x5NnZ5ZFNVREE"
    driver.get(login_url)

def main():
    jalan_coupon()
    #relux_coupon()
    #test()
    #jalan_fes()

if __name__ == '__main__':
    main()

