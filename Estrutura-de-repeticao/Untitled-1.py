

print("Quantas rodas tem o veiculo?")
quantidade_de_rodas = int(input())
print("Quantas pessoas cabem no veículo?")
quantidade_de_pessoas = int(input())
print("Quanto pesa o veículo?")
peso_kg = int(input())


if (quantidade_de_rodas == 2 or 3) and (quantidade_de_pessoas == 2) and (peso_kg < 3500):
    print("Categoria A")
elif (quantidade_de_rodas == 4) and (quantidade_de_pessoas <= 8) and (peso_kg <= 3500):
    print("Categoria B")
elif (quantidade_de_rodas >= 4) and (peso_kg >= 3500) and (peso_kg <= 6000):
    print("Categoria C")
elif (quantidade_de_rodas >= 4) and (quantidade_de_pessoas > 8) and (peso_kg > 3500) and (peso_kg <= 6000):
    print("Categoria D")
elif (quantidade_de_rodas >= 4) or (quantidade_de_pessoas >= 8) and (peso_kg > 6000):
    print("Categoria E")
else: 
    print("Veículo não categorizado!")