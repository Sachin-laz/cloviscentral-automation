from pages.login_page import LoginPage
from utils.config_reader import ConfigReader


def test_forgot_password(page):

    config = ConfigReader.read()

    page.goto(
        config["url"],
        wait_until="domcontentloaded",
        timeout=60000
    )

    login = LoginPage(page)

    login.click_forgot_password()

    page.wait_for_timeout(3000)

    print("URL:", page.url)

    assert "forgot-password" in page.url

    assert login.forgot_password_page_loaded()