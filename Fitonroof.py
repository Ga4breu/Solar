import matplotlib.pyplot as plt
import matplotlib.patches as patches

def ajustar_paineis_hibrido(telhado_largura, telhado_comprimento, painel_largura, painel_comprimento):
    # Function to calculate the number of panels and their positions
    def calc_posicoes(telhado_largura, telhado_comprimento, painel_largura, painel_comprimento):
        posicoes = []
        y = 0
        while y + painel_comprimento <= telhado_comprimento:
            x = 0
            while x + painel_largura <= telhado_largura:
                posicoes.append((x, y))
                x += painel_largura
            y += painel_comprimento
        return posicoes

    # Calculate positions for horizontal panels first, then fill remaining space with vertical panels
    def calc_hibrido_horizontal_primeiro(telhado_largura, telhado_comprimento, painel_largura, painel_comprimento):
        posicoes = calc_posicoes(telhado_largura, telhado_comprimento, painel_largura, painel_comprimento)
        if posicoes:
            ultimo_y = posicoes[-1][1] + painel_comprimento
            posicoes_vertical = calc_posicoes(telhado_largura, telhado_comprimento - ultimo_y, painel_comprimento, painel_largura)
            for (x, y) in posicoes_vertical:
                posicoes.append((x, y + ultimo_y))
        return posicoes

    # Calculate positions for vertical panels first, then fill remaining space with horizontal panels
    def calc_hibrido_vertical_primeiro(telhado_largura, telhado_comprimento, painel_largura, painel_comprimento):
        posicoes = calc_posicoes(telhado_largura, telhado_comprimento, painel_comprimento, painel_largura)
        if posicoes:
            ultimo_x = posicoes[-1][0] + painel_comprimento
            posicoes_horizontal = calc_posicoes(telhado_largura - ultimo_x, telhado_comprimento, painel_largura, painel_comprimento)
            for (x, y) in posicoes_horizontal:
                posicoes.append((x + ultimo_x, y))
        return posicoes

    posicoes_hibrido_horizontal_primeiro = calc_hibrido_horizontal_primeiro(telhado_largura, telhado_comprimento, painel_largura, painel_comprimento)
    posicoes_hibrido_vertical_primeiro = calc_hibrido_vertical_primeiro(telhado_largura, telhado_comprimento, painel_largura, painel_comprimento)

    if len(posicoes_hibrido_horizontal_primeiro) > len(posicoes_hibrido_vertical_primeiro):
        return posicoes_hibrido_horizontal_primeiro
    else:
        return posicoes_hibrido_vertical_primeiro

def plotar_paineis(telhado_largura, telhado_comprimento, painel_largura, painel_comprimento, posicoes):
    fig, ax = plt.subplots()

    # Desenha o telhado
    telhado = patches.Rectangle((0, 0), telhado_largura, telhado_comprimento, linewidth=1, edgecolor='r', facecolor='none', label='Telhado')
    ax.add_patch(telhado)

    # Desenha os painéis solares
    for (x, y) in posicoes:
        if (x + painel_comprimento <= telhado_largura) and (y + painel_largura <= telhado_comprimento):
            painel = patches.Rectangle((x, y), painel_comprimento, painel_largura, linewidth=1, edgecolor='b', facecolor='blue', alpha=0.5)
        else:
            painel = patches.Rectangle((x, y), painel_largura, painel_comprimento, linewidth=1, edgecolor='b', facecolor='blue', alpha=0.5)
        ax.add_patch(painel)

    # Adiciona a legenda com o número de painéis
    num_paineis = len(posicoes)
    plt.legend([telhado], [f'Telhado com {num_paineis} painéis solares'])

    # Define os limites e mostra o gráfico
    plt.xlim([0, telhado_largura])
    plt.ylim([0, telhado_comprimento])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('Largura do Telhado (m)')
    plt.ylabel('Comprimento do Telhado (m)')
    plt.title('Layout dos Painéis Solares no Telhado')
    plt.show()

#Coloque os tamanhos
telhado_largura =9.6
telhado_comprimento = 22
painel_largura = 1.15
painel_comprimento = 2.4

posicoes = ajustar_paineis_hibrido(telhado_largura, telhado_comprimento, painel_largura, painel_comprimento)
print(len(posicoes))
plotar_paineis(telhado_largura, telhado_comprimento, painel_largura, painel_comprimento, posicoes)
