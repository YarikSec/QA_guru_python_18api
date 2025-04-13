import pytest
from selene import browser
from utils.attach import add_screenshot, add_logs, add_html, add_video


@pytest.fixture(scope='function', autouse=True)
def browser_conf():
    # browser.config.base_url = 'https://demowebshop.tricentis.com/'
    # browser.config.type_by_js = True

    # browser.config.hold_browser_open = True
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    add_screenshot(browser)
    add_logs(browser)
    add_html(browser)
    add_video(browser)

    browser.quit()