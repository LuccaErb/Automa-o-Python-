# biblioteca para fazer as funcoes demorarem um pouco mais para vizualização melhor do desenvolvedor
from time import sleep
from selenium import webdriver
# versao mais atualizada do chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from utils import ler_login_credenciais
from pages import login, adicionar_item_carrinho, ver_carrinho, checkout


def main():
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)

    username, password = ler_login_credenciais('login.csv')

    login(navegador, username, password)
    adicionar_item_carrinho(navegador)
    ver_carrinho(navegador)
    checkout(navegador)

    print(f"O valor total da compra é: {total}")

    # fechando navegador aopos finalizar
    sleep(5)
    navegador.quit()


if __name__ == "__main__":
    main()
