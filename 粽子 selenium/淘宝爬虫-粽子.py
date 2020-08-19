# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import csv
import re

# # 搜索商品，获取商品页码
# def search_product(key_word):
#     # 定位输入框
#     browser.find_element_by_id("q").send_keys(key_word)
#     # 定义点击按钮，并点击
#     browser.find_element_by_class_name('btn-search').click()
#     # 最大化窗口：为了方便我们扫码
#     browser.maximize_window()
#     # 等待15秒，给足时间我们扫码
#     time.sleep(15)
#     # 定位这个“页码”，获取“共100页这个文本”
#     page_info = browser.find_element_by_xpath('//div[@class="total"]').text
#     # 需要注意的是：findall()返回的是一个列表，虽然此时只有一个元素它也是一个列表。
#     page = re.findall("(\d+)",page_info)[0]
#     return page

# 获取数据
def get_data():
    # 通过页面分析发现：所有的信息都在items节点下
    items = browser.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
    for item in items:
        # 参数信息
        pro_desc = item.find_element_by_xpath('.//div[@class="row row-2 title"]/a').text
        # 价格
        pro_price = item.find_element_by_xpath('.//strong').text
        # 付款人数
        buy_num = item.find_element_by_xpath('.//div[@class="deal-cnt"]').text
        # 旗舰店
        shop = item.find_element_by_xpath('.//div[@class="shop"]/a').text
        # 发货地
        address = item.find_element_by_xpath('.//div[@class="location"]').text
        #print(pro_desc, pro_price, buy_num, shop, address)
        with open('{}.csv'.format(key_word), mode='a', newline='', encoding='utf-8-sig') as f:
            csv_writer = csv.writer(f, delimiter=',')
            csv_writer.writerow([pro_desc, pro_price, buy_num, shop, address])

def main():
    browser.get('https://www.taobao.com/')
    # page = search_product(key_word)
    # print(page) # 100
    get_data()
    page_num = 1
    print("正在爬取第1页")

    while page_num < 100:
        print("*" * 100)
        print("正在爬取第{}页".format(page_num + 1))
        browser.get('https://s.taobao.com/search?q={}&s={}'.format(key_word, page_num*44))
        browser.implicitly_wait(15)
        get_data()
        page_num += 1
    print("数据爬取完毕！")

if __name__ == '__main__':
    key_word = "粽子"
    browser = webdriver.Chrome()
    main()