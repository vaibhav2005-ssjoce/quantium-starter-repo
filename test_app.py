from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from dash.testing.application_runners import import_app
from selenium import webdriver
from dash.testing.application_runners import import_app

driver = webdriver.Chrome(executable_path="C:/webdrivers/chromedriver.exe")

app = import_app("app")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

driver_path = ChromeDriverManager().install()

def test_header(dash_duo):
    dash_duo.start_server(app)
    dash_duo.driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
    header = dash_duo.find_element("h1")
    assert "Pink Morsel Sales Visualiser" in header.text
