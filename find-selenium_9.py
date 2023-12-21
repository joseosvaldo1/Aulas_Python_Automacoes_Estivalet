"""
Automação Web - Parte XI:

* Aguardando Um Elemento Estar Visível:

- Os tipos de métodos de espera que o Selenium WebDriver oferece são:
1) Sleep: Ele é um método que interrompe a execução do script por um tempo 
específico, independentemente do elemento ter sido encontrado ou não.
# Desvantagem:
- O script vai ser obrigado a aguardar todo o tempo do sleep passar, mesmo 
que o elemento seguinte já esteja disponível, aumentando o tempo geral da 
execução do script.
- O Selenium ainda vai lançar um erro se o elemento não aparecer somente 
após o tempo passar do sleep. Nesse caso, então você não saberá o quanto 
tempo leva para que ele apareça, forçando a experimentar diversas vezes até 
acertar o tempo do sleep, que, aliás, pode variar a depender também da conexão
com um site da internet. Enfim, são vários fatores.

- Ele só funciona para o próximo elemento do script. No caso de haver vários 
elementos que necessitam de espera. Você precisa especificar esse sleep para 
cada um deles, poluindo muito código.Portanto, então é sleep. Ele não é uma 
boa prática.

2) Implicit Wait: Ele manda o Web Driver aguardar por um tempo quando 
tenta localizar algum elemento que não está disponível imediatamente.
# Vantagens:
- Ele é declarado somente uma vez e se mantém até o fim do uso do web driver, 
- Não vai precisar esperar todos os segundos que foram especificados. 
O script vai continuar até que o elemento seja localizado. Caso não seja após 
o tempo de espera, o Selenium lança então uma exceção, por exemplo, 
"no such element exception".
# Desvantagens: 
- Performances; 
- Exceptions; 
- Confiabilidade; 
- Condições.

3) Explicit Wait: Ele pode estipular um tempo de espera até que uma certa 
condição se cumpra. Por exemplo, espere 30 segundos até que o elemento X
seja clicável. Caso a condição não se cumpra no tempo estipulado, o Selenium
retornará um erro. Caso a condição se cumpra, podemos realizar uma ação
como, por exemplo, clicar em um elemento ou preencher um campo.


Implicit Wait                    vs         Explicit Wait:
1) É aplicado a todos os                    1) Aplica-se a um elemento por vez    
elementos do script;                           que é específico para uma dada
2) Não pode esperar baseado                    condição;
em uma condição como "ser                   2) Pode-se especificar o tempo da 
clicável" ou "estar visível";                  espera com base na condição dada;
3) Geralmente é usado quando                3) Geralmente é usado quando não se
se tem certeza de que o                        pode prever quando o elemento 
elemento estará visível em                     estará visível.
um dado momento. 

4) Fluent wait: Ele vai definir a quantidade máxima de tempo a se esperar por 
uma condição, bem como a frequência com que se verifica a mesma. Podemos 
configurar esse tipo de wait para ignorar algumas exceptions específicas 
enquanto se aguarda a busca por um elemento na página.

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#import time
import sys

sys.stdout.reconfigure(encoding='utf-8')
driver = webdriver.Chrome()
page = "https://estivalet.github.io/static-testing-sites/simple/dynload.html"
driver.get(page)


button = driver.find_element(By.XPATH, '//button[.="Start 1"]')
button.click()

wait = WebDriverWait(driver, 10)
condition = EC.visibility_of_element_located((By.ID, 'finish'))
wait.until(condition)


print("Continua a execução do script.")

#time.sleep(3)


driver.close()
