import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get('https://www.amazon.in/')
# driver.maximize_window()
time.sleep(5)

ele=driver.find_element(By.XPATH,'//span[@class="nav-line-2 "]//span')
act=ActionChains(driver)
act.move_to_element(ele).perform()
ele1=driver.find_element(By.LINK_TEXT,'Sign in')
act.move_to_element(ele1).double_click(ele1).perform()
time.sleep(2)
driver.find_element(By.XPATH,'//input[@id="ap_email"]').send_keys('sushantgdekar@gmail.com')
driver.find_element(By.ID,"continue").click()
time.sleep(2)
driver.find_element(By.ID,"ap_password").send_keys('test_automation@10')
time.sleep(2)
driver.find_element(By.ID,"signInSubmit").click()
time.sleep(2)
act_title=driver.title
exp_title='Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in'
if act_title==exp_title:
    print("Result:","Pass")
button=driver.find_element(By.ID,"searchDropdownBox")
drop=Select(button)
drop.select_by_visible_text("Clothing & Accessories")

# driver.find_element(By.ID,"twotabsearchtextbox").send_keys("iphone 13")
# time.sleep(1)
# driver.find_element(By.ID,"nav-search-submit-button").click()

# driver.find_element(By.ID,'//*[contains(text(), "Apple iPhone 13 (256GB) - (Product) RED")]').click()
time.sleep(5)

driver.find_element(By.XPATH,'//img[@class="s-image" and (@src="https://m.media-amazon.com/images/I/61KeIxmldLL._AC_UY218_.jpg")]').click()
time.sleep(10)
