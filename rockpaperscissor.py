from random import *
partidas = 0
vitorias_computador = 0
vitorias_jogador = 0

while vitorias_jogador < 2 and vitorias_computador < 2:
    computador = randint(0, 2)
    jogador = int(input("Digite sua jogada: 0 para pedra, 1 para papel, 2 para tesoura:  "))

    if jogador < 0 or jogador > 2:
        print ("Jogada inválida")
    else:
        if computador == jogador:
            print("Empate")
        else:
            if computador == 0:
                if jogador == 1:
                    print("Vitória do Jogador,  Jogador: Papel  Computador: Pedra")
                    vitorias_jogador = vitorias_jogador + 1
                else:
                    print("Vitória do Computador, Jogador: Tesoura  Computador: Pedra")
                    vitorias_computador = vitorias_computador + 1
            else:
                if computador == 1:
                    if jogador == 0:
                        print("Vitória do Computador, Jogador: Pedra  Computador: Papel")
                        vitorias_computador = vitorias_computador + 1
                    else:
                        print("Vitória do Jogador, Jogador: Tesoura  Computador: Papel")
                        vitorias_jogador = vitorias_jogador + 1
                else:
                    if jogador == 1:
                        print("Vitória do Computador, Jogador: Papel  Computador: Tesoura")
                        vitorias_computador = vitorias_computador + 1
                    else:
                        print("Vitória do Jogador, Jogador: Pedra  Computador: Tesoura")
                        vitorias_jogador = vitorias_jogador + 1

if vitorias_jogador == 2:
    print("Vitória do jogador")
else:
    print("Vitória do computador")
print(f"Jogador: {vitorias_jogador} Máquina: {vitorias_computador}")