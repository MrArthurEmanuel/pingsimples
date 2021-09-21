import os #importa o modulo ou biblioteca OS (Integra os programas e recursos do SO)
import time

print('#' *31)
print('### Testador de IP''s e Hosts ###')
print('#' *31)
print('\nBy. Mr.Arthur (EU MESMO)')

ip_ou_host = input('\nDigite o IP ou HOST a ser verificado: ')
#Criando uma variável para receber do usuário o IP ou HOST

print("-" *60)
#Imprimindo o "-" 60 vezes

os.system('ping -n 6 {}'. format(ip_ou_host))
#Chamando o Modulo Sistema (system) da biblioteca OS.

print("-" *60)
#Imprimindo o "-" 60 vezes

time.sleep(2)
os.system('pause')