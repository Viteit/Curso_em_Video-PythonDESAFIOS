salario = float(input('Qual é o salário do funcionário: '))
if salario > 1250.00 :
    print('Você recebrá um aumento de 10%, e seu salário será R${:.2f}'.format((salario * 10 / 100) + salario))
elif salario <= 1250.00 :
    print('Você receberá um aumento de 15%, e seu salário será R${:.2f}'.format((salario * 15 / 100) + salario))
