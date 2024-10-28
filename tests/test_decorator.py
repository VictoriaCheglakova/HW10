import allure
from selene import browser, have


def test_with_decorator():
    step_open()
    step_find()

@allure.step('Открываем главую страницу GitHub')
def step_open():
    browser.open('https://github.com/VictoriaCheglakova/HW10')

allure.step('Ищем название issure Homework#10')
def step_find():
    browser.element('#issues-tab').click()
    browser.element('#issue_1_link').should(have.exact_text('Homework #10'))