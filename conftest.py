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
class Dim:
    width: int
    height: int

    def __repr__(self):
        return f"({self.width}_{self.height})"


dim1 = Dim(width=3840, height=2160)
dim2 = Dim(width=1920, height=1080)
dim3 = Dim(width=353, height=745)
dim4 = Dim(width=414, height=896)

only_desktop = pytest.mark.parametrize("desktop_browser", [(dim1.width, dim1.height), (dim2.width, dim2.height)],
                                       indirect=True, ids=repr)
only_mobile = pytest.mark.parametrize("mobile_browser", [(dim3.width, dim3.height), (dim4.width, dim4.height)],
                                      indirect=True, ids=repr)


@pytest.fixture(params=[(dim1.width, dim1.height), (dim2.width, dim2.height)], ids=repr)
def desktop_browser(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]


@pytest.fixture(params=[(dim3.width, dim3.height), (dim4.width, dim4.height)], ids=repr)
def mobile_browser(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

@pytest.fixture(
    params=[(dim1.width, dim1.height), (dim2.width, dim2.height), (dim3.width, dim3.height), (dim4.width, dim4.height)], ids=repr)
def browser_size(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    if request.param[0] >= request.param[1]:
        return "desktop"
    else:
        return "mobile"
