from dbconnection import *
import numpy as np
from scipy.stats import ttest_ind, t
from sklearn.metrics import r2_score
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

BubbleSort = [bubbleSort[(bubbleSort['sample_size'] == 100) & (bubbleSort['pc_specs_id'] == 1)]['run_time'],
    bubbleSort[(bubbleSort['sample_size'] == 1000) & (bubbleSort['pc_specs_id'] == 1)]['run_time'],
    bubbleSort[(bubbleSort['sample_size'] == 10000) & (bubbleSort['pc_specs_id'] == 1)]['run_time']]

MergeSort = [mergeSort[(mergeSort['sample_size'] == 100) & (mergeSort['pc_specs_id'] == 1)]['run_time'],
    mergeSort[(mergeSort['sample_size'] == 1000) & (mergeSort['pc_specs_id'] == 1)]['run_time'],
    mergeSort[(mergeSort['sample_size'] == 10000) & (mergeSort['pc_specs_id'] == 1)]['run_time']]

QuickSort = [quickSort[(quickSort['sample_size'] == 100) & (quickSort['pc_specs_id'] == 1)]['run_time'],
    quickSort[(quickSort['sample_size'] == 1000) & (quickSort['pc_specs_id'] == 1)]['run_time'],
    quickSort[(quickSort['sample_size'] == 10000) & (quickSort['pc_specs_id'] == 1)]['run_time']]

print('Descricao BubbleSort')

for i in range(0, 3, 1):
  print(f'Tamanho da amostra: {np.power(10, i + 2)}\n{BubbleSort[i].describe()}\n') if i < 2 else print(f'Descricao BubbleSort {np.power(10, i + 2)}\n{BubbleSort[i].describe()}')

print()
print('Descricao Mergesort')

for i in range(0, 3, 1):
  print(f'Tamanho da amostra: {np.power(10, i + 2)}\n{MergeSort[i].describe()}\n') if i < 2 else print(f'Descricao MergeSort {np.power(10, i + 2)}\n{MergeSort[i].describe()}')

print()
print('Descricao QuickSort')

for i in range(0, 3, 1):
  print(f'Tamanho da amostra: {np.power(10, i + 2)}\n{QuickSort[i].describe()}\n') if i < 2 else print(f'Tamanho da amostra {np.power(10, i + 2)}\n{QuickSort[i].describe()}')











# Hipotese 1 -> BubbleSort e MergeSort possuem um desempeho extremamente similar para amostras menores

alpha = 0.05

t_statistic, p_value = ttest_ind(BubbleSort[0], MergeSort[0])

if p_value < alpha:
    print("Para a amostra de tamanho 100, rejeitamos a hipótese nula.") # Possui uma diferenca significativa
else:
    print("Para a amostra de tamanho 100, não temos evidências para rejeitar a hipótese nula.")

# Qual o algoritimo mais rapido para cada tamanho de amostra?

for i in range(0, 3, 1):
    resultados = [('BubbleSort', BubbleSort[i].mean()), ('MergeSort', MergeSort[i].mean()), ('QuickSort', QuickSort[i].mean())]

    # Ordenando a lista pelo tempo médio em ordem crescente
    resultados.sort(key=lambda x: x[1])

    # Imprimindo o pódio para o tamanho de amostra atual
    print(f"\nPara o tamanho de amostra {np.power(10, i + 2)}:")
    for posicao, (algoritmo, media) in enumerate(resultados, start=1):
        print(f"{posicao}º lugar: {algoritmo} com média de {media:.4f} microsegundos.")




# INTERVALO PARA BUBBLE SORT
desvio_padrao_bubble = np.std(BubbleSort[0], ddof=1)  # Use ddof=1 para cálculo não enviesado do desvio padrão
    
# Calculando o intervalo de confiança
tamanho_amostral = len(BubbleSort[0])
erro_padrao = desvio_padrao_bubble / np.sqrt(tamanho_amostral)
intervalo_confianca = t.interval((1 - alpha), tamanho_amostral - 1, loc=BubbleSort[0].mean(), scale=erro_padrao)

print(f"\nIntervalo de Confiança para o Bubble Sort (amostra de tamanho {100}):")
print(f"Média: {BubbleSort[0].mean():.4f}")
print(f"Intervalo de Confiança: {intervalo_confianca}")





# INTERVALO PARA MERGE SORT
desvio_padrao_bubble = np.std(MergeSort[0], ddof=1)  # Use ddof=1 para cálculo não enviesado do desvio padrão
    
# Calculando o intervalo de confiança
tamanho_amostral = len(MergeSort[0])
erro_padrao = desvio_padrao_bubble / np.sqrt(tamanho_amostral)
intervalo_confianca = t.interval((1 - alpha), tamanho_amostral - 1, loc=MergeSort[0].mean(), scale=erro_padrao)

print(f"\nIntervalo de Confiança para o Bubble Sort (amostra de tamanho {100}):")
print(f"Média: {MergeSort[0].mean():.4f}")
print(f"Intervalo de Confiança: {intervalo_confianca}")





# INTERVALO PARA BUBBLE SORT
desvio_padrao_bubble = np.std(QuickSort[0], ddof=1)  # Use ddof=1 para cálculo não enviesado do desvio padrão
    
# Calculando o intervalo de confiança
tamanho_amostral = len(QuickSort[0])
erro_padrao = desvio_padrao_bubble / np.sqrt(tamanho_amostral)
intervalo_confianca = t.interval((1 - alpha), tamanho_amostral - 1, loc=QuickSort[0].mean(), scale=erro_padrao)

print(f"\nIntervalo de Confiança para o Bubble Sort (amostra de tamanho {100}):")
print(f"Média: {QuickSort[0].mean():.4f}")
print(f"Intervalo de Confiança: {intervalo_confianca}")























sizes_bubble = bubbleSort.loc[bubbleSort['pc_specs_id'] == 1, 'sample_size'].values
execution_times_bubble = bubbleSort.loc[bubbleSort['pc_specs_id'] == 1, 'run_time'].values

# Função quadrática (polinômio de grau 2)
def quadratic_func(x, a, b, c):
    return a * x**2 + b * x + c

# Ajuste dos dados à função quadrática
params_bubble, covariance_bubble = curve_fit(quadratic_func, sizes_bubble, execution_times_bubble)

# Previsões usando a função ajustada
predictions_bubble = quadratic_func(sizes_bubble, *params_bubble)

# Cálculo do R²
r_squared_bubble = r2_score(execution_times_bubble, predictions_bubble)

# Impressão do R²
print(f"Coeficiente de Determinação (R²) para Bubble Sort: {r_squared_bubble}")








sizes_merge = mergeSort.loc[mergeSort['pc_specs_id'] == 1, 'sample_size'].values
execution_times_merge = mergeSort.loc[mergeSort['pc_specs_id'] == 1, 'run_time'].values

# Função logarítmica (O(n log n))
def log_func(x, a, b):
    return a * x * np.log(x) + b

# Ajuste dos dados à função logarítmica
params_merge, covariance_merge = curve_fit(log_func, sizes_merge, execution_times_merge)

# Previsões usando a função ajustada
predictions_merge = log_func(sizes_merge, *params_merge)

# Cálculo do R²
r_squared_merge = r2_score(execution_times_merge, predictions_merge)

# Impressão do R²
print(f"Coeficiente de Determinação (R²) para Merge Sort: {r_squared_merge}")























sizes_quick = quickSort.loc[quickSort['pc_specs_id'] == 1, 'sample_size'].values
execution_times_quick = quickSort.loc[quickSort['pc_specs_id'] == 1, 'run_time'].values

# Função linear (O(n))
def linear_func(x, a, b):
    return a * x + b

# Ajuste dos dados à função linear
params_quick, covariance_quick = curve_fit(linear_func, sizes_quick, execution_times_quick)

# Previsões usando a função ajustada
predictions_quick = linear_func(sizes_quick, *params_quick)

# Cálculo do R²
r_squared_quick = r2_score(execution_times_quick, predictions_quick)

# Impressão do R²
print(f"Coeficiente de Determinação (R²) para Quick Sort: {r_squared_quick}")


