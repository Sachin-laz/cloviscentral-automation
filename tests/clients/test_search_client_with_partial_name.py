from pages.login_page import LoginPage
from pages.clients_page import ClientsPage
from utils.config_reader import ConfigReader
from testdata.client_data import ClientData



def test_search_client_partial_name(page):

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

    customer = ClientData.valid_customer()

    clients.open()

    partial_name = customer["organisation"].split("_")[1]

    while clients.verify_client_exists(partial_name):
        customer = ClientData.valid_customer()

    clients.add_customer(customer)

    assert clients.is_customer_saved_successfully()

    clients.search_client(partial_name)

    assert clients.verify_client_name_exists(
        customer["organisation"]
    )