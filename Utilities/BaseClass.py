import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    #This class is the parent of all pages
    #It contains all the generic methods and utilities for all the pages


    def getLogger(self):

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logfile.log')

        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        logger.debug("A debug statement is executed")
        logger.info("A debug statement is executed")
        logger.warning("A debug statement is executed")
        logger.error("A debug statement is executed")
        logger.critical("A debug statement is executed")
        return logger

    def get_title(self,title):
        WebDriverWait(self.driver,20).until(expected_conditions.title_is(title))
        return self.driver.title
