# Faça um programa que leia três números e mostre-os em ordem decrescente

# Já que não especifica que são inteiros, usarei o float.
numeros = []
for i in range(3):
    n = float(input(f"Digite o número {i+1}: "))
    numeros.append(n)

numeros.sort(reverse=True) # Organiza os números de forma descrescente inplace

# Printando com string formatada
print(f"Os números inputados de forma decrescente são: {numeros[0]}, {numeros[1]} e {numeros[2]}!")

# Poderia também printar linha a linha de forma mais direta --- apenas descomentar:
# for x in numeros: # Note que a lista já está com os números em ordem.
#     print(x)

