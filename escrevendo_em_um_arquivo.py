#arquivo = open("arquivo que vc quer abrir", "aqui o parametro") Exemplo a baixo
arquivo = open("palavras.txt", "w") #Parametros: W -> usado para escrever em algum arquivo w = write / a = append adiciona um texto em um arquivo sem apagar nada / r = read lê um arquivo
arquivo.write("banana")
#6
arquivo.write("melancia")
#8
arquivo.close()

arquivo = open("palavras.txt", "a")
arquivo.write("morango\n")
#8
arquivo.write("manga\n")

arquivo.close()
#6
#Ao fechar o arquivo e verificar novamente o seu conteúdo, vemos:

#bananamelanciamorango
#manga
#A palavra morango ainda ficou na mesma linha, mas como especificamos na sua adição que após a palavra deverá ter uma quebra de linha, a palavra manga foi adicionada abaixo, em uma nova linha.

#Por fim, vamos mover esse arquivo para dentro do nosso projeto, e ajeitar as suas palavras, quebrando as linhas. Ele ficará assim:

#banana
#melancia
#morango
#manga 

