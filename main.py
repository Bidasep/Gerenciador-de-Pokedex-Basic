#O objetivo deste projeto é desenvolver um programa para gerenciar uma Pokédex (um banco de dados de Pokémon). O 
# programa deve permitir ao usuário realizar operações básicas de gerenciamento, como adicionar,
# listar, remover e atualizar dados de Pokémon, além de registrar capturas e exibir um histórico de 
# capturas. Este projeto ajuda a consolidar o uso de estruturas de dados em Python, como dicionários e 
# listas, bem como a aplicar conceitos de programação orientada a objetos, se desejado, e manipulação de entrada e saída.





pokemons = []
# "Nome do pokemon" : nome_pokemon,
# "Tipo do Pokemon" : tipo_pokemon,
# "Nivel do Pokemon" : nivel_pokemon


registros_captura = []
#"Nome do pokemon":nome_pokemon,
#"Quantidade de capturas": quantidade_captura

#1 - Adicionar Pokémon:
# O programa deve pedir o nome do Pokémon, o tipo (como "Fogo", "Água", "Elétrico", etc.),
# e o nível (um número inteiro entre 1 e 100). Essas informações devem ser armazenadas no dicionário.
def adicionar_pokemon():
    #recebe o nome do pokemon
    nome_pokemon = input ("Digite o nome do pokemon: ")
    
    #verifica se o pokemon já está cadastrado
    for pokemon in pokemons:
        if pokemon["Nome do pokemon"].lower() == nome_pokemon.lower(): 
            print ("Pokemon já cadastrado.")
            return
        
    #se nao estiver cadastrado, pede o tipo de pokemon    
    tipo_pokemon = input("Digite o tipo de pokemon:\n" "'Fogo' ,'Agua', 'Elétrico', 'Terra', 'Pedra' etc...  \n")    
        
    #faz um try exceptio com a entrada para ser um inteiro
    try:
        nivel_pokemon = int(input("Digite o nivel do pokemon entre 1 e 100\n"))
        
        #válida a entrada para estar entre 1 e 100
        if nivel_pokemon < 1 or nivel_pokemon > 100:
            print("Valor inválido, Digite um valor válido entre 1 e 100")
            return
        
    except ValueError:
        print("Nivel do Pokemon inválido, Digite um nivel válido.")
        return
    
    #Adiciona o dicionário do pokemon na lista de pokemons.
    pokemons.append({
        "Nome do pokemon" : nome_pokemon,
        "Tipo do Pokemon" : tipo_pokemon,
        "Nivel do Pokemon" : nivel_pokemon
    })
    
    print (f"Pokemon {nome_pokemon} foi adicionado com sucesso, seu tipo é: {tipo_pokemon} e seu nivel é: {nivel_pokemon}")
    

#Listar Pokémon:
# O programa deve exibir todos os Pokémon cadastrados no formato: 
# nome do Pokémon - tipo - nível. Os Pokémon devem ser listados em ordem alfabética.
def listar_pokemon():
    
    
    #se nao tiver nenhum pokemon na lista de pokemons
    if not pokemons:
        
        print("\n======================================================")
        print("                 Lista de Pokemons                    ")
        print("======================================================")
        print("\n           Não há Pokemons na lista.\n")
    else:
        
        print("\n======================================================")
        print("                 Lista de Pokemons                    ")
        print("======================================================\n")
        
        #varre cada pokemon e imprime na tela as informações e em ordem alfábetica com base no "nome do pokemon"
        for pokemon in sorted (
            pokemons,key=lambda p: p["Nome do pokemon"].lower()):
            
            print(
                f"Nome do Pokemon: {pokemon['Nome do pokemon']} - "
                f"Tipo do pokemon: {pokemon['Tipo do Pokemon']} - "
                f"Nivel do Pokemon: {pokemon['Nivel do Pokemon']}\n"
            )
            


#Remover Pokémon:
# O programa deve pedir o nome do Pokémon a ser removido. Caso o Pokémon 
# exista, ele será removido do dicionário. Se o Pokémon não existir, o programa exibirá uma mensagem de erro.
def remover_pokemon():
    #recebe o nome do pokemon
    nome_pokemon = input("Digite o nome do pokemon a ser Removido:")
        
    #varre cada pokemon e compara com o nome do pokemon passado, se existir, deleta o dicionário do pokemon.
    for pokemon in pokemons:
        if pokemon["Nome do pokemon"].lower() == nome_pokemon.lower():
            pokemons.remove(pokemon)
            print(f"Pokemon {nome_pokemon} removido com sucesso")
            return
            
    print("Este Pokemon nao está cadastrado ou já foi deletado.")
      
    
#Atualizar nível do Pokémon:
# O programa deve pedir o nome do Pokémon e o novo nível (um número inteiro entre 1 e 100).
# Se o Pokémon existir, o nível será atualizado. Caso contrário, será exibida uma mensagem de erro.       
def atualizar_nivel():
    #Recebe o nome do pokemon
    nome_pokemon = input("Digite o nome do pokemon para atualizar a força:")
    
    #varre cada pokemon e compara com o nome do pokemon passado, se existir
    for pokemon in pokemons:
        #Se existir o pokemon, faz um try e recebe o novo valor do nivel "int" que deverá ser maior que 0 e menor que 101
        if pokemon["Nome do pokemon"].lower() == nome_pokemon.lower():
            try:
                novo_valor = int(input("Digite o novo valor do Nivel"))
                
                if novo_valor <1 or novo_valor >100 :
                    print("Valor inválido, digite um valor entre 1 e 100")
                    return
                
            except ValueError:
                print("Valor inválido.Digite um valor válido entre 1 e 100")
                return
            #atualiza o novo valor do nivel do pokemon dentro do indice do momento.
            pokemon["Nivel do Pokemon"] = novo_valor
            
        
            
            print(f"O pokemon {nome_pokemon}, foi atualizado o Nivel para {novo_valor}.")
            return
            
        
    print("Este pokemon nao está cadastrado ou já foi removido")    
            
            
#Registrar captura de Pokémon:
# O programa deve pedir o nome do Pokémon e a quantidade de 
# vezes capturadas. O valor de capturas será atualizado, aumentando a quantidade de vezes que o 
# Pokémon foi capturado. Caso o Pokémon não exista, será exibida uma mensagem de erro.    
def registrar_captura():
    
    nome_pokemon = input("Digite o nome do pokemon para registar a sua captura: ")
    
    #varre cada pokemon e compara com o nome do pokemon passado
    for pokemon in pokemons:
        if pokemon["Nome do pokemon"].lower() == nome_pokemon.lower():
            #se existir o pokemon dentro da lista: faz um try exception para o valor da quantidade de captura
            try:
                quantidade_captura = int(input(f"Digite a quantidade de vezes em que o {nome_pokemon} foi capturado, o valor deverá ser maior que 1: "))
                
                #a quantidade de capturas deve ser maior que zero.
                if quantidade_captura > 0:
                    
                    # se nao existir nenhum registro de captura, adiciona o novo registro a lista.
                    if not registros_captura:
                        
                        registros_captura.append({
                        "Nome do pokemon":nome_pokemon,
                        "Quantidade de capturas": quantidade_captura
                        })
                        
                        print(f"\nA quantidade de capturas do {nome_pokemon} foi Registrada com sucesso,a quantidade de capturas é = {quantidade_captura}")
                        return
                    
                    #Se existir registro:
                    else:
                        #faz uma varredura em cada registro.
                        for registro in registros_captura:
                            if registro["Nome do pokemon"].lower() == nome_pokemon.lower():
                                
                                #pega a quantidade de registros e adiciona a nova quantidade.
                                registro["Quantidade de capturas"] += quantidade_captura
                                print(f"\nA quantidade de capturas do {nome_pokemon} foi atualizada com sucesso, nova quantidade = {registro['Quantidade de capturas']}")
                                return
                        
                        #se existir o registro do pokemon mas nao existir o registro de captura    
                        registros_captura.append({
                            "Nome do pokemon":nome_pokemon,
                            "Quantidade de capturas": quantidade_captura
                        })
                        
                        print(f"\nA quantidade de capturas do {nome_pokemon} foi Registrada com sucesso,a quantidade de capturas é = {quantidade_captura}")
                        return
                else:
                    print("\nO valor deve ser maior que zero")
                    return    
                            
            except ValueError:
                print("\nErro.Digite um valor válido para a quantidade de captura.")
                return           
            
    
    
    print(f"\n O pokemon {nome_pokemon} não existe ou já foi deletado da base de dados.")    
        
#Exibir histórico de capturas:
# O histórico de capturas deve ser armazenado em uma lista, onde 
# cada entrada consiste no nome do Pokémon e a quantidade de vezes que foi capturado. Quando o 
# usuário escolher exibir o histórico de capturas, o programa deve mostrar todas as entradas feitas.
def exibir_historico():
    #Se nao existir nenhum registro na lista:
    if not registros_captura:
        
        print("\n======================================================")
        print("             Histórico de Capturas                    ")
        print("======================================================")
        print("\n       Não existe históricos de captura.")
        
    #Se existir registros na lista.
    else:
        print("\n======================================================")
        print("             Histórico de Capturas                    ")
        print("======================================================\n")
        for registro in registros_captura:
            print(
                f"Pokemon: {registro['Nome do pokemon']} - "  
                f"Capturas: {registro['Quantidade de capturas']}\n"
            )
                  


#Função para exibir as opções
def menu():
    print("\n======================================================")
    print("   Seja Bem vindo ao sistema de gerenciamento Pokemon.")
    print("======================================================")
    print("Escolha uma opção: \n")
    print(" 1 - Adicionar pokemon")
    print(" 2 - Listar Pokemons")
    print(" 3 - Remover Pokemons")
    print(" 4 - Atualizar nivel do pokemon")
    print(" 5 - Registar Captura pokemon")
    print(" 6 - Exibir histórico de capturas")
    print(" 7 - Sair\n")
    

#Função main com Loop    
def main():
    
    while True:
        menu()
        
        opcao = input ("Digite a opção Escolhida : \n")
        
        if opcao == "1":
            adicionar_pokemon()
        elif opcao == "2":
            listar_pokemon()
        elif opcao == "3":
            remover_pokemon()
        elif opcao == "4":
            atualizar_nivel()
        elif opcao == "5":
            registrar_captura()
        elif opcao == "6":
            exibir_historico()
        elif opcao == "7":
            print("Saindo. Obrigado...")
            break
            
        else:
            print ("Opção inválida, Digite uma opção válida.")   
            
#função principal iniciar
main()     