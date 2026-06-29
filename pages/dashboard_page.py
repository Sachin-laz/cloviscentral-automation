from pages.base_page import BasePage

from locators.dashboard_locators import DashboardLocators

from locators.login_locators import LoginLocators


import re

class DashBoardpage(BasePage):


    def open(self):

        self.click(
            DashboardLocators.DASHBOARD_MENU
        )
        self.page.locator(
            LoginLocators.DASHBOARD_HEADER
        ).wait_for(state="visible", timeout=15000)

    def logout(self):

        self.click(
            DashboardLocators.PROFILE_ICON
        )

        self.page.locator(
            DashboardLocators.LOGOUT_BUTTON
        ).wait_for(
            state="visible",
            timeout=5000
        )

        self.click(
            DashboardLocators.LOGOUT_BUTTON
        )

        self.page.locator(
            DashboardLocators.CONFIRM_LOGOUT
        ).wait_for(
            state="visible",
            timeout=5000
        )

        self.click(
            DashboardLocators.CONFIRM_LOGOUT
        )

        self.page.wait_for_url(
        "**/login",
        timeout=15000
    )
        
    def get_dashboard_client_count(self):

        count_locator = self.page.locator(
            DashboardLocators.CLIENT_COUNT
            )

        count_locator.wait_for(state="visible")

        for _ in range(20):

            count = count_locator.inner_text().strip()

            print("Current Value:", count)

            if count.isdigit():
                return int(count)

            self.page.wait_for_timeout(500)

        raise Exception("Customer count never loaded")