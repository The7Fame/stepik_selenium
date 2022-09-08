import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

try:

    link = "http://suninjuly.github.io/selects1.html"
    driver = webdriver.Chrome()
    driver.get(link)
    num_1 = driver.find_element(By.ID, "num1")
    num_2 = driver.find_element(By.ID, "num2")
    sum = int(num_1.text) + int(num_2.text)
    dropdown = Select(driver.find_element(By.ID, "dropdown"))
    dropdown.select_by_value(str(sum))
    button_submit = driver.find_element(By.TAG_NAME, "button")
    button_submit.click()
finally:
    time.sleep(10)
    driver.quit()
