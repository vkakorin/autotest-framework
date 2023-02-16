import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    # Створення об'єкту для керування бразуером
    driver = webdriver.Chrome(
        service=Service(r"/Users/vkakorin/PycharmProjects/AutotestFramework" + "chromedriver")
        )

    # відкриваємо сторінку https://github.com/login
    driver.get("https://github.com/login")

    # Знаходимо поле, в яке будемо вводити неправильне ім'я користувача або поштову адресу
    driver.find_element(By.ID, "login_field").send_keys('kakorinviktor@nomail.com')

    # Знаходимо поле, в яке будемо вводити неправильний пароль
    driver.find_element(By.ID, "password").send_keys('test_password')

    # Знаходимо кнопку sign in. Емулюємо клік
    driver.find_element(By.NAME, "commit").click()

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert driver.title == "Sign in to GitHub · GitHub"

    # Закриваємо браузер
    driver.close()
