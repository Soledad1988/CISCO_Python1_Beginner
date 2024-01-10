#Escriba un programa que simule una alcancia. El programa solicitara una cantidad,
#que sera la cantidad de dinero que queremos ahorrar. A continuacion solicitara una y 
#otra vez las cantidades que se iran ahorrando, hasta que el total ahorrado iguale o 
#supere al objetivo. El programa no comprobara que las cantidades sean positivas

print('Alcancía')

objetivo = int(input('¿Cuanto dinero quiere ahorar? '))

ahorro = 0

while objetivo > ahorro:
    ahorro += int(input('Cuanto dinero quiere colocar en la alcancia? '))

print(f'Objetivo conseguido, usted ha ahorrado {ahorro}')