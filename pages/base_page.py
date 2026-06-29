import re

class BasePage:

    def __init__(self, page):
        self.page = page

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, value):
        self.page.locator(locator).type(value, delay=100)

    def get_text(self, locator):
        return self.page.locator(locator).text_content()

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()

    def wait_for(self, locator):
        self.page.locator(locator).wait_for()

    def wait_for_element(self, locator):
        self.page.locator(locator).wait_for(
            state="visible",
            timeout=10000
        )

    def select_autocomplete(self, locator, value):

        self.click(locator)

        self.fill(locator, value)

        self.page.locator(
        "[role='option']",
        has_text=re.compile(f"^{re.escape(value)}$")
        ).first.wait_for(state="visible")

        self.page.locator(
            "[role='option']",
            has_text=re.compile(f"^{re.escape(value)}$")
        ).first.click()

    
    def clear_and_fill(self, locator, text):

        element = self.page.locator(locator)

        element.clear()

        element.type(text, delay=100)

    def get_client_row(self):

        return self.page.locator("tbody tr").first
