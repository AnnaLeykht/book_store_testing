# import time
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("http://practice.automationtesting.in/")
# my_account = driver.find_element_by_xpath("//a[@href = 'https://practice.automationtesting.in/my-account/']").click()
# email_adress = driver.find_element_by_id("reg_email")
# email_adress.send_keys("s.tree.t@mail.ru\n")
# password = driver.find_element_by_id("reg_password")
# password.send_keys("cat345strong!")
# button_submit = driver.find_element_by_css_selector(".woocomerce-FormRow.form-row .woocommerce-Button").click()

# Ввод логина
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
my_account = driver.find_element_by_xpath("//a[@href = 'https://practice.automationtesting.in/my-account/']").click()
email_adress = driver.find_element_by_id("username")
email_adress.send_keys("s.tree.t@mail.ru\n")
password = driver.find_element_by_id("password")
password.send_keys("cat345strong!")
button_submit = driver.find_element_by_css_selector(".login .woocommerce-Button ,button").click()
text_to_be_logout = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".page-template-default"), "Logout"))