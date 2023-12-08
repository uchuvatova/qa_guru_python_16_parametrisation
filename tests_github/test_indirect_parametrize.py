"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
from selene import browser, have

from conftest import only_desktop, only_mobile


@only_desktop
def test_github_sign_in_desktop(desktop_browser):
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').click()

    browser.element('#login').should(have.text('Sign in to GitHub'))


@only_mobile
def test_github_sign_in_mobile(mobile_browser):
    browser.open('https://github.com')
    browser.element('.js-details-target.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()

    browser.element('#login').should(have.text('Sign in to GitHub'))
