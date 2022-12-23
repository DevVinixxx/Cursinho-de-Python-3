import forca
import adivinhacao

#Notas antigas, porem ja tem novas atualizações. Tais como: os exemplos de fazer uma função -> def nome_da_função():
    #TODA VEZ QUE QUISER IMPORTAR UMA BIBLIOTECA COLOQUE NO INICIO DO CODIGO
    #MAS O MESMO NAO SE APLICA PARA ARQUIVOS QUE VC QUEIRA EXECUTAR INDIVIDUALMENTE
    #ARQUIVOS QUE VC QUER EXECUTAR INDIVIDUALMENTE SÓ COLOQUE DENTRO DO SEU "IF()"

def jogos():
    print("**********************************")
    print("****Bem Vindo! Escolha um jogo****")
    print("**********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual o jogo? "))

    if(jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao.jogar()
        #caso queira executar o arquivo dentro de uma pasta, especifique o caminho EX: Import pasta.arquivo

if(__name__ == "__main__"):
    jogos()
