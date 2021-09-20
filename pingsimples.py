import os #importa o modulo ou biblioteca OS (Integra os programas e recursos do SO)

print("#" *60) #Imprimindo 60 vezes o "#"

ip_ou_host = input('Digite o IP ou HOST a ser verificado: ')
#Criando uma variável para receber do usuário o IP ou HOST

print("-" *60)
#Imprimindo o "-" 60 vezes

os.system('ping -n 6 {}'. format(ip_ou_host))
#Chamando o Modulo Sistema (system) da biblioteca OS.

print("-" *60)
#Imprimindo o "-" 60 vezes