from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
        
    robot_radio = browser.find_element_by_id("robotsRule")
    robot_checked = robot_radio.get_attribute("name")
    print("value of robot radio: ", robot_checked)

    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("check")
    print("value of people radio: ", people_checked)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
