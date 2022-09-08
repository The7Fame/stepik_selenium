from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
    first_name.send_keys("Имя")
    second_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
    second_name.send_keys("Фамилия")
    email = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
    email.send_keys("test@test.test")
    phone = browser.find_element(By.CSS_SELECTOR, ".second_block .form-control.first")
    phone.send_keys(7777777)
    address = browser.find_element(By.CSS_SELECTOR, ".second_block .form-control.second")
    address.send_keys("Address")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()