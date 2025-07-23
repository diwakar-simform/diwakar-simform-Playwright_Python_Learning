import time
import pytest
from playwright.sync_api import Page,expect

def test_uiValidationDynamicScript(page: Page):
    # Requirement: Add to cart Iphone x and nokia edge --> verify the cart count
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    assert "login" in page.url
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach") # here value = "teach"
    page.locator("#terms").check() # for css selectors we have locator()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click() # here name is value attribte
    page.wait_for_url("https://rahulshettyacademy.com/angularpractice/shop")
    assert "angularpractice" in page.url 
    iphoneX = page.locator("app-card").filter(has_text="iphone X")
    iphoneX.get_by_role("button").click() # add to cart button

    nokiaEdge = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaEdge.get_by_role("button").click() # add to cart button

    page.get_by_text("Checkout").click() # clicking on checkout button

    checkoutItemCount = page.locator(".col-sm-8.col-md-6")
    print("item count = ", checkoutItemCount, type(checkoutItemCount))
    # expect is only meant to work with Playwright objects like Locator, Page, or APIResponse.
    expect(checkoutItemCount).to_have_count(2) # verifying two item got added into the cart
    expect(page.get_by_text("Nokia Edge")).to_be_in_viewport()
    expect(page.get_by_text("iphone X")).to_be_in_viewport()
    time.sleep(5)

def test_newChildWindowHandle(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    assert "login" in page.url
    with page.expect_popup() as newPage_info: # expect_popup is a listener event
        page.locator(".blinkingText").click()
        newPage = newPage_info.value

    assert "documents-request" in newPage.url
    email = newPage.locator(".red a").text_content()
    print("email = ", email)
    assert "mentor@rahulshettyacademy.com" == email
    assert "mentor@rahulshettyacademy.com" == email
    time.sleep(5)


