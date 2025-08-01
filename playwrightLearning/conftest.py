from playwright.sync_api import Playwright
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )

    parser.addoption(
        "--url_name", action="store", default="https://rahulshettyacademy.com/client", help="url selection"
    )

@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param # this statement will return back to the test case and check for parameter.

@pytest.fixture
def browserInstance(playwright: Playwright, request):
    browser_name = request.config.getoption("browser_name")
    url_name = request.config.getoption("url_name")

    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)

    context = browser.new_context()
    page = context.new_page()
    # page.goto(url_name)
    yield page # this act as  a return statement
    browser.close()
    context.close()
    