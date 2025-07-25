from .orderDetails import OrderDetailsPage


class OrdersHistoryPage:

    def __init__(self, page):
        self.page = page

    def selectOrder(self, orderId):
        orderRow = self.page.locator("tr").filter(has_text=orderId)
        orderRow.get_by_role("button", name="View").click()
        orderDetailsPage = OrderDetailsPage(self.page)
        return orderDetailsPage
