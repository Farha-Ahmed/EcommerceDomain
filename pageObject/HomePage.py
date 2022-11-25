from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver):
        self.driver = driver

    #enter text in search field
    #driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
    search = (By.XPATH, "//input[@id='twotabsearchtextbox']")
    def searchbar(self):
        return self.driver.find_element(*HomePage.search)

    #click on search icon
    #driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']")
    submit = (By.XPATH, "//input[@id='nav-search-submit-button']")
    def submitbutton(self):
        return self.driver.find_element(*HomePage.submit)

    #Laptop should be delivered next day
    #driver.find_elements(By.XPATH, "//li[@id='p_90/6741118031']//i[@class='a-icon a-icon-checkbox']")
    deliveryday = (By.XPATH, "//li[@id='p_90/6741118031']//i[@class='a-icon a-icon-checkbox']")
    def deliveryfilter(self):
        return self.driver.find_element(*HomePage.deliveryday)

    #Assertion for delivery
    #(By.XPATH, "//span[contains(text(),'Get It by Tomorrow')]")
    actDelivery = (By.XPATH, "//span[contains(text(),'Get It by Tomorrow')]")
    def deliveryassertion(self):
        return self.driver.find_element(*HomePage.actDelivery)

    #price should be in between 40000 to 50000
    #driver.find_element(By.XPATH, "//span[contains(text(),'₹40,000 – ₹50,000')]")
    price = (By.XPATH, "//span[contains(text(),'₹40,000 – ₹50,000')]")
    def pricefilter(self):
        return self.driver.find_element(*HomePage.price)

    # Assertion for price
    # (By.XPATH, "//span[contains(text(),'₹40,000 – ₹50,000')]")
    actPrice = (By.XPATH, "//span[contains(text(),'₹40,000 – ₹50,000')]")
    def priceassertion(self):
        return self.driver.find_element(*HomePage.actPrice)

    # CPU manufacturer should be intel
    # driver.find_element(By.XPATH, "//body")
    CPU = (By.XPATH, "//body")
    def CPUfilter(self):
        return self.driver.find_element(*HomePage.CPU)

    #Operating system should be window 10 home
    #driver.find_element(By.XPATH, "(//i[@class='a-icon a-icon-checkbox'])[25]")
    checkbox = (By.XPATH, "(//i[@class='a-icon a-icon-checkbox'])[25]")
    def systemfilter (self):
        return self.driver.find_element(*HomePage.search)





