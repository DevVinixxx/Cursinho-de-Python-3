import random

def jogar():

    mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    #fruta = str(input("Qual a fruta que voce quer? "))

    #palavra_secreta = fruta.upper()
    #palavra_secreta = "mamao".upper()
    

    #for letra in palavra_secreta:
    #    letras_acertadas.append("_")
                # A funcção append(tem que ter um valor incluido dentro para ser adicionado em uma lista)
    erros = 0
    enforcou = False
    acertou = False

    #enquanto ( True and True)
    #not enforcou -> enforcou = False

    while(not acertou and not enforcou):

        chute = reqchute()
        
        if(chute in palavra_secreta):
            validchute(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1   # mesma coisa que -> erros = erros + 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        msg_vencendor(palavra_secreta)
    elif(enforcou):
        msg_perdedor(palavra_secreta)

def mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def reqchute():
    chute = input("Qual a letra? ")
    chute = chute.strip().upper()
    return chute

def validchute(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1 #index = index + 1  

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def msg_vencendor(palavra_secreta):
    print("Parabens você venceu!! a palavra era: ")
    print(palavra_secreta)

def msg_perdedor(palavra_secreta):
    print("Que pena!")
    print("Você perdeu, tente novamente")
    print("A fruta era: ", palavra_secreta)

if(__name__ == "__main__"):
    jogar()
