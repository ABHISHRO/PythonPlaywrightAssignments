import pytest


# Run when pytest starts
def pytest_configure(config):
    config.option.browser = ["chromium", "firefox"]
    #config.option.reruns = 1                          # retry a failed test once (needs pytest-rerunfailures)


# Base URL
@pytest.fixture(scope="session")
def base_url():
    return "https://eventhub.rahulshettyacademy.com"