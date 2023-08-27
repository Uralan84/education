import pytest
from config.data import Data
from pages.login_page import LoginPage
from pages.personal_page import PersonalPage
from pages.dashboard_page import DashboardPage


class BaseTest:
    login_page: LoginPage
    personal_page: PersonalPage
    dashboard_page: DashboardPage
    data: Data

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.login_page = LoginPage(driver)
        request.cls.personal_page = PersonalPage(driver)
        request.cls.dashboard_page = DashboardPage(driver)
        request.cls.data = Data()
