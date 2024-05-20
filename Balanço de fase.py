def balancear_sistema_trifasico(potencias_inversores, limite_corrente_fase):
    """
    Equilibra a potência dos inversores fornecidos em um sistema trifásico
    com base no limite de corrente por fase e nas potências nominais dos inversores fornecidas.

    Parâmetros:
    - potencias_inversores: Lista de potências nominais de cada inversor (em kW).
    - limite_corrente_fase: Corrente máxima permitida por fase (em A).

    Retorna:
    - Dicionário com as fases como chaves e seus inversores atribuídos com corrente total por fase,
      ou uma mensagem de erro se a configuração não for viável.
    """
    # Constantes
    tensao_linha_linha = 220  # Tensão entre fases (V)

    # Inicializa as cargas e atribuições das fases
    fases = {'L1': [], 'L2': [], 'L3': []}
    correntes_fase = {'L1': 0, 'L2': 0, 'L3': 0}

    # Função para encontrar as duas fases adjacentes menos carregadas
    def obter_fases_adjacentemente_menos_carregadas():
        fases_ordenadas = sorted(correntes_fase.items(), key=lambda x: x[1])
        return fases_ordenadas[0][0], fases_ordenadas[1][0]

    # Verifica se cada inversor pode se adequar aos limites de corrente
    for potencia in potencias_inversores:
        # Calcula a corrente por fase (tensão linha-linha)
        corrente_por_fase = potencia * 1000 / tensao_linha_linha

        # Obtém as duas fases adjacentes menos carregadas
        fase_primaria, fase_secundaria = obter_fases_adjacentemente_menos_carregadas()

        # Verifica se ambas as fases podem suportar a corrente
        if correntes_fase[fase_primaria] + corrente_por_fase <= limite_corrente_fase and \
                correntes_fase[fase_secundaria] + corrente_por_fase <= limite_corrente_fase:
            # Adiciona este inversor a ambas as fases
            fases[fase_primaria].append(potencia)
            fases[fase_secundaria].append(potencia)
            correntes_fase[fase_primaria] += corrente_por_fase
            correntes_fase[fase_secundaria] += corrente_por_fase
        else:
            return "Erro: A configuração atual não pode acomodar os inversores especificados dentro dos limites das fases."

    return fases, correntes_fase


# Exemplo de uso:
if __name__ == "__main__":
    # Lista exemplo de potências nominais dos inversores em kW
    potencias_inversores = [10,10,5]
    # Exemplo de corrente máxima suportada por cada fase (em A)
    limite_corrente_fase = 100
    # Chama a função para balancear o sistema
    resultado = balancear_sistema_trifasico(potencias_inversores, limite_corrente_fase)

    # Imprime os resultados
    if isinstance(resultado, str):
        print(resultado)  # Mensagem de erro
    else:
        fases, correntes_fase = resultado
        for fase, potencias_atribuidas in fases.items():
            print(f"{fase}: {potencias_atribuidas} (Corrente Total: {correntes_fase[fase]:.2f} A)")
