import random
import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Profile")
class TestProfileFeature(BaseTest):

    @allure.title("Change profile name")
    @allure.severity("Critical")
    def test_change_profile_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_button()
        self.personal_page.change_name(f"Test {random.randint(1, 10)}")
        self.personal_page.save_changes()
        self.personal_page.is_changed_saved()
