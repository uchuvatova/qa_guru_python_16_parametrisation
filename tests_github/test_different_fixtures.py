"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
from selene import browser, have


def test_github_sign_in_desktop(desktop_browser):
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').click()

    browser.element('#login').should(have.text('Sign in to GitHub'))


def test_github_sign_in_mobile(mobile_browser):
    browser.open('https://github.com')
    browser.element('.js-details-target.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()

    browser.element('#login').should(have.text('Sign in to GitHub'))
