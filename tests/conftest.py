import os
import time

import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
@pytest.fixture(scope="class")
def setup(request):
    global driver
    browserName = request.config.getoption("browser_name")

    if browserName == "chrome":
        services_obj = Service(r"C:\Selenium Softwares\chromedriver.exe")
        driver = webdriver.Chrome(service=services_obj)

    elif browserName == "edge":
        service_obj = Service(r"C:\Selenium Softwares\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)


    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    request.cls.driver = driver

    yield
    #driver.close()