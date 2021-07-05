from selenium import webdriver
from tests.features.pages.home_page import HomePage
from pytest_bdd import scenarios, given, when, then, parsers, scenario
from selenium.webdriver.common.keys import Keys
import pytest
import time
import re


@pytest.fixture
def driver():
    driver = None
    if driver is None:
        driver = webdriver.Chrome()
        return driver


@pytest.fixture
def homePage(driver):
    homePage = HomePage(driver)
    yield homePage


scenarios('../search.feature')


@given(parsers.parse('I navigate to the Google Home page'))
def navigate_to_home_page(homePage):
    homePage.driver.get('https://google.com/')
    time.sleep(5)
    assert homePage.current_url, "{}".format(homePage.project_url)


@when(parsers.parse('I search for {search_data}'))
def search_for(homePage, search_data):
    search_bar = homePage.driver.find_element_by_name(homePage.driver.search_bar)
    search_bar.clear()
    search_bar.send_keys(search_data)
    homePage.find_element_by_css_selector(homePage.driver.search_button).click()


@then(parsers.parse('I should see the results'))
def get_results(homePage):
    assert homePage.driver.find_element_by_css_selector(homePage.first_result).text, "Welcome to Python.org"
