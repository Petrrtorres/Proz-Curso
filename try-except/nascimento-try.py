nome = str(input("Digite seu nome completo: "))
ano_nascimento = int(input("Digite seu ano de nascimento: "))

i=True
while i != False:
      try:
            if ano_nascimento > 1922 and ano_nascimento < 2021:
                  idade = 2022 - ano_nascimento
                  print(f'Seu nome é {nome.upper()} e você tem {idade} anos.')
                  i = False
      except Exception as erro:
            print(str('Dados inválidos: ' + erro.__cause__))