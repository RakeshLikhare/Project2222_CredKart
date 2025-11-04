import pytest
from selenium.webdriver.common.by import By

from pageObjects.CredKartLogin import Test_CredKartLogin

from utilities.LoggerFile import LogGenerator
from utilities.ReadConfigFile import readconfig


class Test_CredLogin_params:
    log=LogGenerator.loggen()

    @pytest.mark.regression
    @pytest.mark.group4
    def test_CredKart_Login_params_003(self,setup,GetDataForLogin):
        self.log.info("test_CredKart_Login_params_003 is start")
        self.log.info("opening the browser")
        self.browser=setup
        self.lp=Test_CredKartLogin(self.browser)
        self.lp.Click_login()
        self.log.info("email is--->"+GetDataForLogin[0])
        self.log.info("password is--->"+GetDataForLogin[1])
        self.log.info("entering the email")
        self.lp.Enter_email(GetDataForLogin[0])
        self.log.info("entering the password")
        self.lp.Enter_password(GetDataForLogin[1])
        self.log.info("click on login button")
        self.lp.Click_loginB()
        try:
            self.log.info("validate login status")
            if self.lp.validate_login() == "loginPass" and GetDataForLogin[2] == "Login_Pass":
                self.log.info("taking screenshot")
                self.browser.save_screenshot(".\\Screenshots\\test_CredKart_Login_params_003_pass.png")
                self.log.info("click on dropdown menu")
                self.lp.Menu_Button()
                self.log.info("click on logout button")
                self.lp.Click_logout()
                print("menu button is present login pass✅")
                self.log.info("test_CredKart_Login_params_003 is pass")
                assert True
            elif self.lp.validate_login() == "loginPass" and GetDataForLogin[2] == "Login_Fail":
                self.log.info("taking screenshot")
                self.browser.save_screenshot(".\\Screenshots\\test_CredKart_Login_params_003_fail.png")
                self.log.info("click on dropdown menu")
                self.lp.Menu_Button()
                self.log.info("click on logout button")
                self.lp.Click_logout()
                print("menu button is present login pass✅")
                self.log.info("test_CredKart_Login_params_003 is pass")
                assert False
            elif self.lp.validate_login() == "loginFail" and GetDataForLogin[2] == "Login_Pass":
                self.log.info("taking screenshot")
                self.browser.save_screenshot(".\\Screenshots\\test_CredKart_Login_params_003_fail.png")
                self.log.info("test_CredKart_Login_params_003 is fail")
                assert False
            elif self.lp.validate_login() == "loginFail" and GetDataForLogin[2] == "Login_Fail":
                self.log.info("taking screenshot")
                self.browser.save_screenshot(".\\Screenshots\\test_CredKart_Login_params_003_fail.png")
                print("menu button not found testcase is fail😢")
                self.log.info("test_CredKart_Login_params_003 is fail")
                assert True
        finally:
            self.log.info("test_CredKart_Login_params_003 is end")
            self.log.info("browser closed")
            self.browser.quit()


