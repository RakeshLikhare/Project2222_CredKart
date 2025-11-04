from selenium.webdriver.common.by import By


class Test_CredKartLogin:
    Click_login_Xpath = (By.XPATH,"//a[normalize-space()='Login']")
    Text_email_Xpath = (By.XPATH,"//input[@id='email']")
    Text_password_Xpath = (By.XPATH,"//input[@id='password']")
    Click_loginB_Xpath = (By.XPATH,"//button[@type='submit']")
    Click_menu_Xpath = (By.XPATH,"//a[@role='button']")
    Click_logout_Xpath=(By.XPATH,"//a[normalize-space()='Logout']")


    def __init__(self,driver):
        self.browser=driver

    def Click_login(self):
        self.browser.find_element(*Test_CredKartLogin.Click_login_Xpath).click()

    def Enter_email(self,email):
        self.browser.find_element(*Test_CredKartLogin.Text_email_Xpath).send_keys(email)

    def Enter_password(self,password):
        self.browser.find_element(*Test_CredKartLogin.Text_password_Xpath).send_keys(password)

    def Click_loginB(self):
        self.browser.find_element(*Test_CredKartLogin.Click_loginB_Xpath).click()

    def Menu_Button(self):
        self.browser.find_element(*Test_CredKartLogin.Click_menu_Xpath).click()

    def Click_logout(self):
        self.browser.find_element(*Test_CredKartLogin.Click_logout_Xpath).click()

    def validate_login(self):
        try:
            self.browser.find_element(*Test_CredKartLogin.Click_menu_Xpath)
            print('CredKart login is pass✅')
            return "loginPass"
        except:
            print('CredKart login is fail😢')
            return "loginFail"
