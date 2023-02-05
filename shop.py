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
# email_adress = driver.find_element_by_id("username")
# email_adress.send_keys("s.tree.t@mail.ru\n")
# password = driver.find_element_by_id("password")
# password.send_keys("cat345strong!")
# button_submit = driver.find_element_by_css_selector(".login .woocommerce-Button ,button").click()
# shop = driver.find_element_by_link_text("Shop").click()
# book = driver.find_element_by_css_selector(".post-181 > a > img").click()
# namebook = driver.find_element_by_css_selector(".product_title.entry-title")
# message = namebook.text
# print(message)
# if message == "HTML5 Forms":
#     print("Right!")
# else:
#     print("Wrong message")

# #Shop:количество товаров в категории
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
# email_adress = driver.find_element_by_id("username")
# email_adress.send_keys("s.tree.t@mail.ru\n")
# password = driver.find_element_by_id("password")
# password.send_keys("cat345strong!")
# button_submit = driver.find_element_by_css_selector(".login .woocommerce-Button ,button").click()
# shop = driver.find_element_by_link_text("Shop").click()
# html = driver.find_element_by_link_text("HTML").click()
# page = driver.find_elements_by_css_selector(".pagewidth.clearfix > div > ul > li")
# if len(page) == 3:
#  print("На странице 3 товара")
# else:
#  print("Ошибка. Количество товаров на странице: " + str(len(page)))

#Shop: сортировка товаров
# import time
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("http://practice.automationtesting.in/")
# my_account = driver.find_element_by_xpath("//a[@href = 'https://practice.automationtesting.in/my-account/']").click()
# email_adress = driver.find_element_by_id("username")
# email_adress.send_keys("s.tree.t@mail.ru\n")
# password = driver.find_element_by_id("password")
# password.send_keys("cat345strong!")
# button_submit = driver.find_element_by_css_selector(".login .woocommerce-Button ,button").click()
# shop = driver.find_element_by_link_text("Shop").click()
# element = driver.find_element_by_css_selector(".orderby > option:nth-child(1)")
# element_value = element.get_attribute("value")
# if element_value == 'menu_order':
#    print("Верно!")
# else:
#    print("Ошибка", element_value)
# element_price = driver.find_element_by_css_selector(".woocommerce-ordering > select")
# select = Select(element_price)
# select.select_by_value("price-desc")
# Default_sorting = driver.find_element_by_css_selector(".woocommerce-ordering > select")
# select = Select(Default_sorting)
# select.select_by_value("menu_order")
# element_price2= driver.find_element_by_css_selector(".woocommerce-ordering > select")
# element_value2 = element_price2.get_attribute("value")
# if element_value2 == 'price-desc':
#    print("Верно!")
# else:
#    print("Ошибка", element_value2)

# # Shop: отображение, скидка товара
# import time
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("http://practice.automationtesting.in/")
# my_account = driver.find_element_by_xpath("//a[@href = 'https://practice.automationtesting.in/my-account/']").click()
# email_adress = driver.find_element_by_id("username")
# email_adress.send_keys("s.tree.t@mail.ru\n")
# password = driver.find_element_by_id("password")
# password.send_keys("cat345strong!")
# button_submit = driver.find_element_by_css_selector(".login .woocommerce-Button ,button").click()
# shop = driver.find_element_by_link_text("Shop").click()
# android_quick = driver.find_element_by_css_selector(".post-169 > a > img").click()
# price = driver.find_element_by_css_selector(".price >del .woocommerce-Price-amount.amount")
# price_text = price.text
# assert "600" in price_text
# price_new = driver.find_element_by_css_selector(".price >ins .woocommerce-Price-amount.amount")
# price_new_text = price_new.text
# assert "450" in price_new_text
# picture_open = driver.find_element_by_xpath("//a[@href='https://practice.automationtesting.in/wp-content/uploads/2017/01/Android-Quick-Start-Guide.png']").click()
# wait = WebDriverWait(driver, 10)
# picture = wait.until(EC.url_to_be("https://practice.automationtesting.in/product/android-quick-start-guide/"))
# how_many= wait.until(EC.number_of_windows_to_be(1))
# print(how_many)
# picture_close = driver.find_element_by_css_selector(".pp_close").click()
# C:/Users/stree/PycharmProjects/pythonProject1/BeTester/book_store_testing

