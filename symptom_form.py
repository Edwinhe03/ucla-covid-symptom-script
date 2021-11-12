from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import getpass
import time

def run(user, pw):
    driver = webdriver.Chrome('./driver/chromedriver')
    driver.get("https://uclasurveys.co1.qualtrics.com/jfe/form/SV_3qRLtouCYKzBbH7")

    try: 
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "QID3-2-label"))
        )
        element.click()
        driver.find_element(By.ID, "NextButton").click()

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="logon"]'))
        )
        element.send_keys(user)

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="pass"]'))
        )
        element.send_keys(pw)


        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="sso"]/form/div/table/tbody/tr/td[1]/button'))
        )
        element.click()

        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, "duo_iframe"))
            )
        
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="auth_methods"]/fieldset/div[1]/button'))
        )
        element.click()

        element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, "NextButton"))
        )
        element.click()

        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "NextButton"))
        )
        element.click()

        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "QID221-15-label"))
        )
        element.click()
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "NextButton"))
        )
        element.click()

        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "NextButton"))
        )
        element.click()

        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "NextButton"))
        )
        element.click()

        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "NextButton"))
        )
        element.click()

        time.sleep(2)
        
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "QID2-1-label"))
        )
        element.click()
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "NextButton"))
        )
        element.click()

        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "QID3-2-label"))
        )
        element.click()
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "NextButton"))
        )
        element.click()
     
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "QID12-2-label"))
        )
        element.click()
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "NextButton"))
        )
        element.click()
    finally:
        time.sleep(10)
        driver.quit()

user = input("Enter username: ")
pw = getpass.getpass("Enter password: ")
print("*** Be ready to authenticate login on DUO Mobile ***")
run(user, pw)
