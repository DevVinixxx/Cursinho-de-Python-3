import random

def jogar():
    print("==================================")
    print("Bem vindo ao Game de adivinhação")
    print("==================================")

    total_de_tentativas = 0

    numero_secreto = random.randrange(0,101)
    #usando randrange já gera um numero int, tendo apenas que definir o numero menor e o maior!
    #numero_secreto = round(random.random() * 100) -> gera um numero float(numero que é quebrado) 
    #Round() -> função usada para arredondar valores para int (inteiros)

    print("Qual o nivel de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Nivel: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    #Exemplo: "Em {} o Carnaval acontece em {} do dia {} até o dia {}".format(ano, mes, dia_ini, dia_fim)

    while (total_de_tentativas > 0):
        chute_str = input("Digite o seu número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("voce deve digitar um numero entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou!")
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")

        total_de_tentativas = total_de_tentativas - 1

    print("O numero secreto era:", numero_secreto)
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()