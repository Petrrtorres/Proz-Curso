def calculadora (num1, num2, operacao): 
    while operacao != 0:
          if operacao == 1:
            resultado=num1+num2
          elif operacao == 2:
            resultado=num1-num2
          elif operacao == 3:
            resultado=num1*num2
          elif operacao == 4:
            resultado=num1/num2
          elif operacao >= 5:
            resultado=0
            print("Operação inexistente, o resultado é: ")

          return resultado
      
     


#Programa principal

print(" 1: Soma \n 2: Subtração \n 3: Multiplicação \n 4: Divisão \n 0: Sair")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = int(input("Digite o número da sua operação, ou [0] para sair: "))

resposta = calculadora(num1, num2, operacao)
print(resposta)