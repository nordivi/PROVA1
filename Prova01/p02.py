populacao_A = 80_000
taxa_A = 3/100
populacao_B = 200_000
taxa_B = 1.5/100

ano = 0
while populacao_A < populacao_B: # "ultrapasse ou iguale" --- por isso estritamente menor
    ano+=1 # Incremento do ano
    populacao_A*=(1+taxa_A) # Aumento de 3% da populacão de A
    populacao_B*=(1+taxa_B) # Aumento de 1.5% da população de B

print(f"Com população inicial de 80000 habitantes do país A e 200000 do país B, "
      f"com taxa de crescimento anual de, respectivamente, 3% e 1.5%, levariam {ano} "
      f"anos para que a população do país A ultrapasse ou iguale a população do país B, "
      f"resultando numa população final de A de {populacao_A} habitantes e de B de "
      f"{populacao_B} habitantes.")


