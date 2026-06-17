from pages.login_page import LoginPage
from pages.dashboard_page import DashBoardpage
from utils.config_reader import ConfigReader
from locators.login_locators import LoginLocators



def test_logout(page):

    config = ConfigReader.read()

    page.goto(
        config["url"],
        wait_until="domcontentloaded",
        timeout=30000
    )

    login = LoginPage(page)

    login.login(
        config["username"],
        config["password"]
    )

    dashboard = DashBoardpage(page)

    dashboard.logout()

    assert page.locator(
        LoginLocators.LOGIN_BUTTON
    ).is_visible()