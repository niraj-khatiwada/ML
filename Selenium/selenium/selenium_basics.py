from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

from shutil import which

firefox_options = Options()
firefox_options.add_argument("--headless")

driver_execuatble_path = which("geckodriver")

driver = webdriver.Firefox(executable_path= driver_execuatble_path, options= firefox_options)
driver.get(url = "https://www.duckduckgo.com")

search_text = driver.find_element_by_id("search_form_input_homepage")
search_text.send_keys("USer Agent")
# search_text.send_keys(Keys.ENTER)
btn = driver.find_element_by_id("search_button_homepage")
btn.click()

print(driver.page_source)
driver.close()