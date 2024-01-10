#Escriba un programa que pida el año actual y un año cualquiera
#y que escriba cuantos años han pasado desde ese año o cuantos
# años faltan para llegar a ese año

print('-'*120)
print('COMPARADOR DE AÑOS')
print('-'*120)

actual = int(input('¿En que año estamos?: '))
otro = int(input('Escriba un año cualquiera: '))

if actual > otro:
    resultado = actual - otro
    print(f'desde el año {otro} han pasado {resultado}')
else:
    resultado = otro - actual
    print(f'Para llegar al año {otro}, faltan {resultado} años')