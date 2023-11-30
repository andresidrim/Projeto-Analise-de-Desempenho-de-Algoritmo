from dbconnection import *
from dados import *
import numpy as np
from scipy.stats import ttest_ind, t
from sklearn.metrics import r2_score
from scipy.optimize import curve_fit

GetBubbleSort()[0].mean()

def MaisRapidoPorcentagem(bubble, merge, quick):
  for i in range(0, 3, 1):
    mediaqs = quick[i].mean()
    mediams = merge[i].mean()
    mediabs = bubble[i].mean()

    # Calcula a porcentagem pela qual o QuickSort é mais rápido que a média dos outros algoritmos
    porcentagem_mais_rapido = abs((mediaqs - (mediams + mediabs) / 2) / ((mediams + mediabs) / 2)) * 100
    
    print(f'Para o tamanho de amostra de tamanho {np.power(10, i + 2)}, o Quick Sort é {porcentagem_mais_rapido:.2f}% mais rápido que a média dos outros algoritmos')
    
  mediaqs = np.mean(quick)
  mediams = np.mean(merge)
  mediabs = np.mean(bubble)
    
  # Calcula a porcentagem pela qual o QuickSort é mais rápido que a média dos outros algoritmos
  porcentagem_mais_rapido = abs((mediaqs - (mediams + mediabs) / 2) / ((mediams + mediabs) / 2)) * 100

  print(f'No geral, o Quick Sort foi {porcentagem_mais_rapido:.2f}% mais rápido que a média dos outros algoritmos')



def DescricaoAlgoritimo(algoritimo, nome):
    print('Descricao ' + nome)

    for i in range(0, 3, 1):
        print(f'Tamanho da amostra: {np.power(10, i + 2)}\n{algoritimo[i].describe()}\n')










# Hipotese 1 -> BubbleSortRunTimeGeral e MergeSortRunTimeGeral possuem um desempeho extremamente similar para amostras menores

def Hipotese1(spec_id = ''):
  alpha = 0.05

  if spec_id == '':
    t_statistic, p_value = ttest_ind(GetBubbleSort()[0], GetMergeSort()[0])

  else:
    t_statistic, p_value = ttest_ind(GetBubbleSort(spec_id)[0], GetMergeSort(spec_id)[0])

  if p_value < alpha:
      print("Para a amostra de tamanho 100, rejeitamos a hipótese nula.") # Possui uma diferenca significativa
  else:
      print("Para a amostra de tamanho 100, não temos evidências para rejeitar a hipótese nula")

def MergeMaisRapido(spec_id = ''):
  if spec_id == '':
    media_bubble_sort = np.mean(GetBubbleSort()[0])
    media_merge_sort = np.mean(GetMergeSort()[0])

  else:
    media_bubble_sort = np.mean(GetBubbleSort(spec_id)[0])
    media_merge_sort = np.mean(GetMergeSort(spec_id)[0])

  # Cálculo da diferença percentual entre os tempos médios
  diferenca_percentual = abs(((media_merge_sort - media_bubble_sort) / media_bubble_sort)) * 100

  print(f"O Merge Sort é {diferenca_percentual:.2f}% mais rápido em relação ao Bubble Sort nesse caso")


# Qual o algoritimo mais rapido para cada tamanho de amostra?
def ClassificacaoAlgoritimos(spec_id = ''):
    for i in range(0, 3, 1):
      if spec_id == '':
        resultados = [('Bubble Sort', GetBubbleSort()[i].mean()), ('Merge Sort', GetMergeSort()[i].mean()), ('Quick Sort', GetQuickSort()[i].mean())]

      else:
        resultados = [('Bubble Sort', GetBubbleSort(spec_id)[i].mean()), ('Merge Sort', GetMergeSort(spec_id)[i].mean()), ('Quick Sort', GetQuickSort(spec_id)[i].mean())]
      
      # Ordenando a lista pelo tempo médio em ordem crescente
      resultados.sort(key=lambda x: x[1])

      # Imprimindo o pódio para o tamanho de amostra atual
      print(f"Para o tamanho de amostra {np.power(10, i + 2)}:")
      for posicao, (algoritmo, media) in enumerate(resultados, start=1):
          print(f"{posicao}º lugar: {algoritmo} com média de {media:.4f} microsegundos")




# INTERVALO DE CONFIANÇA
def IntervaloConfianca(algoritimo, nome, alpha = 0.05):
  for i in range(0, 3, 1):
      desvio_padrao = np.std(algoritimo[i], ddof=1)  # Use ddof=1 para cálculo não enviesado do desvio padrão
          
      # Calculando o intervalo de confiança
      tamanho_amostral = len(algoritimo[i])
      erro_padrao = desvio_padrao / np.sqrt(tamanho_amostral)
      intervalo_confianca = t.interval((1 - alpha), tamanho_amostral - 1, loc=algoritimo[i].mean(), scale=erro_padrao)

      print(f"Intervalo de Confiança para o {nome} (amostra de tamanho {np.power(10, i + 2)}):")
      print(f"Intervalo de Confiança: {intervalo_confianca}\n")



def CalculandoBubbleSortR2():
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
    print(f'Os dados coletados se aproximam {r_squared_bubble * 100:.2f}% da função quadrática')







def CalculandoMergeSortR2():
  sizes_merge = mergeSort.loc[mergeSort['pc_specs_id'] == 1, 'sample_size'].values
  execution_times_merge = mergeSort.loc[mergeSort['pc_specs_id'] == 1, 'run_time'].values

  # Função linearitimica (O(n log n))
  def log_func(x, a, b):
      return a * x * np.log(x) + b

  params_merge, covariance_merge = curve_fit(log_func, sizes_merge, execution_times_merge)

  predictions_merge = log_func(sizes_merge, *params_merge)

  # Cálculo do R²
  r_squared_merge = r2_score(execution_times_merge, predictions_merge)

  # Impressão do R²
  print(f"Coeficiente de Determinação (R²) para Merge Sort: {r_squared_merge}")
  print(f'Os dados coletados se aproximam {r_squared_merge * 100:.2f}% da função linearitimica')






def CalculandoQuickSortR2():
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
  print(f'Os dados coletados se aproximam {r_squared_quick * 100:.2f}% da função linear')