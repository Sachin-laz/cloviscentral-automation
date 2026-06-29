from pages.clients_page import ClientsPage
from testdata.client_data import ClientData
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader


def test_edit_customer(page):

    config = ConfigReader.read()

    customer = ClientData.valid_customer()

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

    updated_customer = ClientData.updated_customer()

    clients.open()

    while clients.verify_client_exists(customer["client_code"]):
        customer = ClientData.valid_customer()

    clients.add_customer(customer)

    assert clients.is_customer_saved_successfully()

    assert clients.verify_client_exists(
        customer["client_code"]
    )

    clients.open_client(
        customer["organisation"]
    )

    clients.click_edit_client()

    clients.edit_client(
        updated_customer
    )

    assert clients.is_customer_saved_successfully()

    clients.click_edit_client_back()

    clients.search_client(
        customer["client_code"]
    )

    assert clients.verify_customer_details(
        updated_customer
    )