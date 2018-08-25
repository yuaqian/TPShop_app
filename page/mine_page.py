import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class MinePage(BaseAction):
    login_sing_up_button = By.ID, "com.tpshop.malls:id/nickname_txtv"

    @allure.step(title="点击登录/注册按钮")
    def click_login_sing_up(self):
        self.click(self.login_sing_up_button)
