import allure
from selene import browser, have


def test_with_step():
    with allure.step('Открываем главую страницу GitHub'):
        browser.open('https://github.com/VictoriaCheglakova/HW10')
    with allure.step('Ищем название issure Homework#10'):
        browser.element('#issues-tab').click()
        browser.element('#issue_1_link').should(have.exact_text('Homework #10'))