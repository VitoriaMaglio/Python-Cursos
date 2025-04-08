#Curso na alura sobre listas e tuplas
#Coleções servem para situações em que precisa armazenar diversos dados. LISTAS,TUPLAS,DICIONÁRIOS,SETS
#var = [lista]
#É possível acessar qualquer valor da lista pela sua posição ; usando len(lista)
#A numeração em python começa por zero, para saber e imprimir a posição precisa ter uma lista e colocar print(lista[0])
#Lista pode ter seus valores alterados, reconhecem todos os tipos de daods pois python é uma linguagem dinâmica
#São variáveis que armazenam diversos dados.
#Para imprimir a lista toda é só dar um print na lista, para imprimir palavra por palavra você usa um for 



lista = [3,6,9,12]
print(type(lista))
print(lista[3])
x = len(lista)
print(x)


for idade in lista:
    print(idade)

#TUPLAS são imutáveis
tupla = ('carro', True, 3.5)
print(type(tupla))
print(tupla)
print(tupla[2])

#dict não permitem membros duplicados , ordenada
dicionario = {
    'chave ' : 2,
    'idade' : 13,
    'nome' : 'Vitória'
}
print(type(dicionario))
print(dicionario)
print(dicionario['nome'])

#sets = conjuntos ; não permitem membros duplicados , não ordenada ent não tem ordem de index
conjunto = { 
    True , 'carro' , 2
}
print(type(conjunto))
print(conjunto)