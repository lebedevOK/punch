from selenium.webdriver.common.by import By

class MainPageLocators:
    COOKIE_ACCEPT_BUTTON = (By.CLASS_NAME, "accept-cookies")
    LOGIN_BUTTON = (By.XPATH, "//a[contains(text(),'Вход')]")
    PREMATCH_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/main[1]/section[1]/div[2]/section[1]/aside[1]/nav[1]/a[1]")
    LIVE_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/main[1]/section[1]/div[2]/section[1]/aside[1]/nav[1]/a[2]")
    SIGNUP_PAGE = (By.XPATH, "/html[1]/body[1]/div[1]/main[1]/section[1]/div[2]/section[1]/div[1]/section[1]/div[1]/h1[1]")

class RegistrationPageLocators:
    PHONE_FIELD = (By.XPATH, "/html[1]/body[1]/div[1]/main[1]/section[1]/div[2]/section[1]/div[1]/section[1]/div[2]/div[2]/div[1]/form[1]/div[3]/div[1]/div[1]/input[1]")
    PASSWORD_FIELD = (By.XPATH, "//input[@placeholder='Введите пароль']")
    REGISTRATION_BUTTON = (By.CLASS_NAME, "signup__btn")
    SUBSCRIBE_BUTTON = (By.XPATH, "//button[contains(text(),'Подписаться')]")
    BONUS_BUTTON = (By.XPATH, "//button[contains(text(),'Хочешь получать больше бонусов?')]")
    PROFILE_BUTTON = (By.XPATH, "//a[contains(text(),'Профиль')]")
    GAME_ACCOUNT = (By.XPATH, "//span[contains(text(),'Игровой счет')]")