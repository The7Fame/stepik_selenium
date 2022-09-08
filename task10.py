import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    result = calc(x_element.text)
    input_value = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_value.send_keys(result)
    find_checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    find_checkbox.click()
    find_radiobutton = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    browser.execute_script("arguments[0].scrollIntoView(true)", find_radiobutton)
    find_radiobutton.click()
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("arguments[0].scrollIntoView(true)", button)
    button.click()
finally:
    time.sleep(10)
    browser.quit()
