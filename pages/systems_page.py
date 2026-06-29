from pages.base_page import BasePage
from locators.systems_locators import SystemsLocator

class SystemsPage(BasePage):

    def open_systems(self):
        self.click(SystemsLocator.SYSTEMS_MENU)

        self.page.wait_for_url("**/systems", timeout=10000)

        self.page.locator(
            SystemsLocator.SYSTEMS_HEADER
        ).wait_for(state="visible", timeout=15000)

        return self.is_visible(SystemsLocator.SYSTEMS_HEADER)
    
    def verify_system_tabs(self):

        return (
        self.is_visible(SystemsLocator.PENDING_TAB)
        and self.is_visible(SystemsLocator.ACTIVE_TAB)
        and self.is_visible(SystemsLocator.INACTIVE_TAB)
    )

    def click_pending_tab(self):

        with self.page.expect_response(
            lambda response:
                "systems_commission_state=PENDING" in response.url
                and response.status in [200, 304]
        ):
            self.click(SystemsLocator.PENDING_TAB)

        return True
    
    def click_active_tab(self):

        with self.page.expect_response(
            lambda response:
                "systems_commission_state=ACTIVE" in response.url
                and response.status in [200, 304]
        ):
            self.click(SystemsLocator.ACTIVE_TAB)

        return True
    

    def click_inactive_tab(self):

        with self.page.expect_response(
            lambda response:
                "systems_commission_state=INACTIVE" in response.url
                and response.status in [200, 304]
        ):
            self.click(SystemsLocator.INACTIVE_TAB)

        return True
    

    def verify_systems_table(self):

        self.wait_for_element(
            SystemsLocator.SYSTEMS_TABLE
        )

        return self.is_visible(
            SystemsLocator.SYSTEMS_TABLE
        )
    
    def verify_search_result(self, expected):

        return (
            self.get_text(
                SystemsLocator.UNIT_ID
            ) == expected
        )
    
    def clear_search(self):

        self.clear_and_fill(
            SystemsLocator.SEARCH_BOX,
            ""
        )

        return True
    
    def search_system(self, value):

        with self.page.expect_response(
            lambda response:
                f"search={value}" in response.url
                and response.status in [200, 304]
        ):
            self.fill(
                SystemsLocator.SEARCH_BOX,
                value
            )

        return True
    
    def verify_no_data_found(self):

        return self.is_visible(
            SystemsLocator.NO_DATA_FOUND
        )
    
    def click_next_page(self):

        with self.page.expect_response(
            lambda response:
                "/systems" in response.url
                and response.status in [200, 304]
        ):
            self.click(
                SystemsLocator.NEXT_BUTTON
            )

        return True
    
    def click_previous_page(self):

        old_text = self.get_text(
            SystemsLocator.PAGINATION_TEXT
        )

        with self.page.expect_response(
            lambda response:
                "/systems" in response.url
                and response.status in [200, 304]
        ):
            self.click(
                SystemsLocator.PREVIOUS_BUTTON
            )

        self.page.wait_for_function(
            f"""
            () => document.querySelector('{SystemsLocator.PAGINATION_TEXT}')?.textContent.trim() !== '{old_text}'
            """
        )

        return True
    
    def change_rows_per_page(self, value):

        with self.page.expect_response(
            lambda response:
                "/systems" in response.url
                and response.status in [200, 304]
        ):
            self.click(
                SystemsLocator.ROWS_PER_PAGE
            )

            self.click(
                f"role=option[name='{value}']"
            )

        return True
    
    def get_pagination_text(self):

        self.page.locator(
            SystemsLocator.PAGINATION_TEXT
        ).wait_for(
            state="visible",
            timeout=10000
        )

        return self.get_text(
            SystemsLocator.PAGINATION_TEXT
        )
    
    def verify_rows_per_page(self, value):

        return (
            self.get_text(
                SystemsLocator.ROWS_PER_PAGE
            ) == value
        )
    

    def wait_for_pagination_load(self):

        self.page.wait_for_function(
            f"""
            () => {{
                const text = document.querySelector('{SystemsLocator.PAGINATION_TEXT}')?.textContent?.trim() || '';
                return text !== '' && text !== '0 results';
            }}
            """
        )

        return True
    
    def select_autocomplete(self, locator, value):

        self.click(locator)

        self.fill(locator, value)

        self.click(
            f"role=option[name='{value}']"
        )

        return True
    
    def select_client(self, client):

        return self.select_autocomplete(
            SystemsLocator.CLIENT_FILTER,
            client
        )


    def select_variant(self, variant):

        return self.select_autocomplete(
            SystemsLocator.VARIANT_FILTER,
            variant
        )
    
    def verify_text_visible(self, value):

        locator = self.page.get_by_text(
            value,
            exact=True
        )

        locator.first.wait_for(
            state="visible"
        )

        return locator.first.is_visible()
    
    def verify_client_filter(self, client):

        return self.verify_text_visible(
            client
        )
    
    def verify_variant_filter(self, variant):

        return self.verify_text_visible(
            variant
        )
    
    def clear_client_filter(self):

        return self.clear_filter(
            SystemsLocator.CLIENT_FILTER
        )


    def clear_variant_filter(self):

        return self.clear_filter(
            SystemsLocator.VARIANT_FILTER
        )
    
    def clear_filter(self, locator):

        self.page.locator(locator).clear()

        self.page.keyboard.press("Tab")

        return True
    
    def open_columns(self):

        self.click(
            SystemsLocator.COLUMNS_BUTTON
        )

        return True
    
    def show_all_columns(self):

        self.click(
            SystemsLocator.SHOW_ALL_BUTTON
        )

        return True
    
    def enable_all_columns(self):

        self.click(
            SystemsLocator.COLUMNS_BUTTON
        )

        self.click(
            SystemsLocator.SHOW_ALL_BUTTON
        )

        self.page.keyboard.press("Escape")

        return True