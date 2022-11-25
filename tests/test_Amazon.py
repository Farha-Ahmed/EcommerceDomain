import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass
from pageObject.HomePage import HomePage


class TestHomePageAmazon(BaseClass):

    @pytest.fixture(params=HomePageData.getTestData("TestCase2"))
    def getData(self,request):
        return request.param

    def test_Amazon(self,getData):
     log = self.getLogger()


     Home = HomePage(self.driver)
     self.driver.implicitly_wait(30)

     # enter text in search field
     # driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
     Home.searchbar().clear()
     log.info("Laptop is"+getData["search"])
     Home.searchbar().send_keys(getData["search"])
     log.info("sending the dell laptops text in the search bar")


     # click on search icon
     # driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']")
     Home.submitbutton().click()
     log.info("click on the search icon")

     # Laptop should be delivered next day
     # driver.find_elements(By.XPATH, "//li[@id='p_90/6741118031']//i[@class='a-icon a-icon-checkbox']")
     Home.deliveryfilter().click()
     log.info("Laptop should be delivered next day")

     #assertion for delivery day
     actDelivery = Home.deliveryassertion().text
     expDelivery = 'Get It by Tomorrow'
     if expDelivery == actDelivery:
         assert True
     else:
         self.driver.save_screenshot(".\\Screenshots\\" + "test_Amazon.png")  # screenshot
         assert False

     # price should be in between 40000 to 50000
     # driver.find_element(By.XPATH, "//span[contains(text(),'₹40,000 – ₹50,000')]")
     Home.pricefilter().click()
     log.info("select the range 40000 to 50000")

     # assertion for price
     actPrice = Home.priceassertion().text
     expPrice = '₹40,000 – ₹50,000'
     if expPrice == actPrice:
         assert True
     else:
         self.driver.save_screenshot(".\\Screenshots\\"+"test_Amazon.png")
         assert False


     # CPU manufacturer should be intel
     # driver.find_element(By.XPATH, "//body")
     Home.CPUfilter().click()
     log.info("CPU manufacturer should be intel")

     # Operating system should be window 10 home
     # driver.find_element(By.XPATH, "(//i[@class='a-icon a-icon-checkbox'])[25]")
     Home.systemfilter().click()
     log.info("select window 10 home")

     #assertion 1
     #actTitle = Home.titleassertion().text
     #expTitle = "Amazon.in"
     #if expTitle == actTitle:
         #assert True
     #else:
         #self.driver.save_screenshot(".\\Screenshots\\"+"test_amazon.png") #screenshot
         #assert False








