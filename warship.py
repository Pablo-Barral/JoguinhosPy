# Aluno: Pablo da Cunha Barral (Individual)
import random

def desenhar_posicionamento(tabuleiro):  # Desenha o tabuleiro com os barcos do jogador
    print(" ")
    print(tabuleiro[0])
    print(tabuleiro[1])
    print(tabuleiro[2])
    print(tabuleiro[3])
    print(tabuleiro[4])
    print(" ")

def atualizar_possibilidades(tabuleiro):  # atualiza lista de possibilidades
    possibilidades = []
    for i in range(5):
        for j in range(5):
            possibilidades.append(tabuleiro[i][j])
    for k in range(25):
        if possibilidades[k] == "O " or possibilidades[k] == "W ":
            possibilidades[k] = "N/A"
    return possibilidades

def posicionar(posicao, tabuleiro):  # coloca os barcos no tabuleiro
    for i in range(5):
        for j in range(5):
            if posicao == tabuleiro[i][j]:
                tabuleiro[i][j] = "O "
    return tabuleiro

def verificar_espaco_brigue(posicao, tabuleiro, orientacao):  # verifica se o brigue cabe em um espaço
    if orientacao == "V":
        for i in range(5):
            for j in range(5):
                if posicao == tabuleiro[i][j]:
                    if i == 4:
                        return False
                    if tabuleiro[i + 1][j] == "O ":
                        return False
                    else:
                        return True
    else:
        for i in range(5):
            for j in range(5):
                if posicao == tabuleiro[i][j]:
                    if j == 4:
                        return False
                    if tabuleiro[i][j + 1] == "O ":
                        return False
                    else:
                        return True

def posicionar_brigue(posicao, tabuleiro, orientacao):  # posiciona o brigue no tabuleiro
    if orientacao == "V":
        for i in range(5):
            for j in range(5):
                if posicao == tabuleiro[i][j]:
                    tabuleiro[i][j] = "O "
                    tabuleiro[i+1][j] = "O "
    else:
        for i in range(5):
            for j in range(5):
                if posicao == tabuleiro[i][j]:
                    tabuleiro[i][j] = "O "
                    tabuleiro[i][j + 1] = "O "
    return tabuleiro

def desenhar_guerra(posicoes, aliados, inimigos):
    # desenha os dois tabuleiros, mostrando os tiros de cada um e os barcos do jogador separadamente
    for i in range(2):  # adiciona 0 ao início de números com 1 dígito, para manter a uniformidade da matriz
        for j in range (5):
            if len(aliados[i][j]) < 2:
                aliados[i][j] = f"0{aliados[i][j]}"
    print(" ")
    print("\033[92mSeus planos de guerra: \033[0m")
    print(posicoes[0])
    print(posicoes[1])
    print(posicoes[2])
    print(posicoes[3])
    print(posicoes[4])
    print("")
    print("\033[91mTiros do inimigo:\033[0m                   \033[96mSeus tiros: \033[0m")
    print(f"{aliados[0]}      {inimigos[0]}")
    print(f"{aliados[1]}      {inimigos[1]}")
    print(f"{aliados[2]}      {inimigos[2]}")
    print(f"{aliados[3]}      {inimigos[3]}")
    print(f"{aliados[4]}      {inimigos[4]}")
    print("")
    return "None"

def jogar(jogada, tabuleiro, mapa):  # dispara um morteiro no campo inimigo
    for i in range(5):
        for j in range(5):
            if jogada == mapa[i][j]:
                if tabuleiro [i][j] == "O ":
                    mapa[i][j] = "O "
                else:
                    mapa[i][j] = "W "
    return mapa

def procurar_vitoria(tabuleiro):  # procura todos os barcos e define se o jogo acabou
    pontos = 0
    for i in range(5):
        for j in range(5):
            if tabuleiro[i][j] == "O ":
                pontos = pontos + 1
    if pontos == 6:
        return True
    else:
        return False

# iniciar matrizes(feitas individualmente, de otura forma dava erro)
esquadra_aliada = [["01", "02", "03", "04", "05"], ["06", "07", "08", "09", "10"], ["11", "12", "13", "14", "15"],
                   ["16", "17", "18", "19", "20"], ["21", "22", "23", "24", "25"]]
esquadra_inimiga = [["1", "2", "3", "4", "5"], ["6", "7", "8", "9", "10"], ["11", "12", "13", "14", "15"],
                   ["16", "17", "18", "19", "20"], ["21", "22", "23", "24", "25"]]
possibilidades_jogador = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
                  "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"]
possibilidades_computador = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                  "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"]
tabuleiro_aliado = [["1", "2", "3", "4", "5"], ["6", "7", "8", "9", "10"], ["11", "12", "13", "14", "15"],
                   ["16", "17", "18", "19", "20"], ["21", "22", "23", "24", "25"]]
tabuleiro_inimigo = [["01", "02", "03", "04", "05"], ["06", "07", "08", "09", "10"], ["11", "12", "13", "14", "15"],
                   ["16", "17", "18", "19", "20"], ["21", "22", "23", "24", "25"]]
# iniciar estado de jogo e variavel controle
game_over = False
controle_vez = 2

# histórinha
print("\n\033[92mA guerra naval entre Inglaterra e Argentina começou! O rei inglês te contratou para comandar a esquadra britânica\033[0m")
print("Monte seu plano de guerra:\n")
desenhar_posicionamento(esquadra_aliada)

# jogador posiciona seus barcos
for i in range (4):
    posicao = input(f"Posicione a {i + 1}° escuna  ")
    while posicao not in possibilidades_jogador:
        print("\033[91mPosição inválida, tente novamente\033[0m")
        posicao = (input(f"\nPosicione a {i + 1}° escuna  "))
    esquadra_aliada = posicionar(posicao, esquadra_aliada)
    possibilidades_jogador = atualizar_possibilidades(esquadra_aliada)
    desenhar_posicionamento(esquadra_aliada)
# brigue posicionado separadamente
print("Agora posicione nosso brigue")
orientacao = input("Quer colocar na horizontal(H) ou vertical(V)?  ")
orientacao = orientacao.upper()
while orientacao != "H" and orientacao != "V":
    print("\033[91mOrientação inválida, tente novamente\033[0m")
    orientacao = (input("Quer colocar na horizontal(H) ou vertical(V)?  "))
    orientacao = orientacao.upper()
if orientacao == "V":
    posicao = input("Posicione o brigue(marque mais acima) ")
    while posicao not in possibilidades_jogador or verificar_espaco_brigue(posicao, esquadra_aliada, orientacao) == False:
        print("\033[91mO brigue não pode ficar aí! Tente novamente\n\033[0m")
        posicao = (input("Posicione o brigue(marque mais acima) "))
else:
    posicao = input("Posicione o brigue(marque mais à esquerda) ")
    while posicao not in possibilidades_jogador or verificar_espaco_brigue(posicao, esquadra_aliada, orientacao) == False:
        print("\033[91mO brigue não pode ficar aí! Tente novamente\n\033[0m")
        posicao = (input("Posicione o brigue(marque mais à esquerda) "))
esquadra_aliada = posicionar_brigue(posicao, esquadra_aliada, orientacao)
possibilidades_jogador = atualizar_possibilidades(esquadra_aliada)
desenhar_posicionamento(esquadra_aliada)

# computador posiciona os barcos
for i in range(6):
    posicao = -1
    while posicao not in possibilidades_computador:
        posicao = random.randint(1, 25)
        posicao = str(posicao)
    esquadra_inimiga = posicionar(posicao, esquadra_inimiga)
    possibilidades_computador = atualizar_possibilidades(esquadra_inimiga)

# histórinha
print("\n\033[93mEstamos com sorte! A Argentina está em crise e só conseguiu enviar 6 escunas para a batalha.")
print("\033[91mAcabe com eles capitão!\033[0m")
desenhar_guerra(esquadra_aliada, tabuleiro_aliado, tabuleiro_inimigo)

# reseta possibilidades, dessa vez para a batalha
possibilidades_computador = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                  "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"]
possibilidades_jogador = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
                  "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"]

while not game_over:  # loop principal do jogo
    if controle_vez % 2 == 0:
        jogadaJ = input("Escolha onde disparar um morteiro: ")
        while jogadaJ not in possibilidades_jogador:
            print("Não podemos disparar aí! Tente novamente.")
            jogadaJ = input("Escolha onde disparar um morteiro: ")
        jogar(jogadaJ, esquadra_inimiga, tabuleiro_inimigo)
        possibilidades_jogador = atualizar_possibilidades(tabuleiro_inimigo)
        game_over = procurar_vitoria(tabuleiro_inimigo)
        if game_over:
            vencedor = "jogador"
    else:
        jogadaC = -1
        while jogadaC not in possibilidades_computador:
            jogadaC = random.randint(1, 25)
            jogadaC = str(jogadaC)
            if len(jogadaC) < 2:
                jogadaC = "0" + jogadaC
        jogar(jogadaC, esquadra_aliada, tabuleiro_aliado)
        possibilidades_computador = atualizar_possibilidades(tabuleiro_aliado)
        game_over = procurar_vitoria(tabuleiro_aliado)
        if game_over:
            vencedor = "computador"
    desenhar_guerra(esquadra_aliada, tabuleiro_aliado, tabuleiro_inimigo)
    print("\033[94mW: Água    \033[91mO: Navio\033[0m")
    controle_vez = controle_vez + 1
print(f"\033[91mFim de jogo! \033[93mVitória do {vencedor}")

# mensagem de vitória
if vencedor == "jogador":
    print("Excelente trabalho, capitão, botou eles pra correr")
else:
    print("\033[91mEles são fortes demais, bater em retirada!")
