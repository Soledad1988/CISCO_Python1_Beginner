# Escriba un programa que pida dos numeros enteros y que escriba si el mayor es multiplo del menor

num1 = int(input('Escriba un numero: '))
num2 = int (input('Escriba otro numero: '))



#if (num1 >= num2):
  #  if num1%num2 ==0:
  #      print(f'{num1} es multiplo de {num2}')
  #  else:
  #      print(f'{num1} no es multiplo de {num2}')
#elif (num2 >= num1):
  #  if num2%num1==0:
  #      print(f'{num2} es multiplo de {num1}')
  #  else:
  #     print(f'{num2} no es multiplo de {num1}')

#mejorando el programa anterior, se solicita cuando se escriben valores
#negativos o nulos

if num1 >= num2:
    if num1 % num2 != 0:
        print(f"{num1} no es múltiplo de {num2}.")
    else:
        print(f"{num1} es múltiplo de {num2}.")
else:
    if num2 % num1 != 0:
        print(f"{num2} no es múltiplo de {num1}.")
    else:
        print(f"{num2} es múltiplo de {num1}.")