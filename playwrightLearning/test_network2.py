from playwright.sync_api import Page
import time

# mockrequest@gmail.com
# Mock@12345
# here you are mocking your request 
def interceptRequest(route, request):
    modified_url = "https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6880bb346f585eb60d3cabc2"
    route.continue_(url=modified_url)


# Task: is to verify in case where no order is present in the order history
def test_network1(page: Page):
    
    # Step1: Login
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    assert "login" in page.url
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", interceptRequest)
    page.get_by_placeholder("email@example.com").fill("diwakar12345@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Diwakar@123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click() # this will trigger the page.route() --> call interceptRequest order = 6880b5ce6f585eb60d3c9c5a
    message = page.locator(".blink_me").text_content()

    assert "You are not authorize to view this order" == message
    print("Message = ",message)
    time.sleep(50)

    