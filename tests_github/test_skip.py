"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, have


def test_github_sign_in_desktop(browser_size):
    if browser_size == "mobile":
        pytest.skip(reason="Тест только для десктоп")
    browser.open("https://github.com/")
    browser.element('.HeaderMenu-link--sign-in').click()

    browser.element('#login').should(have.text('Sign in to GitHub'))


def test_github_sign_in_mobile(browser_size):
    if browser_size == "desktop":
        pytest.skip(reason="Тест только для мобильного браузера")
    browser.open("https://github.com/")
    browser.element('.HeaderMenu-toggle-bar').click()
    browser.element('.HeaderMenu-link--sign-in').click()

    browser.element('#login').should(have.text('Sign in to GitHub'))
