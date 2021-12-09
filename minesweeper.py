# Aluno: Pablo da Cunha Barral (individual)

import random

def montar_mapa(tamanho, quantidade):  # monta o mapa sem bombas
    controle = 1
    mapa = []
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            linha.append(controle)
            controle = controle + 1
        mapa.append(linha)
    posicionar_bombas(mapa, quantidade)
    return mapa

def posicionar_bombas(mapa, quantidade):  # posiciona as bombas no mapa
    possibilidades = []  # controle para evitar bombas repetidas
    for i in range(len(mapa)):
        for j in range(len(mapa)):
            possibilidades.append(mapa[i][j])
    for k in range(quantidade):
        bomba = -1  # posição da bomba (resetada para -1 a cada loop)
        while bomba not in possibilidades:
            bomba = random.randint(1, len(mapa) ** 2)
        for i in range(len(mapa)):
            for j in range(len(mapa)):
                if bomba == mapa[i][j]:
                    mapa[i][j] = 0
        for l in range(len(possibilidades)):
            if possibilidades[l] == bomba:
                possibilidades[l] = -2
    return mapa

def jogar(linha, coluna, posicao_bombas, tabuleiro):  # faz a jogada e abre o tabuleiro por recursão
    if posicao_bombas[linha][coluna] == "0":  # acertou bomba, condição de derrota
        return "game over"
    else:  # não acertou bomba, prosseguir
        if posicao_bombas[linha][coluna] != " ":  # substitui tabuleiro por mapa quando for um número
            tabuleiro[linha][coluna] = posicao_bombas[linha][coluna]
        else:  # substitui tabuleiro por mapa quando não for número
            tabuleiro[linha][coluna] = posicao_bombas[linha][coluna]
            if linha < (len(tabuleiro) - 1):
                if tabuleiro[linha + 1][coluna] != "0" and tabuleiro[linha + 1][coluna] == "?":
                    jogar(linha + 1, coluna, posicao_bombas, tabuleiro)
            if linha > 0:
                if tabuleiro[linha - 1][coluna] != "0" and tabuleiro[linha - 1][coluna] == "?":
                    jogar(linha - 1, coluna, posicao_bombas, tabuleiro)
            if coluna < (len(tabuleiro)- 1):
                if tabuleiro[linha][coluna + 1] != "0" and tabuleiro[linha][coluna + 1] == "?":
                    jogar(linha, coluna + 1, posicao_bombas, tabuleiro)
            if coluna > 0:
                if tabuleiro[linha][coluna - 1] != "0" and tabuleiro[linha][coluna - 1] == "?":
                    jogar(linha, coluna - 1, posicao_bombas, tabuleiro)

    return tabuleiro

def montar_tabuleiro(tabuleiro):  # monta tabuleiro visível para jogador
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            tabuleiro[i][j] = "?"
    return tabuleiro

def contar_bomba(campo):  # conta quantas bombas estão adjacentes a cada casa
    # lógica de contagem adaptada da fornecida pelo professor Marco Antônio
    for i in range(len(campo)):
        for j in range(len(campo)):
            if campo[i][j] != 0:
                linha_inicial = i - 1
                if linha_inicial < 0:
                    linha_inicial = 0
                linha_final = i + 1
                if linha_final > len(campo) - 1:
                    linha_final = len(campo) - 1
                coluna_inicial = j - 1
                if coluna_inicial < 0:
                    coluna_inicial = 0
                coluna_final = j + 1
                if coluna_final > len(campo) - 1:
                    coluna_final = len(campo) - 1

                valor = 1
                for l in range(linha_inicial, linha_final + 1):
                    for c in range(coluna_inicial, coluna_final + 1):
                        if campo[l][c] == 0:
                            valor = valor + 1
                if valor != 0:
                    campo[i][j] = valor

    # substituição do mapa pelo valor em str (ou " " caso não seja um número) *conteúdo original*
    for i in range(len(campo)):
        for j in range(len(campo)):
            if campo[i][j] == 1:
                campo[i][j] = 10  # casa que vale 1 (ou seja, sem bombas perto) passa a valer 10
            if campo[i][j] != 0:
                campo[i][j] = campo[i][j] - 1  # subtrai 1 de todas as não-bombas
            campo[i][j] = str(campo[i][j])  # transforma os valores em string para serem exibidos no mapa
            if campo[i][j] == "9":
                campo[i][j] = " "  # tratamento das casas vazias sem bombas perto
    return campo

def verificar_tabuleiro(mesa, bombas):  # verifica se jogador ganhou
    contador = 0
    for i in range(len(mesa)):
        for j in range(len(mesa)):
            if mesa[i][j] == "?":
                contador = contador + 1
    if contador == bombas:
        return True

# customizar tamanho do tabuleiro
tamanho = "N/A"
while tamanho == "N/A":
    print()
    tamanho = input('Digite o tamnho do tabuleiro (mínimo 4, máximo 25 (máximo recomendado 13), digite 0 para o valor padrão): ')
    if tamanho == "0":
        tamanho = 9
    else:
        if tamanho.isnumeric():
            tamanho = int(tamanho)
            if tamanho > 25:
                tamanho = 25
            if tamanho < 4:
                tamanho = 4
        else:
            tamanho = "N/A"

# customizar número de bombas
qtde_bombas = "N/A"
while qtde_bombas == "N/A":
    qtde_bombas = input(f'Digite a quantidade de bombas(mínimo 1, máximo {int(tamanho**2 - tamanho*2)}, digite 0 para o valor padrão): ')
    if qtde_bombas == "0":
        qtde_bombas = tamanho + 1
    else:
        if qtde_bombas.isnumeric():
            qtde_bombas = int(qtde_bombas)
            if qtde_bombas < 1:
                qtde_bombas = 1
            if qtde_bombas > tamanho**2 - tamanho*2:
                qtde_bombas = tamanho**2 - tamanho*2
        else:
            qtde_bombas = "N/A"

game_over = False  # variável de controle de fim de jogo

mapa = montar_mapa(tamanho, qtde_bombas)
tabuleiro = montar_tabuleiro(mapa)  # monta o tabuleiro visível para o jogador
mapa = montar_mapa(tamanho, qtde_bombas)  # gera mapa outra vez porque mapa espelhava tabuleiro
mapa = contar_bomba(mapa)  # substitui o mapa pela versão com números perto de bombas



# ajustar linhas para interface
linhas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
          "X", "Y", "Z"]
linhas_validas = []
for i in range(tamanho):
    linhas_validas.append(linhas[i])

# exibir interface
indice_coluna = []
indice_coluna_string = ""
for j in range(tamanho):
    indice_coluna.append(j)
    indice_coluna_string = f"{indice_coluna_string + str(indice_coluna[j])}    "
print(f"    {indice_coluna_string}")
for i in range(tamanho):
    print(f"{linhas[i]} {tabuleiro[i]}")

# loop principal de jogo
while not game_over:
    ocupado = True
    while ocupado:
        # resetar variáveis de jogo
        ocupado = False
        linha = "N/A"
        coluna = -1
        # input de jogadas
        while linha not in linhas_validas:
            linha = input(f"\nDigite a linha que quer jogar (A-{linhas[tamanho - 1]}): ")
            linha = linha.upper()
            if linha == "CCBBEDEDBA":  # konami code: exibe o mapa (ferramenta de trapaça)
                for i in range(tamanho):
                    print(mapa[i])
            if linha not in linhas_validas and linha != "CCBBEDEDBA":
                print("Linha inválida, tente novamente")
        while coluna not in range(tamanho):
            coluna = (input(f"\nDigite a coluna que quer jogar (0-{tamanho-1}): "))
            if coluna.isnumeric():
                coluna = int(coluna)
            if coluna not in range(tamanho):
                print("Coluna inválida, tente novamente")
        for i in range(tamanho):  # transforma a letra (linha) em número para o computador ler
            if linhas[i] == linha:
                linha = i
        if tabuleiro[linha][coluna] != "?":  # evita jogadas repetidas
            print(f"\n\033[91m{linhas[linha]}{coluna} já está aberto, tente novamente\033[0m")
            ocupado = True
    tabuleiro = jogar(linha, coluna, mapa, tabuleiro)
    if tabuleiro == "game over":
        game_over = True
    else:
        print()
        print(f"    {indice_coluna_string}")
        for i in range(tamanho):
            print(f"{linhas[i]} {tabuleiro[i]}")
        if verificar_tabuleiro(tabuleiro, qtde_bombas):
            game_over = True

# pós-jogo, vitória ou derrota
if tabuleiro == "game over":
    print()
    print(f"    {indice_coluna_string}")
    for i in range(tamanho):
        print(f"{linhas[i]} {mapa[i]}")
    print(f"\n\033[91mVocê perdeu, {linhas[linha]}{coluna} era uma bomba\033[0m")
else:
    print("\n\033[96mParabéns, você venceu!\033[0m")
