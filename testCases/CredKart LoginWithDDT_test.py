import time

import pytest
from selenium.webdriver.common.by import By

from pageObjects.CredKartLogin import Test_CredKartLogin
from utilities.LoggerFile import LogGenerator
from utilities import Excel_utils
from utilities.ReadConfigFile import readconfig


class Test_CredLogin_DDT:
    log=LogGenerator.loggen()
    file_path="testCases\\Test_Data\\Test_Data2.xlsx"

    @pytest.mark.group9
    def test_CredKart_Login_DDT_004(self,setup):
        self.log.info("test_CredKart_Login_DDT_004 is start")
        self.log.info("opening the browser")
        self.browser=setup
        list_status=[]
        self.lp=Test_CredKartLogin(self.browser)
        self.row=Excel_utils.GetRowCount(self.file_path,"login_data")
        self.log.info("row count is-->" + str(self.row))
        print("rowcount in our excel file--->"+str(self.row))
        for r in range(2,self.row+1):
            self.log.info("for loop is start with"+' '+str(r)+"nd row credential")
            self.email=Excel_utils.read_data(self.file_path,"login_data",r,2)
            self.password=Excel_utils.read_data(self.file_path,"login_data",r,3)
            self.Expected_result=Excel_utils.read_data(self.file_path,"login_data",r,4)
            # print("email is---->"+self.email)
            # print("password is---->" +self.password)
            # print("Expected_result is---->"+self.Expected_result
            self.lp.Click_login()
            self.log.info("email is--->"+str(self.email))
            self.log.info("password is--->"+str(self.password))
            self.log.info("entering the email")
            self.lp.Enter_email(self.email)
            self.log.info("entering the password")
            self.lp.Enter_password(self.password)
            self.log.info("click on login button")
            self.lp.Click_loginB()
            self.log.info("validate login status")
            if self.lp.validate_login() == "loginPass" and self.Expected_result == "Login_Pass":
                list_status.append("Pass")
                Excel_utils.write_data(self.file_path, "login_data", r, 5, "Pass")
                self.log.info("taking screenshot")
                self.browser.save_screenshot(".\\Screenshots\\test_CredKart_Login_DDT_004_pass.png")
                self.log.info("click on dropdown menu")
                self.lp.Menu_Button()
                self.log.info("click on logout button")
                self.lp.Click_logout()
            elif self.lp.validate_login() == "loginPass" and self.Expected_result == "Login_Fail":
                list_status.append("Fail")
                Excel_utils.write_data(self.file_path, "login_data", r, 5, "Fail")
                self.log.info("taking screenshot")
                self.browser.save_screenshot(".\\Screenshots\\test_CredKart_Login_DDT_004_fail.png")
                self.log.info("click on dropdown menu")
                self.lp.Menu_Button()
                self.log.info("click on logout button")
                self.lp.Click_logout()
            elif self.lp.validate_login() == "loginFail" and self.Expected_result == "Login_Pass":
                list_status.append("Fail")
                Excel_utils.write_data(self.file_path, "login_data", r, 5, "Fail")
                self.log.info("taking screenshot")
                self.browser.save_screenshot(".\\Screenshots\\test_CredKart_Login_DDT_004_fail.png")
            elif self.lp.validate_login() == "loginFail" and self.Expected_result == "Login_Fail":
                list_status.append("Pass")
                Excel_utils.write_data(self.file_path, "login_data", r, 5, "Pass")
                self.log.info("taking screenshot")
                self.browser.save_screenshot(".\\Screenshots\\test_CredKart_Login_DDT_004_fail.png")
        print(list_status)
        if "Fail" not in list_status:
            print("menu button is present login pass✅")
            self.log.info("test_CredKart_Login_DDT_004 is pass")
            self.log.info("test_CredKart_Login_DDT_004 is end")
            self.log.info("browser closed")
            assert True
        else:
            print("menu button not found testcase is fail😢")
            self.log.info("test_CredKart_Login_DDT_004 is fail")
            self.log.info("test_CredKart_Login_DDT_004 is end")
            self.log.info("browser closed")
            assert False