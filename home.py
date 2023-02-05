import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
go = driver.find_element_by_css_selector("[title = 'Selenium Ruby']").click()
switch = driver.find_element_by_xpath("//a[@href = '#tab-reviews']").click()
star5 = driver.find_element_by_css_selector(".comment-form > p .stars .star-5").click()
text = driver.find_element_by_css_selector("[id = 'comment']")
text.send_keys("Nice book!")
name = driver.find_element_by_css_selector("[name = 'author']")
name.send_keys("AnnaLeykht")
email_adress = driver.find_element_by_id("email")
email_adress.send_keys("s.tree.t@mail.ru")
submit = driver.find_element_by_id("submit").click()
