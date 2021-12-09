# Aluno: Pablo da Cunha Barral (Individual)
import random

def sortear_palavra():  # cortesia do professor Marco Antônio
    arquivo = open("br-sem-acentos.txt")
    linhas = arquivo.readlines()
    palavra = ''
    while len(palavra) < 3 or len(palavra) > 9:  # tamanho aceitável modificado
        sorteio = random.randint(0, len(linhas)) + 1
        palavra = linhas[sorteio]
    palavra = palavra.upper()
    arquivo.close()
    return palavra

def contar_acerto(letra, palavra, palavra_atual):  # coloca a(s) letra(s) na palavra
    for i in range(len(palavra) - 1):
        if letra == palavra[i]:  # substitui letras em caso de acerto
            palavra_atual[i] = palavra[i]
        else:
            if palavra_atual[i] != "_":  # mantem letras certas na palavra
                palavra_atual[i] = palavra[i]
            else:  # mantem os espaços vazios para letras não "acertadas"
                palavra_atual[i] = "_"
    return palavra_atual

def converter_string(vetor_atual):  # Converte o vetor palavra_atual para uma string
    resposta_string = ""
    for i in range(len(vetor_atual)):
        resposta_string = resposta_string + vetor_atual[i]
    return resposta_string


# inicializar variaveis
tentativas_restantes = 6  # contagem regressiva para mensagem (linha 61)
erros = []  # lista de letras testadas e não na palavra
palavra_atual = []  # palavra com letras nos lugares certos

palavra = sortear_palavra()
for i in range(len(palavra)-1):  # iniciar template da palavra vazia
    palavra_atual.append("_")

print(f"Palavra: {converter_string(palavra_atual)}")
while tentativas_restantes > 0 and "_" in palavra_atual:  # loop principal do jogo
    letra = input("Digite uma letra: ")
    letra = letra.upper()

    if len(letra) > 1:
        print("Digite apenas uma letra por vez")

    else:

        palavra_atual = contar_acerto(letra, palavra, palavra_atual)

        if letra not in palavra:  # contar erro
            if letra not in erros:
                erros.append(letra)
                print(f" \n{letra} não pertence à palavra")
                tentativas_restantes = tentativas_restantes - 1

        # interface do usuário
        print(f"{tentativas_restantes} tentativas restantes")
        print(f"Letras testadas: {erros}")
        print(f"Palavra: {converter_string(palavra_atual)} \n")

# fim de jogo, definir vitória ou derrota
if tentativas_restantes == 0:
    print(f"Você perdeu, a palavra era {palavra}")
else:
    print(f"Você venceu com {tentativas_restantes} tentativas restantes, a palavra era {palavra}")
