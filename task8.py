from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure_value = browser.find_element(By.ID, "treasure")
    value = treasure_value.get_attribute("valuex")
    calculated = calc(value)
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(calculated)
    find_checkbox = browser.find_element(By.ID, "robotCheckbox")
    find_checkbox.click()
    find_radiobutton = browser.find_element(By.ID, "robotsRule")
    find_radiobutton.click()
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()