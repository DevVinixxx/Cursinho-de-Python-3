#exemplo correto de como formatar todas as letras para maiusculo

#a variavel palavra tem seu valor definido em "alura 1"
palavra = "alura 1"

#Para alterar o valor dela com uma função é necessario colocar a variavel com um novo valor e adicionando a função!
palavra = palavra.upper()

print(palavra)

#exemplo de como formatar somente a primeira letra para maiusculo

palavra2 = "alura 2"

palavra2 = palavra2.capitalize()

print(palavra2)

#exemplo de como formatar todas as letras para minusculo

palavra3 = "Alura 3"

palavra3 = palavra3.lower()

print(palavra3)

#exemplo de como formatar tirando todos os espaços da palavra

palavra4 = "     alura 4    "

palavra4 = palavra4.strip()

print(palavra4)