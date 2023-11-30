from dbconnection import *
import numpy as np
from scipy.stats import ttest_ind, t
from sklearn.metrics import r2_score
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Organização dos dados
BubbleSortRunTime = [bubbleSort[(bubbleSort['sample_size'] == 100) & (bubbleSort['pc_specs_id'] == 1)]['run_time'],
    bubbleSort[(bubbleSort['sample_size'] == 1000) & (bubbleSort['pc_specs_id'] == 1)]['run_time'],
    bubbleSort[(bubbleSort['sample_size'] == 10000) & (bubbleSort['pc_specs_id'] == 1)]['run_time']]

MergeSortRunTime = [mergeSort[(mergeSort['sample_size'] == 100) & (mergeSort['pc_specs_id'] == 1)]['run_time'],
    mergeSort[(mergeSort['sample_size'] == 1000) & (mergeSort['pc_specs_id'] == 1)]['run_time'],
    mergeSort[(mergeSort['sample_size'] == 10000) & (mergeSort['pc_specs_id'] == 1)]['run_time']]

QuickSortRunTime = [quickSort[(quickSort['sample_size'] == 100) & (quickSort['pc_specs_id'] == 1)]['run_time'],
    quickSort[(quickSort['sample_size'] == 1000) & (quickSort['pc_specs_id'] == 1)]['run_time'],
    quickSort[(quickSort['sample_size'] == 10000) & (quickSort['pc_specs_id'] == 1)]['run_time']]

def MaisRapidoPorcentagem():
  for i in range(0, 3, 1):
    mediaqs = QuickSortRunTime[i].mean()
    mediams = MergeSortRunTime[i].mean()
    mediabs = BubbleSortRunTime[i].mean()

    # Calcula a porcentagem pela qual o QuickSort é mais rápido que a média dos outros algoritmos
    porcentagem_mais_rapido = abs((mediaqs - (mediams + mediabs) / 2) / ((mediams + mediabs) / 2)) * 100
    
    print(f'Para o tamanho de amostra de tamanho {np.power(10, i + 2)}, o Quick Sort é {porcentagem_mais_rapido:.2f}% mais rápido que a média dos outros algoritmos')

  mediaqs = np.mean(QuickSortRunTime)
  mediams = np.mean(MergeSortRunTime)
  mediabs = np.mean(BubbleSortRunTime)

  # Calcula a porcentagem pela qual o QuickSort é mais rápido que a média dos outros algoritmos
  porcentagem_mais_rapido = abs((mediaqs - (mediams + mediabs) / 2) / ((mediams + mediabs) / 2)) * 100

  print(f'No geral, o Quick Sort foi {porcentagem_mais_rapido:.2f}% mais rápido que a média dos outros algoritmos')



def DescricaoAlgoritimo(algoritimo, nome):
    print('Descricao ' + nome)

    for i in range(0, 3, 1):
        print(f'Tamanho da amostra: {np.power(10, i + 2)}\n{algoritimo[i].describe()}\n')










# Hipotese 1 -> BubbleSortRunTime e MergeSortRunTime possuem um desempeho extremamente similar para amostras menores

def Hipotese1():
  alpha = 0.05

  t_statistic, p_value = ttest_ind(BubbleSortRunTime[0], MergeSortRunTime[0])

  if p_value < alpha:
      print("Para a amostra de tamanho 100, rejeitamos a hipótese nula.") # Possui uma diferenca significativa
  else:
      print("Para a amostra de tamanho 100, não temos evidências para rejeitar a hipótese nula.")

def MergeMaisRapido():
  media_bubble_sort = np.mean(BubbleSortRunTime[0])
  media_merge_sort = np.mean(MergeSortRunTime[0])

  # Cálculo da diferença percentual entre os tempos médios
  diferenca_percentual = abs(((media_merge_sort - media_bubble_sort) / media_bubble_sort)) * 100

  print(f"O Merge Sort é {diferenca_percentual:.2f}% mais rápido em relação ao Bubble Sort.")


# Qual o algoritimo mais rapido para cada tamanho de amostra?
def ClassificacaoAlgoritimos():
    for i in range(0, 3, 1):
      resultados = [('BubbleSortRunTime', BubbleSortRunTime[i].mean()), ('MergeSortRunTime', MergeSortRunTime[i].mean()), ('QuickSortRunTime', QuickSortRunTime[i].mean())]

      # Ordenando a lista pelo tempo médio em ordem crescente
      resultados.sort(key=lambda x: x[1])

      # Imprimindo o pódio para o tamanho de amostra atual
      print(f"\nPara o tamanho de amostra {np.power(10, i + 2)}:")
      for posicao, (algoritmo, media) in enumerate(resultados, start=1):
          print(f"{posicao}º lugar: {algoritmo} com média de {media:.4f} microsegundos.")




# INTERVALO DE CONFIANÇA
def IntervaloConfianca(algoritimo, nome, alpha = 0.05):
  for i in range(0, 3, 1):
      desvio_padrao = np.std(algoritimo[i], ddof=1)  # Use ddof=1 para cálculo não enviesado do desvio padrão
          
      # Calculando o intervalo de confiança
      tamanho_amostral = len(algoritimo[i])
      erro_padrao = desvio_padrao / np.sqrt(tamanho_amostral)
      intervalo_confianca = t.interval((1 - alpha), tamanho_amostral - 1, loc=algoritimo[i].mean(), scale=erro_padrao)

      print(f"\nIntervalo de Confiança para o {nome} (amostra de tamanho {np.power(10, i + 2)}):")
      print(f"Média: {algoritimo[i].mean():.4f}")
      print(f"Intervalo de Confiança: {intervalo_confianca}")





# # INTERVALO PARA MERGE SORT
# for i in range(0, 3, 1):
#     desvio_padrao_bubble = np.std(MergeSortRunTime[i], ddof=1)  # Use ddof=1 para cálculo não enviesado do desvio padrão
        
#     # Calculando o intervalo de confiança
#     tamanho_amostral = len(MergeSortRunTime[i])
#     erro_padrao = desvio_padrao_bubble / np.sqrt(tamanho_amostral)
#     intervalo_confianca = t.interval((1 - alpha), tamanho_amostral - 1, loc=MergeSortRunTime[i].mean(), scale=erro_padrao)

#     print(f"\nIntervalo de Confiança para o Bubble Sort (amostra de tamanho {np.power(10, i + 2)}):")
#     print(f"Média: {MergeSortRunTime[i].mean():.4f}")
#     print(f"Intervalo de Confiança: {intervalo_confianca}")





# # INTERVALO PARA QUICK SORT
# for i in range(0, 3, 1):
#     desvio_padrao_bubble = np.std(QuickSortRunTime[i], ddof=1)  # Use ddof=1 para cálculo não enviesado do desvio padrão
        
#     # Calculando o intervalo de confiança
#     tamanho_amostral = len(QuickSortRunTime[i])
#     erro_padrao = desvio_padrao_bubble / np.sqrt(tamanho_amostral)
#     intervalo_confianca = t.interval((1 - alpha), tamanho_amostral - 1, loc=QuickSortRunTime[i].mean(), scale=erro_padrao)

#     print(f"\nIntervalo de Confiança para o Bubble Sort (amostra de tamanho {np.power(10, i + 2)}):")
#     print(f"Média: {QuickSortRunTime[i].mean():.4f}")
#     print(f"Intervalo de Confiança: {intervalo_confianca}")























# sizes_bubble = bubbleSort.loc[bubbleSort['pc_specs_id'] == 1, 'sample_size'].values
# execution_times_bubble = bubbleSort.loc[bubbleSort['pc_specs_id'] == 1, 'run_time'].values

# # Função quadrática (polinômio de grau 2)
# def quadratic_func(x, a, b, c):
#     return a * x**2 + b * x + c

# # Ajuste dos dados à função quadrática
# params_bubble, covariance_bubble = curve_fit(quadratic_func, sizes_bubble, execution_times_bubble)

# # Previsões usando a função ajustada
# predictions_bubble = quadratic_func(sizes_bubble, *params_bubble)

# # Cálculo do R²
# r_squared_bubble = r2_score(execution_times_bubble, predictions_bubble)

# # Impressão do R²
# print(f"Coeficiente de Determinação (R²) para Bubble Sort: {r_squared_bubble}")








# sizes_merge = mergeSort.loc[mergeSort['pc_specs_id'] == 1, 'sample_size'].values
# execution_times_merge = mergeSort.loc[mergeSort['pc_specs_id'] == 1, 'run_time'].values

# # Função logarítmica (O(n log n))
# def log_func(x, a, b):
#     return a * x * np.log(x) + b

# params_merge, covariance_merge = curve_fit(log_func, sizes_merge, execution_times_merge)

# predictions_merge = log_func(sizes_merge, *params_merge)

# # Cálculo do R²
# r_squared_merge = r2_score(execution_times_merge, predictions_merge)

# # Impressão do R²
# print(f"Coeficiente de Determinação (R²) para Merge Sort: {r_squared_merge}")






















# sizes_quick = quickSort.loc[quickSort['pc_specs_id'] == 1, 'sample_size'].values
# execution_times_quick = quickSort.loc[quickSort['pc_specs_id'] == 1, 'run_time'].values

# # Função linear (O(n))
# def linear_func(x, a, b):
#     return a * x + b

# # Ajuste dos dados à função linear
# params_quick, covariance_quick = curve_fit(linear_func, sizes_quick, execution_times_quick)

# # Previsões usando a função ajustada
# predictions_quick = linear_func(sizes_quick, *params_quick)

# # Cálculo do R²
# r_squared_quick = r2_score(execution_times_quick, predictions_quick)

# # Impressão do R²
# print(f"Coeficiente de Determinação (R²) para Quick Sort: {r_squared_quick}")


