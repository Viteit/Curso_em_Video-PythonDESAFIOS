velocidade_do_carro = float(input('Qual sua velocidade: '))
if velocidade_do_carro <= 80:
    print('Parabéns, continue andando no limite de velocidade!')
else:
    print('Você exedeu o limite de velocidade e foi multado em R${:.2f}'.format((velocidade_do_carro - 80) * 7))
