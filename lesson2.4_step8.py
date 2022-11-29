from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button1 = browser.find_element(By.ID, "book")
    button1.click()

    x_element = browser.find_element(By.ID, "input_value")
    number = x_element.text
    y = calc(number)

    inpt = browser.find_element(By.ID, "answer")
    inpt.send_keys(y)
    
    button2 = browser.find_element(By.ID, "solve")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
