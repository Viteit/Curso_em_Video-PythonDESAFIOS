distancia_da_viagem = float(input('Qual a distância da viagem: '))
if distancia_da_viagem <= 200:
    print('A passagem irá custar R${:.2f}'.format(distancia_da_viagem * 0.50))
elif distancia_da_viagem > 200:
    print('A passagem irá custar R${:.2f}'.format(distancia_da_viagem * 0.45))