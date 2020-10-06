from Page.BasePage import BasePage
from Locator.DashboardLocator import DashboardLocator


class DashboardPage(BasePage):

    """Locator for Dashboard Page"""
    welcome_link = DashboardLocator.welcome_link
    """Test Data for Dashboard Page"""
    logout_link = DashboardLocator.logout_link

    """Constructor of the page class"""
    # def __init__(self, driver):
    #     super().__init__(driver)

    def click_welcome_link(self):
        self.click_on(self.welcome_link)

    def click_logout_link(self):
        self.click_on(self.logout_link)
