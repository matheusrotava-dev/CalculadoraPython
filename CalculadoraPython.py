import sys
import math

def calculate():

 def again():
     calcular_de_novo = input('quer usar a calculadora de novo ? digite "S" pra sim e "N" pra não: ')
     if calcular_de_novo.upper() == 'S':
         calculate()
     elif calcular_de_novo.upper() == 'N':
         print('obrigado por usar')
     else:
         again()


 print('1 - SOMA')
 print('2 - SUBTRAÇÃO')
 print('3 - MULTIPLICAÇÃO')
 print('4 - DIVISÃO')
 print('5 - EXPONENCIAÇÃO')
 print('6 - RAIZ QUADRADA')
 print('7 - SAIR DO PRAGAMA')
 operacao = int(input('qual operação deseja fazer ?'))

 if operacao == 7:
    sys.exit('você encerrou o programa.')

 if operacao == 1:
    numero1 = float(input('digite o primeiro número da operação: '))
    numero2 = float(input('digite o segundo número da operação: '))
    resultado = (numero1+numero2)
    print(f'o resultado da operação é: {resultado:0.2f}')

 if operacao == 2:
        numero1 = float(input('digite o primeiro número da operação: '))
        numero2 = float(input('digite o segundo número da operação: '))
        resultado = (numero1-numero2)
        print(f'o resultado da operação é: {resultado:0.2f}')

 if operacao == 3:
    numero1 = float(input('digite o primeiro número da operação: '))
    numero2 = float(input('digite o segundo número da operação: '))
    resultado = (numero1*numero2)
    print(f'o resultado da operação é: {resultado:0.2f}')

 if operacao == 4:
    numero1 = float(input('digite o primeiro número da operação: '))
    numero2 = float(input('digite o segundo número da operação: '))
    if numero1 == 0:
        numero1 = float(input('0 é um número inválido pra essa operação, digite novamente: '))
    if numero2 == 0:
            numero2 = float(input('0 é um número inválido pra essa operação, digite novamente: '))
    resultado = (numero1/numero2)
    print(f'o resultado da operação é: {resultado:0.2f}')

 if operacao == 5:
    numero1 = int(input('digite primeira a base: '))
    numero2 = int(input('digite o expoente: '))
    resultado = (numero1**numero2)
    print(f'a operação ficou assim: {numero1}^{numero2}, o resultado é: {resultado}')

 if operacao == 6:
    numero1 = float(input('digite o número que você quer saber a raiz quadrada: '))
    raiz = math.sqrt(numero1)
    print(f'a raiz quadrada de {numero1} é: {raiz}')

 again()

calculate()







