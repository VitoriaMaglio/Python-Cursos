#solicite ao usuário que inscreva um número e use if-else para determinar se o número é par ou ímpar

#Para um número ser par ele precisa se divisível por dois e ter resto zero.

num =int(input('Digite um número: '))
if num%2 == 0:
    print('Número par')
else:
    print('Número ímpar')
    
    
#Pergunte a idade do usuário e use if-elif-else para classificar: 
idade=int(input('Digite sua idade: '))
if  0 <= idade <= 12:
    print('Criança')
elif 13<= idade <= 18:
    print('Adolescente')
else:
    print('Adulto')
    
    

    