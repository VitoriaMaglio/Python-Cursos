#Exercícios de treino sobre laçõs de repetição do curso da Alura.



# 1- Ana está desenvolvendo um programa que precisa processar uma lista de 5 nomes de clientes para gerar relatórios mensais. Para isso, ela precisa escrever um programa que percorra a lista de nomes e exiba cada cliente.

#LEMBRAR QUE FOR = SABE O NÚMERO DE ITERAÇÕES -> lista->for->print

clientes = ['João','Ana', 'Vi' , 'Felipe', 'Matheus']
for nome in clientes:
    print(nome)

# 2- André está testando um novo recurso no backend do Buscante que processa dados em um loop. Durante os testes, ele percebeu que o sistema parou de responder, e suspeita que o problema está em um loop infinito. 
#O q está errado?  R: É um loop infinito, falta  o contador +=1
#contador = 0
#while contador < 10:
#   print("Processando dados...")

contador = 0
while contador < 10:
    print("Processando dados...")
    contador +=1


# 3- Você está recebendo uma lista de valores representando os produtos de sua loja virtual e gostaria de calcular a soma total desses produtos para entender o desempenho financeiro semanal.
#valores = [10, 20, 30, 40, 50]
#Crie um programa para implementar a soma.

valores = [10, 20, 30, 40, 50]
soma = 0
for valor in valores:
    soma += valor
    #print(f'A soma total das receitas é: {soma}')
#Se o print estiver dentro do for ele vai imprimir os resultados parciais, para imprimir só o resultado final ele tem que estar fora.
print(f'A soma total das receitas é: {soma}')


# 4- Ana está desenvolvendo seu portfólio para exibir os projetos de Python que concluiu. Ela organizou uma lista com o nome de cada projeto, mas percebeu que alguns itens podem estar ausentes, aparecendo como None: Crie um programa que ajude Ana a percorrer a lista de projetos e exiba os nomes dos projetos válidos. Se encontrar um item None, o programa deve exibir a mensagem: "Projeto ausente".

projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]
for projeto in projetos:
    if projeto is None:
        print('Projeto ausente')
    else:
        print(projeto)