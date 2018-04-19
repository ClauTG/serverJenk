import pytest
from selenium import webdriver


def pytest_addoption(parser):
	parser.addoption("--driver", action="store", default="chrome", help="Type in browser type")
	parser.addoption("--url", action="store", default="https://qa.moodle.net/", help="url")
	parser.addoption("--username", action="store", default="manager", help="username")
	parser.addoption("--password", action="store", default="test", help="password")
	parser.addoption('--headless', 
						action='store_true', default=False,
						help='enable headless mode for supported browsers.')


@pytest.fixture
def chrome_options(chrome_options):
	chrome_options.add_argument('--headless')
    return chrome_options

@pytest.fixture(scope="module", autouse=True)
def driver(request):
	
	BROWSER = request.getoption("--driver")

	if BROWSER == 'chrome':
		
		chromeOptions = webdriver.ChromeOptions()

		if headless:
			print "Run test in headless mode: --headless"
			chromeOptions.add_argument("--headless")

		else:
			browser = webdriver.Chrome()
	
		browser.get("about:blank")
		browser.implicitly_wait(10)
		browser.maximize_window()
		return browser

	else:
		print 'only chrome is supported at the moment'

@pytest.fixture(scope="module")
def username(request):
	return request.config.getoption("--username")

@pytest.fixture(scope="module")
def password(request):
	return request.config.getoption("--password")

@pytest.fixture(scope="module")
def url(request):
	return request.config.getoption("--url")