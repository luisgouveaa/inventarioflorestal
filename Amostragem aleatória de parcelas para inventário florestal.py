#"Amostragem aleatória de parcelas para inventário florestal usando geoprocessamento"

import geopandas as gpd
from shapely.geometry import Polygon, Point
from shapely.ops import polygonize
import random
import matplotlib.pyplot as plt

# Carrega o arquivo do shapefile da área de interesse
area_interesse = gpd.read_file('C:/Users/luish/OneDrive/Desktop/inventario/shapeexemplo/talhao.shp')

# Transforma o sistema de projeção para uma projeção adequada para o cálculo de área
area_interesse = area_interesse.to_crs("EPSG:31982") #SIRGAS2000 /UTM zone 22s

# Calcula a área total do polígono
area_total = round(area_interesse.geometry.area.sum(), 2)

# Define o area da parcela
area_parcela = 100

# Calcula o número de parcelas que cabem no polígono

num_parcelas = int(area_total / (area_parcela))

# Definir a margem de erro e o nível de confiança desejados
margem_erro = 0.05
nivel_confianca = 0.95

# Calcular o número de amostras necessárias para uma população finita

num_amostras = int(num_parcelas / (1 + (num_parcelas*(margem_erro**2))))


#Relatório Final 
print('Relatório Final')
print('Área total do Talhão: ', area_total,'m²')
print('Área de cada Parcela: ', area_parcela, 'm²')
print('Número total de parcelas: ', num_parcelas) 
print(f"Número de amostras necessárias: {num_amostras}")

# Gera coordenadas aleatórias para as parcelas amostrais
parcelas_amostrais = []
for i in range(num_amostras):
    while True:
        # Gera coordenadas aleatórias dentro da área de interesse
        x = random.uniform(area_interesse.bounds.minx, area_interesse.bounds.maxx)
        y = random.uniform(area_interesse.bounds.miny, area_interesse.bounds.maxy)

        # Cria um objeto shapely Point com as coordenadas geradas
        ponto = Point(x, y)

        # Cria um objeto shapely Polygon com base no ponto e no tamanho da parcela
        parcela = Polygon([(x - 5, y - 5),
                           (x + 5, y - 5),
                           (x + 5, y + 5),
                           (x - 5, y + 5)])

        # Verifica se a parcela está completamente dentro da área de interesse
        if parcela.within(area_interesse.geometry.iloc[0]):
            # Verifica se a nova parcela sobrepoem alguma parcela anterior
            sobreposicao = False
            for p in parcelas_amostrais:
                if p.intersects(parcela):
                    sobreposicao = True
                    break

            # Se não houver sobreposição, adiciona a nova parcela e sai do loop
            if not sobreposicao:
                parcelas_amostrais.append(parcela)
                break

# Dividir as áreas sobrepostas em novas parcelas
parcelas_divididas = gpd.overlay(gpd.GeoDataFrame(geometry=parcelas_amostrais), gpd.GeoDataFrame(geometry=parcelas_amostrais), how='union')

# Selecionar as parcelas não sobrepostas
parcelas_amostrais = []
for p in parcelas_divididas.geometry:
    if isinstance(p, Polygon) and p.area <= area_parcela:
        if p.within(area_interesse.geometry.iloc[0]):
            parcelas_amostrais.append(p)

# Cria um objeto geopandas GeoDataFrame com as parcelas amostrais
parcelas_amostrais = gpd.GeoDataFrame(geometry=parcelas_amostrais, crs=area_interesse.crs)

# Criando uma mapa como resultado 

# Plota as parcelas amostrais e a área de interesse
fig, ax = plt.subplots(figsize=(10, 10))
area_interesse.plot(ax=ax, color='gray', alpha=0.5, label='Área de interesse')
parcelas_amostrais.plot(ax=ax, color='red', label='Parcelas')
ax.set_title("Parcelas aleatórias sob o talhão a ser inventáriado", fontsize=12)
ax.set_xlabel('UTM Leste')
ax.set_ylabel('UTM Norte')
ax.annotate('Sistema de Projeção: SIRGAS2000 /UTM zone 22s', xy=(0.95, 0.02), xycoords='axes fraction', ha='right', va='bottom')

# Define as cores e labels para cada classe
cores = ['gray', 'red']
labels = ['Área de interesse', 'Parcelas']

# Adiciona a legenda
handles = [plt.Rectangle((0,0),1,1, color=cores[i]) for i in range(len(cores))]
ax.legend(handles, labels, loc='upper right', fontsize=12, bbox_to_anchor=(1.0, 1.0))

plt.show()
