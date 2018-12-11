from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get("http://www.douban.com")

# 账号和密码
driver.find_element_by_name("form_email").send_keys("18747161745")
driver.find_element_by_name("form_password").send_keys("QWERTY0202")

# 模拟点击登录
driver.find_element_by_xpath('//input[@class="bn-submit"]').click()

# 等待3秒
time.sleep(3)

# 生成登录后快照
driver.save_screenshot('douban.png')

with open('douban.html', "w") as f:
    f.write(driver.page_source)

# driver.close()
driver.quit()