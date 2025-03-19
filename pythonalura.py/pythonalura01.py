import os

#lista é feita com = e [] ; para colocar alçgum dado dentro da listra utiliza a palavbra append ;  são mutáveis.
#tuplas são marcadas com () ;  são imutáveis, ou seja,  seus elementos não podem ser alterados depois de criada.

#dicionário
restaurantes = []


def exibir_nome_do_programa():      
    print("""
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')
    
#print('opcao_escolhida == 1')
#print(type(opcao_escolhida))
#print(type(1)) ; não é possível comparar dois tipos diferentes de variáveis, port isso quando não convertenmos o programa continua encerrando.
#Para converter variável é só colocar o tipo que vc quer converter e colocar o que está atribuido a ela entre parênteses.

# se opcao_escolhida for igual a 1 { codigo 1 } = Lógica programação

#Função em python para deixar o código organizado, que é um bloco de código parar executar certas linhas de código.

def finalizar_app():
    exibir_subtitulo('Encerrando o app')
    
def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def opcao_invalida():
        print('Opção inválida!\n')
        voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()
    
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    
    
    for restaurante in restaurantes: #para cada restaurante na lista restaurantes, executar a ação nome ;  for é uma estrutura de repetição usado quando o número de iterações é conhecido, (já o while é usado quando o número de iterações não é conhecido)
            print(f'{restaurantes}')
    voltar_ao_menu_principal()
    
    
    
def escolher_opcao():
    try: # o programa vai tentar ler um inteiro, se não conseguuir vai ler como uma opção inválida.
        
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}.')
        
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app() #toda função tem que ter o parênteses para funcionar
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls') #limpar a tela
    exibir_nome_do_programa()  
    exibir_opcoes()  
    escolher_opcao()
      
if __name__ == '__main__':  
    main()
    main()