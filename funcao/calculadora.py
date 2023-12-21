def calculadora (num1, operacao, num2): 
      if operacao == 1:
        resultado=num1+num2
      elif operacao == 2:
        resultado=num1-num2
      elif operacao == 3:
        resultado=num1*num2
      elif operacao == 4:
        resultado=num1/num2
      else:
        resultado=0
        print("Operação inexistente, o resultado é: " + str(resultado))

      return resultado

num1 = int(input("Digite um número: "))
operacao = int(input("Digite uma operação: "))
num2 = int(input("Digite o segundo número: "))     

resultado = calculadora(num1,operacao,num2)
print(resultado)