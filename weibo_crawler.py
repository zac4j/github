# start_chrome -> input_date -> scroll_down_end -> find_cards_info -> save -> find_next

from time import sleep

from selenium import webdriver
import csv
import os

from selenium.webdriver.common.keys import Keys


def open_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.start_client()
    return driver


def query(star_time, end_time):
    return f'?is_ori=1&key_word=&start_time={star_time}&end_time={end_time}&is_search=1&is_searchadv=1#_0'


def scroll_down():
    html_page = driver.find_element_by_tag_name('html')
    # form > input
    for i in range(15):
        html_page.send_keys(Keys.END)
        sleep(0.6)


def find_cards_info():
    cards_sel = 'div.WB_feed_detail.clearfix'
    cards = driver.find_elements_by_css_selector(cards_sel)
    info_list = []

    for card in cards:
        content_sel = 'div.WB_text.W_f14'
        time_sel = 'div.WB_from.S_txt2 > a:nth-child(1)'
        link_sel = 'div.WB_from.S_txt2 > a:nth-child(2)'

        content = card.find_element_by_css_selector(content_sel)
        time = card.find_element_by_css_selector(time_sel)
        link = card.find_element_by_css_selector(link_sel)
        info_list.append([content, time, link])

    return info_list


def find_next():
    next_sel = '#Pl_Official_MyProfileFeed__20 > div > div:nth-child(38) > div > a'
    next_page = driver.find_elements_by_css_selector(next_sel)
    if next_page:
        return next_page[0].get_attribute('href')


def save(info_list, name):
    full_path = './' + name + '.csv'  # 2018-01-02~2018-08-08.csv
    if os.path.exists(full_path):
        with open(full_path, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(info_list)
            print('Done!')
    else:
        with open(full_path, 'w+') as f:
            writer = csv.writer(f)
            writer.writerow(info_list)
            print('Done!')


def run_crawler(base, duration):
    if not base.endswith('feedtop'):
        # duration: 2018-01-02~2018-08-08
        start_time, end_time = duration.split('~')
        driver.get(base + query(start_time, end_time))
    else:
        driver.get(base)

    sleep(5)
    scroll_down()
    sleep(5)
    info_list = find_cards_info()
    save(info_list, duration)
    next_page = find_next()
    if next_page:
        run_crawler(next_page)
    print(info_list)


base = 'https://weibo.com/u/6431633590'
driver = open_chrome()
input()
run_crawler(base, '2018-01-02~2018-08-08')
