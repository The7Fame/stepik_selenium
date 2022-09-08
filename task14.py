from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()
try:
    driver.get('http://suninjuly.github.io/explicit_wait2.html')
    WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button_book = driver.find_element(By.ID, "book")
    button_book.click()
    input_value = driver.find_element(By.ID, "input_value")
    result = calc(input_value.text)
    answer = driver.find_element(By.ID, "answer")
    answer.send_keys(result)
    button_submit = driver.find_element(By.ID, "solve")
    button_submit.click()
    print(driver.switch_to.alert.text)

finally:
    driver.quit()