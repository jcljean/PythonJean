from acervo import cadastrar, buscar
acervo = []

while True:
    print("Bem-vindo à Biblioteca!")
    print ("1. Adicionar livro")
    print ("2. Listar livros")
    print ("3. Procurar livro")
    print ("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "4":
        print("Saindo da biblioteca. Até logo!")
        break
    elif opcao == "1":
        livro = {}
        livro["titulo"] = input("Digite o título do livro: ")
        livro["autor"] = input("Digite o autor do livro: ")
        livro["ano"] = int(input("Digite o ano de publicação do livro: "))
        cadastrar(acervo, livro["titulo"], livro["autor"], livro["ano"])
        print("Livro adicionado com sucesso!")
    elif opcao == "2":
        if len(acervo) == 0:
            print("Nenhum livro cadastrado.")
        else:
            print("Lista de livros cadastrados:")
            for livro in acervo:
                print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}")
    elif opcao == "3":
        tituloProcurado = input("Digite o título do livro que deseja procurar: ")
        livroEncontrado = buscar(acervo, tituloProcurado)
        if livroEncontrado:
            print(f"Livro encontrado: Título: {livroEncontrado['titulo']}, Autor: {livroEncontrado['autor']}, Ano: {livroEncontrado['ano']}")
        else:
            print("Livro não encontrado.") 
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")