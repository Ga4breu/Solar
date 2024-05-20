#These values are a reference, may vary.

multiplicadores = [
1.5475651459866313, #JAN
 1.39493078241106,  #FEV
 1.373038434143632, #MAR
 1.220613429762475, #ABR
 0.7667224082950573, #MAI
 0.8133878856994736,    #JUN
 0.6623251107129187,    #JUL
 0.6090001102786906,    #AGO
 0.7218510186478773,    #SET
 0.8184622029476277,    #OUT
 1.0193153171868314,    #NOV
 1.0527509390864467   #DEZ

]

def calcular_consumo_mensal(valor_medio):

    # Calcular estimativas de consumo mensal
    consumo_mensal = [valor_medio * multiplicador for multiplicador in multiplicadores]
    
    return consumo_mensal

# Coloque o consumo médio do cliente aqui.
valor_medio = 1000
consumo_estimado = calcular_consumo_mensal(valor_medio)

# Nomes dos meses para imprimir os resultados
nomes_dos_meses = [
    "JAN", "FEV", "MAR", "ABR", "MAI", "JUN",
    "JUL", "AGO", "SET", "OUT", "NOV", "DEZ"
]

# Imprimir os resultados
for nome_do_mes, consumo in zip(nomes_dos_meses, consumo_estimado):
    print(f"{nome_do_mes}: {consumo:.2f}")
