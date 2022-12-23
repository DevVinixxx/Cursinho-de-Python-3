#Formatação de floats
#Agora vamos trocar o exemplo, e formatar um valor em reais, por exemplo:

print("R$ {}".format(1.59))
#R$ 1.59
#Só que um valor pode ter vários tamanhos e até duas casas decimais, por exemplo:

#1.59
#45.9
#1234.97
#O ideal é que esses valores sempre tenham a mesma formatação:

 #  1.59
 # 45.9
#1234.97
#Então precisamos preencher as lacunas, os espaços em branco. E a função format faz isso para nós. Primeiro precisamos dizer para ela que estamos recebendo um valor do tipo float, passando :f dentro das chaves da string:

print("R$ {:f}".format(1.59))
#R$ 1.590000
#Podemos reparar que só de dizer que estamos passando um float, a formatação já muda, mas podemos manipulá-la, modificá-la, dizendo quantos números devem vir antes e depois do ponto. Queremos que após o ponto tenha apenas 2 números, logo:

print("R$ {:.2f}".format(1.59))
#R$ 1.59
#Podemos testar passando um número de apenas uma casa decimal:

print("R$ {:.2f}".format(1.5))
#R$ 1.50
#Ótimo, agora vamos testar com um número maior:

print("R$ {:.2f}".format(1.5))
#R$ 1.50
print("R$ {:.2f}".format(1234.50))
#R$ 1234.50
#Mas queremos que o ponto fique sempre no mesmo local, ou seja, ele deve ser o quinto caractere. Para essa formatação, precisamos dizer quantos caracteres o número terá no máximo, no nosso caso são 7 (4 números, mais o ponto, mais as duas casas decimais). Então vamos passar o valor 7 dentro das chaves também:

print("R$ {:7.2f}".format(1234.50))
#R$ 1234.50
print("R$ {:7.2f}".format(1.5))
#R$    1.50
#Ou seja, dos 7 caracteres, os três últimos serão o ponto mais dois números das casas decimais.

#Agora espaços ficam na frente quando um número for menor! Deixando o ponto sempre como quinto caractere. Se quisermos preencher os espaços em branco com zeros, é só passar um 0 antes do 7:

print("R$ {:07.2f}".format(1.5))
#R$ 0001.50
#Formatação de inteiros
#Conseguimos formatar números inteiros também, não só números flutuantes. Para números inteiros, passamos a letra d:

print("R$ {:07d}".format(4))
#R$ 0000004