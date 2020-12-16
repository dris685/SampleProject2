from Page.BasePage import BasePage
from Locator.DashboardLocator import DashboardLocator
from Data.DashboardData import DashboardData


class DashboardPage(BasePage):

    """Locator for Dashboard Page"""
    welcome_link = DashboardLocator.welcome_link
    """Test Data for Dashboard Page"""
    dashboard_url = DashboardData.dashboard_url
    logout_link = DashboardLocator.logout_link

    """Constructor of the page class"""
    # def __init__(self, driver):
    #     super().__init__(driver)

    def is_dashboard_url_valid(self):
        return self.isURLValid(self.dashboard_url)

    def click_welcome_link(self):
        self.click_on(self.welcome_link)

    def click_logout_link(self):
        self.click_on(self.logout_link)
