import os

from selenium import webdriver

config = {
    'chromedriver_path': '/Users/ahmed/Documents/Scripts/chromedriver',
    'ww_url': "https://www.gumtree.com/search?featured_filter=false&urgent_filter=false&sort=date&search_scope=false&photos_filter=false&search_category=all&q=man+and+van&tq=&search_location=United+Kingdom&tl"
}

driver = webdriver.Chrome(config['chromedriver_path'])
driver.get(config['ww_url'])

f = open("demofile1.txt", "a")


def links():
    html_list = driver.find_element_by_class_name("list-listing-mini")
    items = html_list.find_elements_by_css_selector("li.natural article a:link")
    for i in items:
        print i.get_attribute("href")
        f.write(i.get_attribute("href"))
        f.write("\n")


while True:
    check = input("press 1 to continue")
    if check == 1:
        print ("Continue...")
        links()
    else:
        break

f.close()
driver.close()

