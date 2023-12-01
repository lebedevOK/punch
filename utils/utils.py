import random
from datetime import datetime

def telefon_rub():
    """
    Функция генерирует номер телефона по маске "+7xxx-xxx-xx-xx", где "x" - случайное число от 0 до 9.
    """
    return "+7" + "".join(random.choice("0123456789") for _ in range(10))

def email_gen():
    """
    Функция генерирует электронную почту по маске "30112023112755@qw.ru", где "30112023112755" - 
    текущая дата и время в формате: день, месяц, год, час, минута, секунда.
    """
    return datetime.now().strftime("%d%m%Y%H%M%S") + "@qw.ru"
