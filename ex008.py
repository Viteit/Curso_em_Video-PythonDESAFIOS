n = float(input('Uma distância em metros:'))
#km = n / 1000
#hm = n / 100
#dam = n / 10
#dm = n * 10
#cm = n * 100
#mm = n * 1000
#print('A medida de {}m corresponde a: \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(n, km, hm, dam, dm, cm, mm))
print('A medida de {}m corresponde a: \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(n, (n / 1000), (n / 100), (n / 10), (n * 10), (n * 100), (n * 1000)))
