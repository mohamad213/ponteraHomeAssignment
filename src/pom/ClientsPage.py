from playwright.sync_api import Page
from . import ClientsPageLocators


class ClientPage:
    def __init__(self, page: Page):
        self.page = page
        self.advisors = ClientsPageLocators.ADVISORS
        self.add_new_client_button = ClientsPageLocators.ADD_NEW_CLIENT

    def add_new_client(self):
        self.page.click(self.add_new_client_button)
