from time import sleep

from selenium import webdriver


def start_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.start_client()
    return driver


def find_strangers():
    btn_sel = '#Profile-following > div:nth-child(2) > div > div > div > div.ContentItem-extra > button'
    return driver.find_elements_by_css_selector(btn_sel)


url = 'https://www.zhihu.com'
follower_url = 'https://www.zhihu.com/people/zac_ju/followers'

tick = 0

while True:
    driver = start_chrome()
    driver.get(url)
    if not driver.get_cookies():
        # push()
        sleep(20)
        break

    if tick > 5:
        break

    sleep(20)  # wait login

    driver.get(follower_url)

    sleep(6)  # wait follower page load complete
    tick += 1
    strangers = find_strangers()
    for s in strangers:
        s.click()
        sleep(3)

    print('Done!')
    sleep(20 * 1000)
