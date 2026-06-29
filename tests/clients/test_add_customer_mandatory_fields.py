from pages.login_page import LoginPage
from pages.clients_page import ClientsPage
from utils.config_reader import ConfigReader


def test_add_customer_mandatory_fields(page):

    config = ConfigReader.read()

    page.goto(
        config["url"],
        wait_until="domcontentloaded",
        timeout=60000
    )

    login = LoginPage(page)

    login.login(
        config["username"],
        config["password"]
    )

    clients = ClientsPage(page)

    clients.open()

    clients.click_add_customer()

    clients.click_save()

    assert clients.is_mandatory_field_validation_displayed()
