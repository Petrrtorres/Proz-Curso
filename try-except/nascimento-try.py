nome = str(input("Digite seu nome completo: "))

i=True

while i != False:
      ano_nascimento=int(input("Digite seu ano de nascimento: "))
      try:
            if ano_nascimento < 1922 or ano_nascimento > 2021:
                  print('O ano informado precisa ser entre 1922 e 2021.')
                  continue
            else:
                  idade = 2022 - ano_nascimento
                  print(f'Seu nome é {nome.upper()} e você tem {idade} anos.')
                  i = False
      except Exception as erro:
            print('Dados inválidos: ' + erro.__cause__)