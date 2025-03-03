import pyautogui
from time import sleep

# 1 - Clicar e digitar meu usuário
pyautogui.click(740, 384, duration=0.5)
pyautogui.write('Victor Hugo')
# 2 - Clicar e digitar minha senha
pyautogui.click(678, 413, duration=0.5)
pyautogui.write('210603')
# 3 - Clicar em "Entrar"
pyautogui.click(595, 433, duration=0.5)
sleep(2) #adicionado um sleep para garantir que a pagina carregou.

# 4 - Extrair cada produto
try:
    with open('produtos.txt', 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip() #remove o \n do final da linha.
            produto, quantidade, preco = linha.split(',')

            # 1 - Clicar e digitar produto
            pyautogui.click(419, 375, duration=0.5)
            pyautogui.write(produto)

            # 2 - Clicar e digitar quantidade
            pyautogui.click(419, 399, duration=0.5)
            pyautogui.write(quantidade)

            # 3 - Clicar e digitar preço
            pyautogui.click(412, 423, duration=0.5)
            pyautogui.write(preco)

            # 4 - Clicar em registar
            pyautogui.click(307, 577, duration=0.5)
            sleep(1)
except FileNotFoundError:
    print("Erro: O arquivo 'produtos.txt' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")