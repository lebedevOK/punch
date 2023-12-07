from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

from utils.Locators import MainPageLocators, RegistrationPageLocators
from utils.utils import telefon_rub

class TestRegistration:
    def test_register_user(self):
        # Setup webdriver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://punch.bet/signup")

        # Wait for page to load
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.SIGNUP_PAGE))

        # Fill the form
        driver.find_element(*RegistrationPageLocators.PHONE_FIELD).send_keys(telefon_rub())
        driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys("111111Aa", Keys.TAB)
        driver.execute_script("arguments[0].scrollIntoView();",
                              driver.find_element(*RegistrationPageLocators.REGISTRATION_BUTTON)).click()

        # Wait for page to refresh and close additional dialogs
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[contains(text(),'Подписаться')]").click()
        driver.find_element(By.XPATH, "//button[contains(text(),'Хочешь получать больше бонусов?')]").click()

        # Check for profile element
        assert "Профиль" in driver.page_source

        # Click on profile and check personal data
        driver.find_element(By.XPATH, "//a[contains(text(),'Профиль')]").click()
        game_account = driver.find_element(By.XPATH, "//span[contains(text(),'Игровой счет')]").text
        assert game_account.isnumeric()
        assert "RUB" in driver.page_source
        #assert "79994252469" in driver.page_source

        # Write credentials to file
        with open("users.txt", "a") as file:
            file.write(f"Phone: +79994252469, Game account: {game_account}, Password: 111111Aa\n")

        # Close the browser
        driver.quit()
