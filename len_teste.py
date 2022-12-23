total = 0

palavra = "python rocks!"

acabou = False

print(len(palavra))

#   len() é usado para contar caracteres dentro de uma string incluindo os espaços

while (not acabou):
    acabou = (total == len(palavra)) 
    total = total + 1
print(total - 1)