try:
      nome_completo = str(input("Digite seu nome completo: "))
      ano_nascimento = int(input("Digite seu ano de nascimento: "))
      
      if ano_nascimento < 1922 and ano_nascimento > 2021:
         idade = 2022 - ano_nascimento 
      else:
         print('Ano de nascimento inválido. \n' )

except Exception as erro: 
      print(erro.__cause__)

else:
      print(f'Seu nome é {nome_completo.upper()} e sua idade é {idade}')