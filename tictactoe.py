# Aluno: Pablo da Cunha Barral (Individual)
def atualizar_possibilidades(tabuleiro):  # atualiza lista de possibilidades
    possibilidades = []
    for i in range(3):
        for j in range(3):
            possibilidades.append(tabuleiro[i][j])
    for k in range(9):
        if possibilidades[k] == "X" or possibilidades[k] == "O":
            possibilidades[k] = "N/A"
    return possibilidades

def jogar_x(tabuleiro, jogada_x):  # jogada do jogador X
    for i in range(3):
        for j in range(3):
            if jogada_x == tabuleiro[i][j]:
                tabuleiro[i][j] = "X"
    return tabuleiro


def jogar_o(tabuleiro, jogada_o):  # jogada do jogador O
    for i in range(3):
        for j in range(3):
            if jogada_o == tabuleiro[i][j]:
                tabuleiro[i][j] = "O"
    return tabuleiro


def encontrar_vitoria(tabuleiro):  # procura possíveis vitórias
    if tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2]:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0]:
        return True
    for j in range(3):
        if tabuleiro[0][j] == tabuleiro[1][j] and tabuleiro[1][j] == tabuleiro[2][j]:
            return True
        if tabuleiro[j][0] == tabuleiro[j][1] and tabuleiro[j][1] == tabuleiro[j][2]:
            return True
    else:
        return False

def definir_vencendor(tabuleiro):  # define quem ganhou em caso de não empate
    if tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2]:
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0]:
        return tabuleiro[0][2]
    for j in range(3):
        if tabuleiro[0][j] == tabuleiro[1][j] and tabuleiro[1][j] == tabuleiro[2][j]:
            return tabuleiro[0][j]
        if tabuleiro[j][0] == tabuleiro[j][1] and tabuleiro[j][1] == tabuleiro[j][2]:
            return tabuleiro[j][0]


# iniciar variaveis
rodadas = 0
game_over = False
tabuleiro = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
possibilidades = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
# codigo não conseguia ler matriz depois da linha 0, transformei em vetor

print(tabuleiro[0])
print(tabuleiro[1])
print(tabuleiro[2])
while game_over == False and rodadas <= 9:  # loop principal de jogo

    # jogador x
    jogada_x = (input("\nJogador X, digite sua jogada: "))
    while len(jogada_x) > 1:
        print("Jogada inválida, tente novamente")
        jogada_x = (input("\nJogador X, digite sua jogada: "))
    while jogada_x not in possibilidades:
        print("Jogada inválida, tente novamente")
        jogada_x = (input("\nJogador X, digite sua jogada: "))
    jogar_x(tabuleiro, jogada_x)
    possibilidades = atualizar_possibilidades(tabuleiro)
    print(tabuleiro[0])
    print(tabuleiro[1])
    print(tabuleiro[2])
    game_over = encontrar_vitoria(tabuleiro)
    rodadas = rodadas + 1
    if game_over == True or rodadas == 9:  # sai do loop caso X ganhe antes da jogada de O
        break

    # jogador O
    jogada_o = (input("\nJogador O, digite sua jogada: "))
    while len(jogada_o) > 1:
        print("Jogada inválida, tente novamente")
        jogada_o = (input("\nJogador O, digite sua jogada: "))
    while jogada_o not in possibilidades:
        print("Jogada inválida, tente novamente")
        jogada_o = (input("\nJogador O, digite sua jogada: "))
    jogar_o(tabuleiro, jogada_o)
    print(tabuleiro[0])
    print(tabuleiro[1])
    print(tabuleiro[2])
    game_over = encontrar_vitoria(tabuleiro)
    rodadas = rodadas + 1

vencedor = definir_vencendor(tabuleiro)
if game_over == True:
    print(f"\nFim de jogo. {vencedor} venceu, Parabéns")
else:
    print("\nEmpate, não há jogadas possíveis")
