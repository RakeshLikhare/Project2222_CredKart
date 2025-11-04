import pytest
from selenium import webdriver

chrome_options=webdriver.ChromeOptions()           ##ratta mar lo ye headless ke liye code
chrome_options.add_argument("headless")

##we need to add comand linear(--browser)
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture
def setup(request):
    ##then we have to give a value
    browser=request.config.getoption("--browser")    ##browser name ke variable ko value diya ye --browser
    if browser=="chrome":
        print('browser run in chrome')
        driver=webdriver.Chrome()

    elif browser=="edge":
        print("browser run in edge")
        driver=webdriver.Edge()

    elif browser == "firefox":
        print("browser run in firefox")
        driver = webdriver.Firefox()

    else:
        print("headless browser")
        driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://automation.credence.in/shop")
    driver.maximize_window()
    yield driver
    driver.quit()



@pytest.fixture(params=[

    ("rakeshlikhare@gmail.com","xcM8c6xQvya@VYg","Login_Pass"),
    ("rakeshlikhare@gmail.com1","xcM8c6xQvya@VYg","Login_Fail"),
    ("rakeshlikhare@gmail.com","xcM8c6xQvya@VYg1","Login_Fail"),
    ("rakeshlikhare@gmail.com1","xcM8c6xQvya@VYg1","Login_Fail")

])
def GetDataForLogin(request):
    return request.param

