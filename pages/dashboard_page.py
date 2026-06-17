from pages.base_page import BasePage

from locators.dashboard_locators import DashboardLocators

class DashBoardpage(BasePage):

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