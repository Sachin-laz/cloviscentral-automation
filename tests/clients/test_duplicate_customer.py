from pages.login_page import LoginPage
from pages.clients_page import ClientsPage
from utils.config_reader import ConfigReader
from testdata.client_data import ClientData


def test_duplicate_customer(page):

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

    customer1 = ClientData.valid_customer()

    while clients.verify_client_exists(customer1["client_code"]):
        customer1 = ClientData.valid_customer()

    clients.add_customer(customer1)

    assert clients.is_customer_saved_successfully()

    customer2 = ClientData.valid_customer()

    customer2["client_code"] = customer1["client_code"]

    clients.add_customer(customer2)

    assert clients.is_duplicate_client_code_displayed()
