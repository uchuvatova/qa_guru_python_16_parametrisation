from dataclasses import dataclass

import pytest
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

options = Options()
options.add_argument("--remote-debugging-port=9222")
driver = webdriver.Chrome(options=options)
browser.config.driver = driver


@dataclass
class Size:
    width: int
    height: int

    def __repr__(self):
        return f"({self.width}_{self.height})"


desktop1 = Size(width=3840, height=2160)
desktop2 = Size(width=1920, height=1080)
mobile1 = Size(width=353, height=745)
mobile2 = Size(width=414, height=896)


@pytest.fixture(
    params=[(desktop1.width, desktop1.height),
            (desktop2.width, desktop2.height),
            (mobile1.width, mobile1.height),
            (mobile2.width, mobile2.height)], ids=repr)
def browser_size(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    if request.param[0] >= request.param[1]:
        return "desktop"
    else:
        return "mobile"


only_desktop = pytest.mark.parametrize(
    "browser_size", [(desktop1.width, desktop1.height), (desktop2.width, desktop2.height)],
    indirect=True, ids=repr)
only_mobile = pytest.mark.parametrize(
    "browser_size", [(mobile1.width, mobile1.height), (mobile2.width, mobile2.height)],
    indirect=True, ids=repr)


@pytest.fixture(params=[(desktop1.width, desktop1.height), (desktop2.width, desktop2.height)],
                ids=repr)
def desktop_browser(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]


@pytest.fixture(params=[(mobile1.width, mobile1.height), (mobile2.width, mobile2.height)],
                ids=repr)
def mobile_browser(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
