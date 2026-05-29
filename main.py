from album import Album
from dados import dados_album

meu_album = Album()

for pais, numeros in dados_album.items():
    meu_album.adicionar_varias_figurinhas(pais, numeros)

while True:
    print("\n")
    print("MENU ÁLBUM")
    print("1 - Adicionar figurinha")
    print("2 - Mostrar figurinha")
    print("3 - Mostrar repetidas")
    print("4 - Sair")
    print("\n")
    
    opcao = input("escolha uma opção: ")
    print("\n")
    if opcao == "1":
        pais = input("Digite o pais: ")
        numero = int(input("Digite o número da figurinha: "))
        meu_album.adicionar_figurinha(pais, numero)
        print("Figurinha adicionada!")
        
    elif opcao == "2":
        meu_album.mostrar_figurinhas()
        print("\n")

    elif opcao == "3":
        meu_album.mostrar_repetidas()
        print("\n")
        
    elif opcao == "4":
        print("Saindo do álbum...")
        break