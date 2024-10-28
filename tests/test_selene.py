import allure
from selene import browser, have
from selene.core.query import text_content


def test_check_issue():
    browser.open('https://github.com/VictoriaCheglakova/HW10')
    browser.element('#issues-tab').click()
    browser.element('#issue_1_link').should(have.exact_text('Homework #10'))





