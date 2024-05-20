#These values were obtained considering an average

multipliers = [
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

valor_mês = 409
mes_referencia = 2 # Janeiro

def calcular_consumo_medio(mês):
    return valor_mês / multipliers[mês]

consumo_medio = calcular_consumo_medio(mes_referencia)

print(f"Consumo médio: {consumo_medio:.2f}")