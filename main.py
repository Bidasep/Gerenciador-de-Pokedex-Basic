#O objetivo deste projeto é desenvolver um programa para gerenciar uma Pokédex (um banco de dados de Pokémon). O 
# programa deve permitir ao usuário realizar operações básicas de gerenciamento, como adicionar,
# listar, remover e atualizar dados de Pokémon, além de registrar capturas e exibir um histórico de 
# capturas. Este projeto ajuda a consolidar o uso de estruturas de dados em Python, como dicionários e 
# listas, bem como a aplicar conceitos de programação orientada a objetos, se desejado, e manipulação de entrada e saída.

#1 - Adicionar Pokémon:
# O programa deve pedir o nome do Pokémon, o tipo (como "Fogo", "Água", "Elétrico", etc.),
# e o nível (um número inteiro entre 1 e 100). Essas informações devem ser armazenadas no dicionário.

#Listar Pokémon:
# O programa deve exibir todos os Pokémon cadastrados no formato: 
# nome do Pokémon - tipo - nível. Os Pokémon devem ser listados em ordem alfabética.

#Remover Pokémon:
# O programa deve pedir o nome do Pokémon a ser removido. Caso o Pokémon 
# exista, ele será removido do dicionário. Se o Pokémon não existir, o programa exibirá uma mensagem de erro.

#Atualizar nível do Pokémon:
# O programa deve pedir o nome do Pokémon e o novo nível (um número inteiro entre 1 e 100).
# Se o Pokémon existir, o nível será atualizado. Caso contrário, será exibida uma mensagem de erro.

#Registrar captura de Pokémon:
# O programa deve pedir o nome do Pokémon e a quantidade de 
# vezes capturadas. O valor de capturas será atualizado, aumentando a quantidade de vezes que o 
# Pokémon foi capturado. Caso o Pokémon não exista, será exibida uma mensagem de erro.

#Exibir histórico de capturas:
# O histórico de capturas deve ser armazenado em uma lista, onde 
# cada entrada consiste no nome do Pokémon e a quantidade de vezes que foi capturado. Quando o 
# usuário escolher exibir o histórico de capturas, o programa deve mostrar todas as entradas feitas.

#Sair: 
# O programa deve encerrar sua execução quando o usuário escolher a opção de sair.

pokemons = []
registros_captura = []


def adicionar_pokemon():
    nome_pokemon = input ("Digite o nome do pokemon: ")
    
    for pokemon in pokemons:
        if pokemon["Nome do pokemon"].lower() == nome_pokemon.lower(): 
            print ("Pokemon já cadastrado.")
            return
        
        
    tipo_pokemon = input("Digite o tipo de pokemon:\n" "'Fogo' ,'Agua', 'Elétrico', 'Terra', 'Pedra' etc...  \n")    
        

    try:
        nivel_pokemon = int(input("Digite o nivel do pokemon entre 1 e 100\n"))
        
        if nivel_pokemon < 1 or nivel_pokemon > 100:
            print("Valor inválido, Digite um valor válido entre 1 e 100")
            return
        
    except ValueError:
        print("Nivel do Pokemon inválido, Digite um nivel válido.")
        return
    
    pokemons.append({
        "Nome do pokemon" : nome_pokemon,
        "Tipo do Pokemon" : tipo_pokemon,
        "Nivel do Pokemon" : nivel_pokemon
    })
    
    print (f"Pokemon {nome_pokemon} foi adicionado com sucesso, seu tipo é: {tipo_pokemon} e seu nivel é: {nivel_pokemon}")
    

def listar_pokemon():
    
    #for pokemon in pokemons():
    
    if not pokemons:
        print("Não há Pokemons na lista.\n")
    else:    
        print(pokemons)



def remover_pokemon():
    
    nome_pokemon = input("Digite o nome do pokemon a ser Removido:")
        
    
    for pokemon in pokemons:
        if pokemon["Nome do pokemon"].lower() == nome_pokemon.lower():
            pokemons.remove(pokemon)
            print(f"Pokemon {nome_pokemon} removido com sucesso")
            return
            
    print("Este Pokemon nao está cadastrado ou já foi deletado.")
      
    
    
   
def atualizar_nivel():
    
    nome_pokemon = input("Digite o nome do pokemon para atualizar a força:")
    
    for pokemon in pokemons:
        if pokemon["Nome do pokemon"].lower() == nome_pokemon.lower():
            try:
                novo_valor = int(input("Digite o novo valor do Nivel"))
                
                if novo_valor <1 or novo_valor >100 :
                    print("Valor inválido, digite um valor entre 1 e 100")
                    return
                
            except ValueError:
                print("Valor inválido.Digite um valor válido entre 1 e 100")
                return
            pokemon["Nivel do Pokemon"] = novo_valor
            
        
            
            print(f"O pokemon {nome_pokemon}, foi atualizado o Nivel para {novo_valor}.")
            return
            
        
    print("Este pokemon nao está cadastrado ou já foi removido")    
            
            
    

def registrar_captura():
    return print("registrar_captura")

def exibir_historico():
    return print("exibir_historico")
    



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
            print("Sainda. Obrigado...")
            break
            
        else:
            print ("Opção inválida, Digite uma opção válida.")   
            
#função principal iniciar

main()     