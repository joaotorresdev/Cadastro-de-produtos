import os 
opcao=0
produto_codigo=[]
produto_nome=[]
produto_preco=[]
produto_quant=[]

while opcao!= 4:
    print("-------------- MENU -----------")
    print("1 - CADASTRAR PRODUTO")
    print("2 - LISTAR PRODUTOS")
    print("3 - Excluir produto")
    print("4 - Sair")

    opcao=int(input("Escolha a opção:"))

    if opcao == 1:
        codigo=input("Digite o código do produto: ")
        nome=input("Digite o nome do produto: ")
        preco=input("Digite o preço do produto: R$")
        quant=input("Digite a quantidade no estoque: ")

        arquivo = open("cad_produtos.txt", "a")
        arquivo.write(f"{codigo},{nome},{preco},{quant}\n")
        arquivo.close()

        os.system("cls")
        print("PRODUTO CADASTRADO!!!")

    elif opcao ==2:
        print("============== BANCO DE DADOS =============")

        arquivo = open("cad_produtos.txt", "r")
        for linha in arquivo:
            
            codigo, nome, preco, quant = linha.strip().split(",")
            print("\n")
            print(f"Código do produto: \t{codigo}")
            print(f"Nome do produto: \t{nome}")
            print(f"Preço do produto: \t{preco}")
            print(f"Produtos em estoque: \t{quant}")
            print("---------------------------------------------------------\n")
        arquivo.close()
        input()
        os.system("cls")
    elif opcao == 3:
        arquivo = open("cad_produtos.txt", "r")# PARA LER O ARQUIVO
        linhas = arquivo.readlines()#PARA LEITURA DAS LINHAS 
        arquivo.close()

        remover = int(input("Digite a linha que deseja remover: "))
        remover = remover - 1
        linhas.pop(remover)

        arquivo = open("cad_produtos.txt", "w")
        for linha in linhas:
            arquivo.write(linha)
        arquivo.close()

        print("Produto removido com sucesso!")
        input()
        os.system("cls")
    