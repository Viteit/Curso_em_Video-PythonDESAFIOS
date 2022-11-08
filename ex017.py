from math import hypot
co = float(input('Compimento do cateto oposto:'))
ca = float(input('Compimento do cateto adjacente:'))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print('A hipotenusa vai medir {:.2f}'.format(hi))
