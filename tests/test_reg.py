from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time


def register_user():
    # Setup webdriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://punch.bet/")

    # Сlose panel Get
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body.vsc-initialized:nth-child(2) section.container div.container__body:nth-child(3) section.body div.body__content div.bottomNotificationsContainer___19e2F section.container___1TjXk > i.icomoon-circle-xmark-solid.white___Nq6he.closeBtn___2sUIi"))).click()

    # Accept cookies
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'button_primary___35en0'))).click()

    # Select language
    driver.find_element(By.XPATH, "//span[contains(text(),'Русский')]").click()

    # Click on registration
    driver.find_element(By.XPATH, "//a[contains(text(),'Регистрация')]").click()

    # Fill the form
    driver.find_element(By.XPATH, "//input[@placeholder='Телефон']").send_keys("+79994252469")
    driver.find_element(By.XPATH, "//input[@placeholder='Введите пароль']").send_keys("111111Aa")
    driver.find_element(By.XPATH, "//button[contains(text(),'Регистрация')]").click()

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
    assert "79994252469" in driver.page_source

    # Write credentials to file
    with open("users.txt", "a") as file:
        file.write(f"Phone: +79994252469, Game account: {game_account}, Password: 111111Aa\n")

    # Close the browser
    driver.quit()


if __name__ == "__main__":
    register_user()
