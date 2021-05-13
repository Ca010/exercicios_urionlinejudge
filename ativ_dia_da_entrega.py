diasDaSemana = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']

diaDaSemana = 0 

diaEntrada = input('Em qual dia da semana foi feita a compra? ')
  
qtdDias = int(input('Quantos dias para a entrega? '))

if qtdDias == 0:
    print('Chega hoje!')
else:
    indexDoDiaSemana = diasDaSemana.index(diaEntrada)
    novaLista = diasDaSemana[indexDoDiaSemana + 1:len(diasDaSemana)] + diasDaSemana[0:indexDoDiaSemana]

    diaEntrega = novaLista[qtdDias - 1]

    print('Sera entregue ',diaEntrega)

