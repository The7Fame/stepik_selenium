from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    result = calc(x_element.text)
    input_value = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_value.send_keys(result)
    find_checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    find_checkbox.click()
    find_radiobutton = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    find_radiobutton.click()
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()