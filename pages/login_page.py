from pages.base_page import BasePage

from locators.login_locators import LoginLocators


class LoginPage(BasePage):

    def enter_username(self, username):
        self.fill(LoginLocators.USERNAME, username)

    def enter_password(self, password):
        self.fill(LoginLocators.PASSWORD, password)

    def click_login(self):
        self.click(LoginLocators.LOGIN_BUTTON)

    def login(self, username, password):

        self.enter_username(username)

        self.enter_password(password)

        self.click_login()

    def dashboard_loaded(self):

        self.page.locator(
            LoginLocators.DASHBOARD_HEADER
        ).wait_for(state="visible", timeout=15000)

        return True
    
    def invalid_login_message_visible(self):
        locator = self.page.locator(
            LoginLocators.ERROR_MESSAGE
        )
        locator.wait_for(state="visible")
        return locator.is_visible()

    def username_validation_visible(self):

        return self.page.locator(
            LoginLocators.USERNAME_REQUIRED
        ).is_visible()
    
    def password_validation_visible(self):

        return self.page.locator(
            LoginLocators.PASSWORD_REQUIRED
        ).is_visible()
    
    def click_forgot_password(self):

        self.page.locator(
            LoginLocators.FORGOT_PASSWORD
        ).click()

    def forgot_password_page_loaded(self):

        self.page.locator(
            LoginLocators.FORGOT_PASSWORD_HEADING
        ).wait_for(
            state="visible",
            timeout=10000
        )

        return True
    
    def click_password_toggle(self):

        self.click(
            LoginLocators.PASSWORD_TOGGLE
        )


    def get_password_field_type(self):

        return self.page.locator(
            LoginLocators.PASSWORD
        ).get_attribute("type")