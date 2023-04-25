 #  CRUD-PORTOS BRASILEIROS---> PBL 03
portos = [ ]
 #  função para cadastrar portos
def AdicionarNovoPorto():
    print("Adicione um novo porto->>>")
    nome = input("Digite o nome do porto: ")
    estado = input("Digite o estado do Porto: ")
    autoridade = input("Digite a autoridade portuária: ")
    tipo = input("Digite o tipo do porto: ")
    porto = {"nome": nome, "estado": estado,
             "autoridade": autoridade, "tipo": tipo }
    portos.append(porto)
    print("Porto cadastrado com sucesso!")
#  fução para listar portos
def ListarPortos():
    if len(portos) == 0:
        print("Nenhum porto cadastrado. ")
    else:
        for i,porto in enumerate(portos):
            print(f"{i+1} - {porto['nome']} ({porto['estado']}) - {porto['tipo']}")
#  função para atualizar portos
def AtualizarPortos():
    if len(portos) == 0:
        print("Nenhum porto cadastrado. ")
    ListarPortos()
    indice = int(input("Digite o número do porto que deseja atualizar: "))-1
    if indice < 0 or indice > len(portos):
        print("Indíce inválido. ")
        return
    porto = portos[indice]
    print(f"Atualizar Porto {porto['nome']}: ")
    nome = input(f"Digite o novo nome do porto: ")
    estado = input("Digite o estado: ")
    autoridade = input("Digite a autoridade: ")
    tipo = input("Digite o tipo do porto: ")

    if nome:
        porto['nome'] = nome
    if estado:
        porto['estado'] = estado
    if autoridade:
        porto['autoridade'] = autoridade
    if tipo:
        porto['tipo'] = tipo
    print("Porto atualizado com sucesso.")
    ListarPortos()
 # função para excluir Portos    
def ExcluirPortos():
    ListarPortos()
    indice = int(input("Digite o índice do porto que deseja excluir: "))-1
    if indice <0 or indice >= len(portos):
        print('Número inválido! ')
        return
    del portos[indice]
    print("Porto excluído com sucesso. ")
#  Menu
def Menu():
    while True:
        print("Selecione uma opção:")
        print("1- Adicionar um novo porto ")
        print("2- Atualizar porto existente")
        print("3- Excluir porto")
        print("4- Listar portos")
        print("0- Sair")
        
        opcao = input("Opção escolhida: ")

        if opcao == "1":
            AdicionarNovoPorto()
        elif opcao == "2":
            AtualizarPortos()
        elif opcao == "3":
            ExcluirPortos()
        elif opcao == "4":
            ListarPortos()
        elif opcao == "0":
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

Menu()
  # este código funciona