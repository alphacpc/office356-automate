from selenium import webdriver
from selenium.webdriver.common.by import By
from config import username_valid, password, onedrive_url_valid
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
from time import sleep


conn = ClientContext(onedrive_url_valid).with_credentials(
    UserCredential(user_name = username_valid, password = password)
)


browser = webdriver.Chrome("./chromedriver/chromedriver")

endpoint = f"{onedrive_url_valid}/Documents/Users"

browser.get(endpoint)

sleep(10)

user = browser.find_element(By.CSS_SELECTOR, value="#i0116")
user.send_keys(username_valid)

sleep(10)

button = browser.find_element(By.CSS_SELECTOR, value="#idSIButton9")
button.click()

sleep(10)

button_password = browser.find_element(By.CSS_SELECTOR, value="#passwordInput")
button_password.send_keys(password)

sleep(4)

button_submit = browser.find_element(By.CSS_SELECTOR, value="#submitButton")
button_submit.click()

sleep(4)

button_stay_connected = browser.find_element(By.CSS_SELECTOR, value="#idSIButton9")
button_stay_connected.click()


# list_source = conn.web.get_folder_by_server_relative_url(f"Documents/Classeurs")
# files = list_source.files
# conn.load(files)
# conn.execute_query()

# file = files[0]
# print(file.name, file.serverRelativeUrl)
# print(file.get_property("LinkingUrl"))

# browser.get(file.get_property("LinkingUrl"))

# user = browser.find_element(By.CSS_SELECTOR, value="#i0116")
# user.send_keys(username_valid)

# button = browser.find_element(By.CSS_SELECTOR, value="#idSIButton9")
# button.click()

# sleep(4)

# button_password = browser.find_element(By.CSS_SELECTOR, value="#passwordInput")
# button_password.send_keys(password)



# button_submit = browser.find_element(By.CSS_SELECTOR, value="#submitButton")
# button_submit.click()

# sleep(4)

# button_stay_connected = browser.find_element(By.CSS_SELECTOR, value="#idSIButton9")
# button_stay_connected.click()



sleep(30)

browser.close()