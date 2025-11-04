import pytest
from selenium.webdriver.common.by import By

from pageObjects.CredKartLogin import Test_CredKartLogin
from utilities.LoggerFile import LogGenerator
from utilities.ReadConfigFile import readconfig


class Test_CredLogin:
    email=readconfig.read_email()
    password=readconfig.read_password()
    log=LogGenerator.loggen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_CredKart_url_001(self,setup):
        # self.log.debug("this is debug")
        # self.log.info("this is info")
        # self.log.warning("this is warning")
        # self.log.error("this is error")
        # self.log.critical("this is critical")

        self.log.info("test_CredKart_url_001 is start")
        self.log.info("opening the browser")
        self.browser=setup
        self.log.info("captured the page title")
        if self.browser.title == 'CredKart':
            self.log.info("taking screenshot")
            self.browser.save_screenshot(".\\Screenshots\\test_CredKart_url_001_pass.png")
            self.log.info("test_CredKart_url_001 is pass")
            assert True
        else:
            self.log.info("taking screenshot")
            self.browser.save_screenshot(".\\Screenshots\\test_CredKart_url_001_pass.png")
            self.log.info("test_CredKart_url_001 is fail")
            assert False
        self.log.info("test_CredKart_url_001 is end")
        self.log.info("browser closed")
        self.browser.quit()

    @pytest.mark.group1
    @pytest.mark.sanity
    def test_CredKart_Login_002(self,setup):
        self.log.info("test_CredKart_Login_002 is start")
        self.log.info("opening the browser")
        self.browser=setup
        self.lp=Test_CredKartLogin(self.browser)
        self.lp.Click_login()
        print("email is--->"+self.email)
        print("password is--->"+self.password)
        self.log.info("entering the email")
        self.lp.Enter_email(self.email)
        self.log.info("entering the password")
        self.lp.Enter_password(self.password)
        self.log.info("click on login button")
        self.lp.Click_loginB()
        try:
            self.log.info("validate login status")
            if self.lp.validate_login() == "loginPass":
                self.log.info("taking screenshot")
                self.browser.save_screenshot(".\\Screenshots\\test_CredKart_Login_002_pass.png")
                self.log.info("click on dropdown menu")
                self.lp.Menu_Button()
                self.log.info("click on logout button")
                self.lp.Click_logout()
                print("menu button is present login pass✅")
                self.log.info("test_CredKart_Login_002 is pass")
                assert True
            else:
                self.log.info("taking screenshot")
                self.browser.save_screenshot(".\\Screenshots\\test_CredKart_Login_002_fail.png")
                print("menu button not found testcase is fail😢")
                self.log.info("test_CredKart_Login_002 is pass")
                assert False
        finally:
            self.log.info("test_CredKart_Login_002 is end")
            self.log.info("browser closed")
            self.browser.quit()


