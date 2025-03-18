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

def finalizar_app():
    os.system('cls')  # Limpa a tela do terminal
    print('Encerrando o app')

def opcao_invalida():
    print('Opção inválida\n')
    input('Digite uma tecla para voltar ao menu principal...')
    main()  # Volta ao menu principal

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    
    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurante')
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
    elif opcao_escolhida == 4:
        print('Sair')
        finalizar_app()  # Finaliza o app
    else:
        opcao_invalida()  # Chama função de opção inválida

def main():
    exibir_nome_do_programa()  
    exibir_opcoes()  
    escolher_opcao()

if __name__ == '__main__':  # Correção do nome especial '__main__'
    main()
    