import os
import subprocess
import sys

def limpar_tela():
    # Limpar tela do terminal (funciona em Windows e Unix/Linux/MacOS)
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    limpar_tela()
    print("=" * 50)
    print("MENU DE PROJETOS")
    print("=" * 50)
    print("1 - Transformar imagem para tons de cinza (Atividade 1)")
    print("2 - Aplicar tonalidades em imagem (Atividade 2)")
    print("0 - Sair")
    print("=" * 50)
    
    opcao = input("Digite o número correspondente ao projeto que deseja executar: ")
    
    if opcao == "1":
        limpar_tela()
        print("Executando o projeto de transformação para tons de cinza...\n")
        script_path = os.path.join("atividade1", "main1.py")
        subprocess.run([sys.executable, script_path])
    elif opcao == "2":
        limpar_tela()
        print("Executando o projeto de aplicação de tonalidades...\n")
        script_path = os.path.join("atividade2", "main2.py")
        subprocess.run([sys.executable, script_path])
    elif opcao == "0":
        print("Saindo do programa...")
        return
    else:
        print("Opção inválida. Por favor, tente novamente.")
        input("Pressione ENTER para continuar...")
        main()  # Volta ao menu principal

if __name__ == "__main__":
    main()
