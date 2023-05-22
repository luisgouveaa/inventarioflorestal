##Compreendendo a Distribuição Diamétrica das Florestas 

import numpy as np
import matplotlib.pyplot as plt

# Gerar dados simulados para uma floresta plantada (distribuição normal)
media_plantada = 40  # Média dos diâmetros
desvio_padrao_plantada = 10  # Desvio padrão dos diâmetros
num_arvores_plantada = 1000  # Número de árvores na floresta plantada

dados_plantada = np.random.normal(media_plantada, desvio_padrao_plantada, num_arvores_plantada)

# Gerar dados simulados para uma floresta natural (distribuição J-invertido)
num_arvores_natural = 1000  # Número de árvores na floresta natural

# Definir os limites das classes de diâmetro para criar a distribuição J-invertido
classes_diametro = [0, 20, 40, 60, 80, 100]  # Intervalos de diâmetro
probabilidades = [0.4, 0.3, 0.2, 0.08, 0.02]  # Probabilidades de cada classe de diâmetro

# Gerar a distribuição J-invertido com base nas probabilidades
dados_natural = np.concatenate([
    np.random.uniform(classes_diametro[i], classes_diametro[i + 1], int(num_arvores_natural * p))
    for i, p in enumerate(probabilidades)
])

# Criar os gráficos de distribuição diamétrica
plt.figure(figsize=(800/96, 400/96), dpi=96)  # Define o tamanho da figura em polegadas com uma resolução de 96 dpi

# Gráfico da floresta plantada (distribuição normal)
plt.subplot(1, 2, 1)
plt.hist(dados_plantada, bins=30, edgecolor='black')
plt.xlabel('Diâmetro do tronco (cm)')
plt.ylabel('Número de árvores')
plt.title('Floresta Plantada')

# Gráfico da floresta natural (distribuição J-invertido)
plt.subplot(1, 2, 2)
plt.hist(dados_natural, bins=30, edgecolor='black')
plt.xlabel('Diâmetro do tronco (cm)')
plt.ylabel('Número de árvores')
plt.title('Floresta Natural')

plt.tight_layout()  # Melhorar o espaçamento entre os gráficos
plt.show()
