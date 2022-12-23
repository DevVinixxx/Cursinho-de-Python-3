#apenas uma lsita normal 
lista = [11122233344, 22233344455, 33344455566]
#append() adiciona algo mesmo que ja exista um valor igual a ele
lista.append(11122233344) #funciona!

#Conhecendo o set
#E agora? Será que o Python não oferece alguma coleção onde não podem existir elementos duplicados? Claro que existe uma coleção com esse propósito e ela se chama set.

#Veja o mesmo exemplo, mas agora inicializando um set:
colecao = {11122233344, 22233344455, 33344455566}
#Repare que usamos {} chaves para declarar os elementos iniciais. Pouca diferença comparando com as sequências, não?
#
#Adicionando elementos no set
#Para adicionar um elemento a um set devemos chamar a função add (ao invés da append):
colecao.add(44455566677) #vai adicionar pois não existe ainda
#E se usarmos um CPF que já existe? Não deve funcionar, certo? Vamos testar,e ver que o set vai ignorá-lo:
colecao.add(11122233344) #nao vai adicionar pois este CPF já existe!