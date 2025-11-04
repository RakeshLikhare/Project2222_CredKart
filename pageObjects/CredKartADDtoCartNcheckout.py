import time

from selenium.webdriver.common.by import By


class Test_ADDtoCartAndCheckout:
    Click_ProductMack_Xpath=(By.XPATH,"//h3[normalize-space()='Apple Macbook Pro']")
    Click_AddToCart_Xpath=(By.XPATH,"//input[@value='Add to Cart']")
    Click_ContinueShop_Xpath=(By.XPATH,"//a[@class='btn btn-primary btn-lg']")
    Click_ProductGuitar_Xpath=(By.XPATH,"//h3[normalize-space()='Acoustic Guitar']")
    Click_ProceedAndCheckout_Xpath = (By.XPATH, "/html[1]/body[1]/div[1]/a[2]")
    ClickDrop_SelectQuantity_Xpath=(By.XPATH, "//tbody/tr[1]/td[3]/select[1]")
    Text_Firstname_Xpath = (By.XPATH, "//input[@id='first_name']")
    Text_Lastname_Xpath = (By.XPATH, "//input[@id='last_name']")
    Text_Phone_Xpath = (By.XPATH, "//input[@id='phone']")
    Text_Address_Xpath = (By.XPATH, "//textarea[@id='address']")
    Text_Zipcode_Xpath = (By.XPATH, "//input[@id='zip']")
    ClickDrop_State_Xpath = (By.XPATH, "//select[@id='state']")
    Text_owner_Xpath = (By.XPATH, "//input[@id='owner']")
    Text_CVV_Xpath= (By.XPATH, "//input[@id='cvv']")
    Text_CardNo_Xpath = (By.XPATH, "//input[@id='cardNumber']")
    ClickDrop_ExpYear_Xpath = (By.XPATH, "//select[@id='exp_year']")
    ClickDrop_ExpMonth_Xpath = (By.XPATH, "//select[@id='exp_month']")
    Click_ContinueAndCheckout_Xpath = (By.XPATH, "//button[@id='confirm-purchase']")

    def __init__(self,driver):
        self.driver=driver

    def ProductMack(self):
        self.driver.find_element(*Test_ADDtoCartAndCheckout.Click_ProductMack_Xpath).click()

    def AddToCart(self):
        self.driver.find_element(*Test_ADDtoCartAndCheckout.Click_AddToCart_Xpath).click()

    def ContinueShop(self):
        self.driver.find_element(*Test_ADDtoCartAndCheckout.Click_ContinueShop_Xpath).click()

    def ProductGuitar(self):
        self.driver.find_element(*Test_ADDtoCartAndCheckout.Click_ProductGuitar_Xpath).click()

    def ProceedAndCheckout(self):
        self.driver.find_element(*Test_ADDtoCartAndCheckout.Click_ProceedAndCheckout_Xpath).click()

    def SelectQuantity(self):
        self.driver.find_element(*Test_ADDtoCartAndCheckout.ClickDrop_SelectQuantity_Xpath).send_keys(2)

    def EnterFirstname(self,firstname):
        self.driver.find_element(*Test_ADDtoCartAndCheckout.Text_Firstname_Xpath).send_keys(firstname)

    def EnterLastname(self,lastname):
        self.driver.find_element(*Test_ADDtoCartAndCheckout.Text_Lastname_Xpath).send_keys(lastname)

    def EnterPhone(self,phone):
        self.driver.find_element(*Test_ADDtoCartAndCheckout.Text_Phone_Xpath).send_keys(phone)

    def EnterAddress(self,address):
        self.driver.find_element(*Test_ADDtoCartAndCheckout.Text_Address_Xpath).send_keys(address)

    def EnterZipcode(self,zip):
        self.driver.find_element(*Test_ADDtoCartAndCheckout.Text_Zipcode_Xpath).send_keys(zip)

    def ClickDrop_State(self):
        self.driver.find_element(*Test_ADDtoCartAndCheckout.ClickDrop_State_Xpath).send_keys("pune")

    def EnterOwner(self,owner):
        self.driver.find_element(*Test_ADDtoCartAndCheckout.Text_owner_Xpath).send_keys(owner)

    def EnterCVV(self,cvv):
        self.driver.find_element(*Test_ADDtoCartAndCheckout.Text_CVV_Xpath).send_keys(cvv)

    def EnterCardNo(self,cardNo):
        self.driver.find_element(*Test_ADDtoCartAndCheckout.Text_CardNo_Xpath).send_keys(cardNo)

    def ClickDrop_ExpYear(self):
        self.driver.find_element(*Test_ADDtoCartAndCheckout.ClickDrop_ExpYear_Xpath).send_keys(2020)

    def ClickDrop_ExpMonth(self):
        self.driver.find_element(*Test_ADDtoCartAndCheckout.ClickDrop_ExpMonth_Xpath).send_keys("May")

    def ContinueAndCheckout(self):
        self.driver.find_element(*Test_ADDtoCartAndCheckout.Click_ContinueAndCheckout_Xpath).click()


    def ValidatCheckout(self):
        try:
            Thanks_Msg=self.driver.find_element(By.XPATH,"//h1[normalize-space()='Thank you.']").text
            print("Checkout done✅ with all the process")
            return Thanks_Msg
        except:
            print("Uff checkout process is not complete😢")













