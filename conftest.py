import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    headless = os.getenv("HEADLESS", "true").lower() == "true"

    # Si algún día querés Grid:
    # remote_url = os.getenv("SELENIUM_REMOTE_URL")
    # if remote_url:
    #     options = webdriver.ChromeOptions()
    #     if headless:
    #         options.add_argument("--headless=new")
    #     options.add_argument("--no-sandbox")
    #     options.add_argument("--disable-dev-shm-usage")
    #     d = webdriver.Remote(command_executor=remote_url, options=options)
    #     d.implicitly_wait(10)
    #     yield d
    #     d.quit()
    #     return

    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1366,768")

    service = Service(ChromeDriverManager().install())
    d = webdriver.Chrome(service=service, options=options)
    d.implicitly_wait(10)

    yield d
    d.quit()