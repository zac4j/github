from time import sleep

from selenium import webdriver
import getui_push

url = 'https://weibo.com/5884573948/H7wJvgD7M?ref=home&rid=0_131072_8_4725540773956118792_0_0&type=comment'


def start_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.start_client()
    return driver


def find_info():
    css_selector = 'span > span > span > em:nth-child(2)'
    elems = driver.find_elements_by_css_selector(css_selector)
    return [int(elem.text) for elem in elems[1:]]


while True:
    driver = start_chrome()
    driver.get(url)
    # wait loading
    sleep(6)
    info = find_info()
    # [49, 53, 224]
    repost, comment, like = info
    if repost > 50:
        text = f'your monitor weibo repost number has more than:{repost}'
        msg = {'title': 'Weibo Monitor', 'text': text, 'url': url}
        getui_push.push_message(msg)
        print(text)
        break
    else:
        print('Nothing happens')

    sleep(2 * 1000)

print("Done!")
