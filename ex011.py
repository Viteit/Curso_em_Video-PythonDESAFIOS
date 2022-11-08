larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
a = larg * alt
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m²'.format(larg, alt, a))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format((a / 2)))
