frutas = ['Banana', 'Maca', 'Pera', 'Uva', 'Melancia', 'Jamelão']

fruta_pedida = input('Qual é a fruta que deseja consultar ?')

fruta_pedida = fruta_pedida.capitalize()

if(fruta_pedida in frutas):
    print ('Sim, temos a fruta.')
else:
    print ('Não temos a fruta.')