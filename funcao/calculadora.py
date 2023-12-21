def calculadora (num1, operacao, num2):
      num1 =0
      num2 = 0
      operacao = ' '

      if operacao == '1':
        resultado=num1+num2
      elif operacao == '2':
        resultado=num1-num2
      elif operacao == '3':
        resultado=num1*num2
      elif operacao == '4':
        resultado=num1/num2
      else:
        resultado=0
        print("Operação inexistente, o resultado é: " + str(resultado))


calculadora (3, '4', 8)