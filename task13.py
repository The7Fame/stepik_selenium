import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_page.html?"
    driver = webdriver.Chrome()
    driver.get(link)
    input_value = driver.find_element(By.ID, "input_value")
    result = calc(input_value.text)
    input_result = driver.find_element(By.ID, "answer")
    input_result.send_keys(result)
    button_submit = driver.find_element(By.TAG_NAME, "button")
    button_submit.click()
    print(driver.switch_to.alert.text)
finally:
    print("l")