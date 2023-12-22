def calculadora (operacao, num1, num2): 
          if operacao == 1:
            resultado=num1+num2
          elif operacao == 2:
            resultado=num1-num2
          elif operacao == 3:
            resultado=num1*num2
          elif operacao == 4:
            resultado=num1/num2
          elif operacao >= 5 or operacao <= 0:
            resultado=0
            print("Operação inexistente")

          return resultado
      
     


#Programa principal
i=None

while i != 0:

  print("Selecione uma das operações abaixo: ") 
  print(" 1: Soma \n 2: Subtração \n 3: Multiplicação \n 4: Divisão \n 0: Sair \n")

  operacao = int(input("Digite o número da sua operação, ou [0] para sair: "))
  if operacao == 0 or operacao < 0 or operacao >= 5:
      i = 0
      print("Fim da operação.")
  else: 
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    resposta = calculadora(operacao, num1, num2)
    print("\n O resultado é: " + str(resposta) + '\n')
    print('--' *30)