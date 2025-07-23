import time
from playwright.sync_api import Page, expect, Playwright
import pytest # importing for auto suggestions and type hints for the page fixture object

def test_playwrightbasics(playwright): # playwright fixture is automatically provided by pytest-playwright
    # Step1: Launch Chromium browser in non-headless mode, but in real time we run it in headless mode because it is faster execution. By default, it is headless mode.
    browser = playwright.chromium.launch(headless=False) 
    # Step2: Create a new browser context: this is like a new incognito window
    # where you can have separate sessions, cookies, etc.
    context = browser.new_context()
    # Step3: Open a new page in the browser context: this is like opening a new tab
    page = context.new_page()
    # Step4: Navigate to the specified URL: you can change this URL to any website you want to test
    page.goto("https://www.google.com")
    # Step5: Take a screenshot of the page
    page.screenshot(path="screenshot.png")
    # Step6: Close the browser context
    context.close()
    # Step7: Close the browser
    browser.close()


# page fixture is automatically provided by pytest-playwright, runs in chromium headless mode, 1 single context
def test_playwrightshortcut(page:Page):
    # Step1: Navigate to the specified URL
    page.goto("https://www.dev.fishertms.com/login") 
    # Verify the title of the page
    assert page.title() == "fishershipping"
    # Step2: Take a screenshot of the page
    page.screenshot(path="screenshot_shortcut.png")
    # Step3: Close the page
    page.close()
    
    # Note: The page.close() is optional here as the context will be closed automatically after the test is done.
    # However, it is a good practice to close the page explicitly if you are done with it to free up resources.
    # Note: The page.goto() method is a shortcut for page.navigate() and page.wait_for_load_state('load').
    # It automatically waits for the page to load before taking the screenshot
    # and it is more convenient to use in most cases.
    # Note: The page.screenshot() method takes a screenshot of the current page and saves it to the specified path.
    # You can also specify additional options like full_page=True to capture the entire page,
    # or clip to capture a specific region of the page. 

def test_coreLocators(page: Page):
    page.goto("https://www.dev.fishertms.com/login")
    page.get_by_label("User Name").fill("diwakar123")  
    page.get_by_label("Password").fill("123456")
    page.get_by_role("button").click()
    time.sleep(5)

# css selectors: #id .class tagname
def test_corelocatorsPractice(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach") # here value = "teach"
    page.locator("#terms").check() # for css selectors we have locator()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click() # here name is value attribte 
    time.sleep(5)

def test_toastMessage(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning1111")
    page.get_by_role("combobox").select_option("teach") # here value = "teach"
    page.locator("#terms").check() # for css selectors we have locator()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click() # here name is value attribte 
    # Verifying/assertion error message: Incorrect username/password.
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(5)

def test_toastMessageInFirefox(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    # context = firefoxBrowser.new_context() # if you have only single page you can skip this step
    page = firefoxBrowser.new_page()
    
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning1111")
    page.get_by_role("combobox").select_option("teach") # here value = "teach"
    page.locator("#terms").check() # for css selectors we have locator()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click() # here name is value attribte 
    # Verifying/assertion error message: Incorrect username/password.
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(5)


@pytest.mark.skip
def test_getByLabellimitation(page: Page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.get_by_label("userEmail").fill("diwakar@gmail.com")
    time.sleep(5)
