frutas = ["maçã", "banana", "laranja", "melancia"]

lista = []
for fruta in frutas:
    lista.append(fruta.upper())

#Metodo Correto

lista = [fruta.upper() for fruta in frutas]