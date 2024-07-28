import pytest
import subprocess


@pytest.fixture(scope="class")
def browser_context():
    from playwright.sync_api import sync_playwright
    # install_playwright()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()


@pytest.fixture(scope="class")
def setup(browser_context, request):
    page = browser_context.new_page()
    page.goto("https://advisor-test.pontera.com/business/auth/signin")
    request.cls.page = page
    yield
    page.close()


def install_playwright():
    subprocess.run(["playwright", "install"], check=True)


@pytest.fixture(scope="function", autouse=True)
def setup_method():
    # This method is called before each test
    test_data = {
        "user_name": "Maayan+Tester1@feex.com",
        "password": "Advisor0103Buckley",
        "firm": "QA Advisors"
    }
    yield test_data
