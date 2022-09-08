import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')


try:
    link = "http://suninjuly.github.io/file_input.html"
    driver = webdriver.Chrome()
    driver.get(link)
    input_name = driver.find_element(By.NAME, "firstname")
    input_name.send_keys("First")
    input_second = driver.find_element(By.NAME, "lastname")
    input_second.send_keys("Seconds")
    input_email = driver.find_element(By.NAME, "email")
    input_email.send_keys("email@email.email")
    input_file = driver.find_element(By.NAME, "file")
    input_file.send_keys(file_path)
    button_submit = driver.find_element(By.TAG_NAME, "button")
    button_submit.click()
finally:
    time.sleep(10)
    driver.quit()