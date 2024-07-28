from src.pom.LoginPage import LoginPage
from src.pom.ClientsPage import ClientPage
from src.pom.NewClientPage import NewClientPage
from tests.ui import TestData
from src.common.Logger import logger
import pytest


@pytest.mark.usefixtures("setup")
class TestAdvisorPage:
    @pytest.mark.uiTests
    def test_create_new_client(self):
        logger.info("Initializing the login page object")
        login_page = LoginPage(self.page)

        logger.info("Entering username and password")
        login_page.enter_username(TestData.USER_NAME)
        login_page.enter_password(TestData.PASSWORD)

        logger.info("Clicking the login button")
        login_page.click_login()

        # Wait for the firm selection dropdown to appear, indicating that login was successful
        self.page.wait_for_selector(login_page.org_select)

        logger.info(f"Selecting the firm: {TestData.FIRM}")
        login_page.select_firm(TestData.FIRM)
        logger.info("Clicking the login button after selecting the firm")
        login_page.click_login()

        logger.info("Initializing the clients page object")
        clients_page = ClientPage(self.page)

        # Wait for an element unique to the clients page to appear
        self.page.wait_for_selector(clients_page.advisors)

        logger.info("Clicking the add new client button")
        clients_page.add_new_client()

        logger.info("Initializing the new client page object")
        new_client_page = NewClientPage(self.page)

        # Wait for an element unique to the new client page to appear
        self.page.wait_for_selector(new_client_page.title)

        logger.info("Verifying that the new client page is loaded")
        assert new_client_page.is_page_loaded(), (f"new client page doesn't appear, "
                                                  f"please check if locators or url needs to be modified")
        logger.info("New client page loaded successfully.")
