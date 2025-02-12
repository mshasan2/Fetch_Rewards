from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create a new instance of the Chrome driver
service = Service(exceutable_path='chromedriver')
driver = webdriver.Chrome(service=service)

# Navigate to the application home page
driver.get('http://sdetchallenge.fetch.com/')

# Wait for the page to load
WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, 'root')))


def printWeighing():
    # This function will print the number of weighings and the list of weighings
    items = driver.find_elements(By.XPATH, "/html/body/div/div/div[1]/div[5]/ol/li")
    print("Number of weighings: ", len(items))
    print("List of weighings: ")
    for item in items:
        print(item.text)
    return

def clickResult(driver, resultCoin):
    # This function will click the result button and catch the alert
    result = driver.find_element(By.ID, resultCoin)
    result.click()
    # Catch the alert
    WebDriverWait(driver, 15).until(
        EC.alert_is_present())
    completion_alert = driver.switch_to.alert
    text = completion_alert.text
    print("Alert Message: ", text)
    # Adding a delay of 2 seconds to manually check the result
    time.sleep(2)
    completion_alert.accept()
    printWeighing()
    return

def clickReset(driver):
    # This function will click the reset button
    reset = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[4]/button[1]")
    reset.click()
    return
    

def findBar(left, right, remaining):
    # This function contains the logic to find the fake bar
    for idx, l in enumerate(left):
        inputElement = driver.find_element(By.ID, ('left_'+str(idx)))
        inputElement.send_keys(l)
    for idx, r in enumerate(right):
        inputElement = driver.find_element(By.ID, ('right_'+str(idx)))
        inputElement.send_keys(r)
    weigh = driver.find_element(By.ID, 'weigh')
    weigh.click()

    # Adding a delay of 2 seconds to manually check the result
    time.sleep(2)

    result_element = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/button")
    if result_element.text == '=':
        if len(remaining) == 1:
            clickResult(driver, "coin_"+remaining[0])
        else:
            clickReset(driver)
            findBar(remaining[0], remaining[1], remaining[2])
    elif result_element.text == '<':
        if len(left) == 1:
            clickResult(driver, "coin_"+left[0])
        else:
            clickReset(driver)
            findBar(left[0], left[1], left[2])
    elif result_element.text == '>':
        if len(right) == 1:
            clickResult(driver, "coin_"+right[0])
        else:
            clickReset(driver)
            findBar(right[0], right[1], right[2])

    return

# Start the process
findBar(['0','1','2'],['3','4','5'],['6','7','8'])

# Wait for 2 seconds before closing the browser, so that we can see the final result
# The below line can be removed if we don't want to see the final result
time.sleep(2)

# Close the browser
driver.quit()