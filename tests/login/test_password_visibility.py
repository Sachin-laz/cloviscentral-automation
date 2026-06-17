from pages.login_page import LoginPage
from utils.config_reader import ConfigReader


def test_password_visibility(page):

    config = ConfigReader.read()

    page.goto(
        config["url"],
        wait_until="domcontentloaded",
        timeout=60000
    )

    login = LoginPage(page)

    login.enter_password("Admin123")

    # Hidden initially
    assert (
        login.get_password_field_type()
        == "password"
    )

    # Show password
    login.click_password_toggle()

    assert (
        login.get_password_field_type()
        == "text"
    )

    # Hide password again
    login.click_password_toggle()

    assert (
        login.get_password_field_type()
        == "password"
    )