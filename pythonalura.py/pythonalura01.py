import os

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
    os.system('cls')  # Limpa a tela do terminal
    print('Encerrando o app')

def opcao_invalida():
    print('Opção inválida\n')
    input('Digite uma tecla para voltar ao menu principal')
    main() #vai limpar todas as opções de erro 
    
def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    print(f'Você escolheu a opção {opcao_escolhida}.')
    
    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurante')
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
    elif opcao_escolhida == 4:
        finalizar_app
    else:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()  
    exibir_opcoes()  
    escolher_opcao()
    
    
    
if __name__ == '__main__':  # Correção do nome especial '__main__'
    main()