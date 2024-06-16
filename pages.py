from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def login(navegador, username, password):
    navegador.get('https://www.saucedemo.com/')  # abrindo url
    sleep(2)
    navegador.find_element('xpath', '//*[@id="user-name"]').send_keys(username)
    sleep(2)
    navegador.find_element('xpath', '//*[@id="password"]').send_keys(password)
    sleep(2)
    navegador.find_element('xpath', '//*[@id="login-button"]').click()
    sleep(2)


def adicionar_item_carrinho(navegador):
    itens = [
        'Test.allTheThings() T-Shirt (Red)',
        'Sauce Labs Bolt T-Shirt',
        'Sauce Labs Bike Light'
    ]
    for item in itens:
        elemento_item = navegador.find_element(
            By.XPATH, f"//div[text()='{item}']/ancestor::div[@class='inventory_item']//button")
        elemento_item.click()
        sleep(2)


def ver_carrinho(navegador):
    navegador.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    sleep(3)


def checkout(navegador):
    navegador.find_element(By.ID, 'checkout').click()
    sleep(2)
    navegador.find_element(By.ID, 'first-name').send_keys('Lucca')
    navegador.find_element(By.ID, 'last-name').send_keys('Batista')
    navegador.find_element(By.ID, 'postal-code').send_keys('12345')
    navegador.find_element(By.ID, 'continue').click()
    sleep(2)
    navegador.find_element(By.ID, 'finish').click()
    sleep(10)

    total_element = navegador.find_element(
        By.CLASS_NAME, 'summary_total_label')
    total = total_element.text
    return total
