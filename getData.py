from selenium import webdriver

options = webdriver.ChromeOptions()
# options.add_argument("user-data-dir=selenium")
driver = webdriver.Chrome("/Users/ahmed/Documents/Scripts/chromedriver", chrome_options=options)

f = open('demofile1.txt', 'r')
g = open('data.csv', 'w')
driver.get("https://my.gumtree.com/login")

check = input("login and press 1 to continue...")
if check == 1:
    print ("Continue...")
    for line in f:
        print ("in file now")
        driver.get(line)

        print ("waiting for 20 sec..")
        driver.implicitly_wait(20)
        button = driver.find_elements_by_css_selector("#reply-panel-reveal-btn")
        print ("Found Button")
        driver.get(button[0].get_attribute("href"))
        print ("Button Clicked")

        address = driver.find_elements_by_css_selector(
            "body > div.is-being-refined-hide.letterbox > div > div.grid-container.main > main > div.grid-col-12.grid-col-l-8.vip-content > header > strong > span")[
            0].text
        name = driver.find_elements_by_css_selector(
            "body > div.is-being-refined-hide.letterbox > div > div.grid-container.main > main > div.grid-col-m-6.hide-fully-to-m.grid-col-m-right.grid-col-l-4 > section.box.box-peelshadow-r > div > div.media.space-man > div > div.space-pls.space-pts.space-prs > h2")[
            0].text
        phone = driver.find_elements_by_css_selector(
            "body > div.is-being-refined-hide.letterbox > div > div.grid-container.main > main > div.grid-col-m-6.hide-fully-to-m.grid-col-m-right.grid-col-l-4 > section.box.box-peelshadow-r > div > div.space-pas > div.clearfix > strong")[
            0].text

        print address
        print name
        print phone
        f.write(str(address) + "\t" + str(name) + "\t" + str(phone))
        f.write("\n")
        print ("Done job: " + line)

driver.close()
