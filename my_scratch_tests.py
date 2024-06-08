from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "https://seclub.org/"
browser = webdriver.Chrome()
browser.get(link)

login_button = browser.find_element(By.XPATH, "/html/body/div[2]/a[2]").click()
name_button = browser.find_element(By.XPATH, "/html/body/form/div[1]/input")
name_button.send_keys("admin")

password_button = browser.find_element(By.XPATH, "/html/body/form/div[2]/input")
password_button.send_keys("admin")

enter_button = browser.find_element(By.XPATH,"/html/body/form/div[3]/input")
enter_button.click()

security_check = browser.find_element(By.XPATH, "/html/body/div[3]").text
security_check_result = "Ошибка авторизации, проверьте логин и пароль!"
if security_check == security_check_result:
    print("Тест на безопасность пройден успешно")






