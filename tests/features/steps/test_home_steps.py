import time

import pytest
from pytest_bdd import scenarios, scenario, given, when, then, parsers
from selenium.webdriver.common.keys import Keys
from tests.features.conftest import driver
from tests.features.object import Singleton
from tests.features.pages.home_page import HomePage
from tests.features.datapool import DATA_ACCESS


@scenario('../search.feature','Search the terms on Google',
           example_converters=dict(data=str))



def test_outlined():
    pass


@given(parsers.parse('I navigate to the Google Home page'))
def navigate_to_home_page(driver):
    homePage = Singleton.getInstance(driver, HomePage)
    assert driver.current_url, "{}".format(homePage.project_url)


@when(parsers.parse('I search for <data>'))
def search_for(driver, data):
    homePage = Singleton.getInstance(driver, HomePage)
    search_bar = driver.find_element_by_name(homePage.search_bar)
    search_bar.clear()
    info = homePage.datapool_read(DATA_ACCESS, data, 'language')
    search_bar.send_keys(info)
    driver.find_element_by_css_selector(homePage.search_button).click()


@then(parsers.parse('I should see the results'))
def get_results(driver):
    homePage = Singleton.getInstance(driver, HomePage)
    assert driver.find_element_by_css_selector(homePage.first_result).text, "Welcome to Python.org"
