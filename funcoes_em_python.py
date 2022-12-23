#Função append() -> serve para adicionar um valor dentro de uma lista -< list() ou de uma tupla -> tuple()
#Na linha abaixo temos uma tupla com valores
nomes = ("nico", "Douglas", "Flavio", "Daniel")

nomes = list(nomes)

nomes.append("fabioaaa")

print(nomes)

#função usada para localizar valores 

precos = [1525,1120,1464,1200,1330,1356,1312,1531,1232, 1234,1250,1114,1553,1147,1303,1296,1309,1404,1479,1376]

#Para achar o valor Minimo
print(min(precos))
#Para achar o valor Maximo
print(max(precos))


#!!!!!!!!!FORMATAÇÕES!!!!!!
#criei essa def somente para tirar o bug
def alt():
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