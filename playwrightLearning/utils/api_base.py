from playwright.sync_api import Playwright

orderPayload = orderPayload = {
    "orders": [
        {
            "country": "British Indian Ocean Territory",
            "productOrderedId": "67a8dde5c0d3e6622a297cc8"
        }
    ]
}

class APIUtils:

    def getToken(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post(url="/api/ecom/auth/login",
                                 data = {"userEmail": "diwakar12345@gmail.com", "userPassword": "Diwakar@123"})
        assert response.ok
        print(response.json)
        responseBody = response.json()
        return responseBody["token"]

    def create_order(self, playwright: Playwright):
        token = self.getToken(playwright)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                 data = orderPayload,
                                 headers={"authorization": token, 
                                          "content-type": "application/json"}
                                )
        print(response.json())

        response_body = response.json()
        orderId = response_body["orders"][0]
        return orderId

