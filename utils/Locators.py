from selenium.webdriver.common.by import By

class MainPageLocators:
    COOKIE_ACCEPT_BUTTON = (By.CSS_SELECTOR, "button.button___2FjQo.button_primary___35en0.button_m___3GCtx.btn___1uHg1")
    LOGIN_BUTTON = (By.XPATH, "//a[contains(text(),'Вход')]")
    PREMATCH_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/main[1]/section[1]/div[2]/section[1]/aside[1]/nav[1]/a[1]")
    LIVE_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/main[1]/section[1]/div[2]/section[1]/aside[1]/nav[1]/a[2]")
    SIGNUP_PAGE = (By.XPATH, "/html[1]/body[1]/div[1]/main[1]/section[1]/div[2]/section[1]/div[1]/section[1]/div[1]/h1[1]")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "a.container__auth-buttons_item.container__auth-buttons_item-signup")
    MAIN_PAGE = (By.CSS_SELECTOR, ".main-menu-item.active")
    SPORTS_BUTTON = (By.CSS_SELECTOR, ".main-menu-item:nth-child(2)")
    CASINO_BUTTON = (By.CSS_SELECTOR, ".main-menu-item:nth-child(4)")
    MYBETS_BUTTON = (By.CSS_SELECTOR, ".main-menu-item:nth-child(3)")
    MENU_BUTTON = (By.CSS_SELECTOR, ".hamburger-menu")

class RegistrationPageLocators:
    CURRENCY_SELECT = (By.XPATH, "//div[@class='select__placeholder']")
    COUNTRY_SELECT = (By.XPATH, "//div[@class='select__placeholder']")
    PHONE_FIELD = (By.XPATH, "/html[1]/body[1]/div[1]/main[1]/section[1]/div[2]/section[1]/div[1]/section[1]/div[2]/div[2]/div[1]/form[1]/div[3]/div[1]/div[1]/input[1]")
    PASSWORD_FIELD = (By.XPATH, "//input[@placeholder='Введите пароль']")
    REGISTRATION_BUTTON = (By.CLASS_NAME, "signup__btn")
    SUBSCRIBE_BUTTON = (By.XPATH, "//button[contains(text(),'Подписаться')]")
    BONUS_BUTTON = (By.XPATH, "//button[contains(text(),'Хочешь получать больше бонусов?')]")
    PROFILE_BUTTON = (By.XPATH, "//a[contains(text(),'Профиль')]")
    GAME_ACCOUNT = (By.XPATH, "//span[contains(text(),'Игровой счет')]")
    CURRENCY_LOCATOR = (By.XPATH, "//span[@class='user-profile-data__props-value']")