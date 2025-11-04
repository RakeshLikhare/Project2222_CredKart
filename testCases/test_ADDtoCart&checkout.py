import time

import pytest

from pageObjects.CredKartLogin import Test_CredKartLogin
from utilities.LoggerFile import LogGenerator
from utilities.ReadConfigFile import readconfig
from pageObjects.CredKartADDtoCartNcheckout import Test_ADDtoCartAndCheckout

class Test_AddToCartAndCheckout:
    log=LogGenerator.loggen()
    email=readconfig.read_email()
    password=readconfig.read_password()

    @pytest.mark.group2
    def test_AddToCartAndCheckout005(self,setup):
        self.log.info("test_AddToCartAndCheckout005 is start")
        self.log.info("opening the browser")
        self.browser=setup
        self.lp=Test_CredKartLogin(self.browser)
        self.log.info("click on login link text")
        self.lp.Click_login()
        self.log.info("enter email address")
        print("email is-->"+self.email)
        self.lp.Enter_email(self.email)
        self.log.info("enter password")
        print("password is-->" + self.password)
        self.lp.Enter_password(self.password)
        self.log.info("click on login button")
        self.lp.Click_loginB()
        self.pc=Test_ADDtoCartAndCheckout(self.browser)
        self.log.info("select the mack laptop as a product")
        self.pc.ProductMack()
        self.log.info("click on add to cart button")
        self.pc.AddToCart()
        self.log.info("click on continue shopping button")
        self.pc.ContinueShop()
        self.log.info("select the guitar as a product")
        self.pc.ProductGuitar()
        self.log.info("click on add to cart button")
        self.pc.AddToCart()
        self.log.info("select the mack laptop product quantity")
        self.pc.SelectQuantity()
        time.sleep(2)
        self.log.info("click on proceed and checkout button")
        self.pc.ProceedAndCheckout()
        self.log.info("entered first name")
        self.pc.EnterFirstname("Rakesh")
        self.log.info("entered last name")
        self.pc.EnterLastname("Likhare")
        self.log.info("entered mobile no")
        self.pc.EnterPhone(7768594849)
        self.log.info("entered address")
        self.pc.EnterAddress("ward n0.12 Sangitdham clony Chhindwara")
        self.log.info("entered zipcode")
        self.pc.EnterZipcode("480108")
        self.log.info("select state")
        self.pc.ClickDrop_State()
        self.log.info("entered card owner name")
        self.pc.EnterOwner("Rockey")
        self.log.info("enter card cvv")
        self.pc.EnterCVV("3234")
        self.log.info("entered card number")
        self.pc.EnterCardNo("5281")
        self.pc.EnterCardNo("0370")
        self.pc.EnterCardNo("4891")
        self.pc.EnterCardNo("6168")
        self.log.info("select card expire year")
        self.pc.ClickDrop_ExpYear()
        self.log.info("select card expire month")
        self.pc.ClickDrop_ExpMonth()
        self.log.info("click on continue and checkout button")
        self.pc.ContinueAndCheckout()
        self.log.info("validate checkout done or not")
        if self.pc.ValidatCheckout() == "Thank you.":
            self.log.info("checkout process complete successfully✅")
            self.log.info("test_AddToCartAndCheckout005 is done")
            self.log.info("test_AddToCartAndCheckout005 is end")
            assert True
        else:
            self.log.info("checkout process not done due to some exceptions😢")
            assert False









