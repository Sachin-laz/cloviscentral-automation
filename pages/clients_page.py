from pages.base_page import BasePage
from locators.clients_locators import ClientsLocators
import re


class ClientsPage(BasePage):

    def open(self):

        self.click(
            ClientsLocators.CLIENTS_MENU
        )

        self.page.wait_for_url(
            "**/customers",
            timeout=10000
        )

        self.page.locator(
            ClientsLocators.CLIENT_HEADER
        ).wait_for(state="visible", timeout=15000)

        return True

    def get_current_page_client_count(self):

        self.page.locator("tbody").wait_for(state="visible")

        rows = self.page.locator(
            ClientsLocators.CLIENT_ROWS
        )

        print("Row Count:", rows.count())

        return rows.count()
    
    def go_to_next_page(self):

        self.click(
            ClientsLocators.NEXT_BUTTON
        )
        self.page.wait_for_load_state("networkidle")

    def is_next_page_available(self):

        next_btn = self.page.locator(ClientsLocators.NEXT_BUTTON)

        print("Enabled:", next_btn.is_enabled())
        print("Disabled attribute:", next_btn.get_attribute("disabled"))

        return next_btn.is_enabled()
    
    def get_client_count(self):

        total = 0

        while True:

            current = self.get_current_page_client_count()

            print(f"Current Page Count: {current}")

            total += current

            if not self.is_next_page_available():
                break

            self.go_to_next_page()

        print(f"Total Client Count: {total}")

        return total


    def enter_organisation_name(self, organisation):

        self.fill(
            ClientsLocators.ORGANISATION_NAME,
            organisation
        )

    def select_country(self, country):

        self.select_autocomplete(
            ClientsLocators.COUNTRY,
            country
        )

    def select_state(self, state):

        self.select_autocomplete(
            ClientsLocators.STATE,
            state
        )

    def select_city(self, city):

        self.select_autocomplete(
            ClientsLocators.CITY,
            city
        )    

    def enter_address(self, address):

        self.fill(
            ClientsLocators.ADDRESS,
            address
        )

    def enter_contact(self, contact):

        self.fill(
            ClientsLocators.CUSTOMER_CONTACT,
            contact
        )

    def enter_email(self, email):

        self.fill(
            ClientsLocators.EMAIL,
            email
        )

    def enter_client_code(self, client_code):
        self.fill(
            ClientsLocators.CLIENT_CODE,
            client_code
        )

    def enter_school_district(self, school_district):
        self.fill(
            ClientsLocators.SCHOOL_DISTRICT,
            school_district
        )

    def enter_district_prefix(self, district_prefix):
        self.fill(
            ClientsLocators.DISTRICT_PREFIX,
            district_prefix
        )

    def enter_phone(self, phone):

        self.fill(
            ClientsLocators.PHONE,
            phone
        )
    
    def click_save(self):

        self.click(
            ClientsLocators.SAVE_BUTTON
        )

    def click_cancel(self):

        self.click(
        ClientsLocators.CANCEL_BUTTON
        )

    def click_add_customer(self):

        self.click(
            ClientsLocators.ADD_CUSTOMER_BUTTON
        )

        self.page.locator(
            ClientsLocators.ADD_CUSTOMER_DIALOG
        ).wait_for(
            state="visible",
            timeout=10000
        )
    
    def is_add_customer_dialog_open(self):

        return self.page.locator(
            ClientsLocators.ADD_CUSTOMER_DIALOG
        ).is_visible()
    
    def is_add_customer_dialog_closed(self):

        self.page.locator(
        ClientsLocators.ADD_CUSTOMER_DIALOG
        ).wait_for(state="hidden")

    def is_mandatory_field_validation_displayed(self):

        validations = [
            ClientsLocators.ORGANISATION_NAME_REQUIRED,
            ClientsLocators.COUNTRY_REQUIRED,
            ClientsLocators.CLIENT_CODE_REQUIRED,
            ClientsLocators.STATE_REQUIRED,
            ClientsLocators.CITY_REQUIRED,
            ClientsLocators.CUSTOMER_CONTACT_REQUIRED,
            ClientsLocators.EMAIL_REQUIRED,
            ClientsLocators.PHONE_REQUIRED,
        ]

        for locator in validations:
            if not self.page.locator(locator).is_visible():
                return False

        return True
    
    def is_customer_saved_successfully(self):

        self.page.locator(
            ClientsLocators.CUSTOMER_SAVE_SUCCESS_MESSAGE
            ).wait_for(state="visible")

        assert self.get_text(
                ClientsLocators.CUSTOMER_SAVE_SUCCESS_MESSAGE
                ) == "Successfully saved!"
        
        return True

    def add_customer(self, customer):

        self.click_add_customer()

        self.enter_organisation_name(
            customer["organisation"]
        )
        
        self.enter_client_code(
            customer["client_code"]
            )
        
        
        self.enter_school_district(
            customer["school_district"]
            )
        
        self.enter_district_prefix(
            customer["district_prefix"]
            )

        self.select_country(
            customer["country"]
        )

        self.select_state(
            customer["state"]
        )

        self.select_city(
            customer["city"]
        )

        self.enter_address(
            customer["address"]
        )

        self.enter_contact(
            customer["contact"]
        )

        self.enter_email(
            customer["email"]
        )

        self.enter_phone(
            customer["phone"]
        )

        self.click_save()

        self.page.wait_for_timeout(5000)

    def verify_client_exists(self, customer_name):

        self.search_client(customer_name)

        return self.page.get_by_text(
            customer_name,
            exact=True
            ).is_visible()
    
    def search_client(self, client_code):

        self.clear_and_fill(
            ClientsLocators.SEARCH_CLIENT,
            client_code
        )

        self.page.wait_for_timeout(1000)

    def is_duplicate_client_code_displayed(self):

        locator = self.page.locator(
            ClientsLocators.CLIENT_CODE_UNIQUE_MESSAGE
        )

        locator.wait_for(state="visible")

        return (
            self.get_text(
                ClientsLocators.CLIENT_CODE_UNIQUE_MESSAGE
            ) == "code must be unique"
        )
    
    def click_yes(self):

        self.click(
            ClientsLocators.YES_BUTTON
        )

        print("Clicked Yes")


    def open_client(self, client_name):

        self.page.get_by_text(
            client_name,
            exact=True
        ).click()

        self.page.wait_for_url(
            "**/customers/*"
        )

        self.page.locator(
            ClientsLocators.EDIT_CLIENT_BUTTON
        ).wait_for(state="visible")

    def click_edit_client(self):

        self.click(
            ClientsLocators.EDIT_CLIENT_BUTTON
        )

    def edit_client(self, customer):

        self.clear_and_fill(
            ClientsLocators.CUSTOMER_CONTACT,
            customer["contact"]
        )

        self.clear_and_fill(
            ClientsLocators.PHONE,
            customer["phone"]
        )

        self.clear_and_fill(
            ClientsLocators.EMAIL,
            customer["email"]
        )

        self.click_save()
    
    def click_edit_client_back(self):

        self.click(
            ClientsLocators.EDIT_BACK_BUTTON
        )

    def verify_customer_details(self, customer):

        row = self.get_client_row()

        return (

            row.get_by_text(
                customer["contact"],
                exact=True
            ).is_visible()

            and

            row.get_by_text(
                customer["email"],
                exact=False
            ).is_visible()

            and

            row.get_by_text(
                customer["phone"],
                exact=True
            ).is_visible()

        )
    
    def click_more_actions(self):

        row = self.page.locator("tbody tr").first

        row.locator(
            "[data-testid='MoreHorizIcon']"
        ).click()

    def click_delete(self):

        self.click(
            ClientsLocators.DELETE_BUTTON
        )

    def confirm_delete(self):

        self.click(
            ClientsLocators.DELETE_CONFIRM_BUTTON
        )
    def is_delete_dialog_visible(self):

        return self.page.locator(
            ClientsLocators.DELETE_CONFIRMATION_DIALOG
        ).is_visible()
    
    def is_customer_deleted_successfully(self):

        self.page.locator(
            ClientsLocators.CUSTOMER_DELETE_SUCCESS_MESSAGE
            ).wait_for(state="visible")

        assert self.get_text(
                ClientsLocators.CUSTOMER_DELETE_SUCCESS_MESSAGE
                ) == "Successfully deleted!"
        
        return True
    
    def verify_client_name_exists(self, organisation):

        row = self.page.locator("tbody tr").first

        return row.get_by_text(
            organisation,
            exact=True
        ).is_visible()
    
    def is_no_data_found_displayed(self):

        self.page.locator(
            ClientsLocators.NO_DATA_FOUND
        ).wait_for(state="visible")

        return (
            self.get_text(
                ClientsLocators.NO_DATA_FOUND
            ) == "No Data Found"
        )
    
    def clear_search(self):

        self.clear_and_fill(
            ClientsLocators.SEARCH_CLIENT,
            ""
        )

    def is_search_box_empty(self):

        return (
            self.page.locator(
                ClientsLocators.SEARCH_CLIENT
            ).input_value() == ""
        )
    
    def get_total_customer_count(self):

        text = self.get_text(
            ClientsLocators.PAGINATION_COUNT
        )

        return int(
            re.search(
                r"of\s+(\d+)",
                text
            ).group(1)
        )