import os
import yaml

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--environment", action="store", default="dev")
    parser.addoption("--browser", action="store", default="firefox")


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    env = request.config.getoption("--environment")
    environment = yaml.safe_load(open(os.path.dirname(__file__) + "/config.yml"))
    url = environment.get(env).get('url')
    driver = request.config.getoption("--browser")
    if driver == "chrome":
        driver = webdriver.Chrome()
        driver.set_page_load_timeout(10)
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(url)
        yield driver  # Teardown
        driver.close()
        driver.quit()
    else:
        driver = webdriver.Firefox()
        driver.set_page_load_timeout(10)
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(url)
        yield driver  # Teardown
        driver.close()
        driver.quit()

