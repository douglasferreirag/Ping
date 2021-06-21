import os  ##Importa o módulo ou biblioteca os (integra os programas e recursos do S.O


print("#" * 60) ##Imprimindo #60 vezes

ip_ou_host = input("Digite o IP ou host a ser verificado: ") ##Criamos uma variável que vai receber do usuário um ip

print("-" * 60) ## imprimindo - 60 vezes

os.system('ping -n 6 {} '.format(ip_ou_host))  ##Chamando system da biblioteca os - comando ping

##-n - num de pacotes que serão 6 {}

print("-" * 60) ## imprimindo - 60 vezes