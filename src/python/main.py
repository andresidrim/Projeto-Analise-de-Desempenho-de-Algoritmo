from dbconnection import *
import numpy as np
from scipy.stats import ttest_rel

BubbleSort = [bubbleSort[bubbleSort['sample_size'] == 100]['run_time'],
                   bubbleSort[bubbleSort['sample_size'] == 1000]['run_time'],
                   bubbleSort[bubbleSort['sample_size'] == 10000]['run_time']]

MergeSort = [mergeSort[mergeSort['sample_size'] == 100]['run_time'],
                   mergeSort[mergeSort['sample_size'] == 1000]['run_time'],
                   mergeSort[mergeSort['sample_size'] == 10000]['run_time']]

QuickSort = [quickSort[quickSort['sample_size'] == 100]['run_time'],
                   quickSort[quickSort['sample_size'] == 1000]['run_time'],
                   quickSort[quickSort['sample_size'] == 10000]['run_time']]

# print('Descricao BubbleSort')

# for i in range(0, 3, 1):
#   print(f'Tamanho da amostra: {np.power(10, i + 2)}\n{BubbleSort[i].describe()}\n') if i < 2 else print(f'Descricao BubbleSort {np.power(10, i + 2)}\n{sBubbleSort[i].describe()}')

# print()
# print('Descricao Mergesort')

# for i in range(0, 3, 1):
#   print(f'Tamanho da amostra: {np.power(10, i + 2)}\n{MergeSort[i].describe()}\n') if i < 2 else print(f'Descricao MergeSort {np.power(10, i + 2)}\n{sMergeSort[i].describe()}')

# print()
# print('Descricao QuickSort')

# for i in range(0, 3, 1):
#   print(f'Tamanho da amostra: {np.power(10, i + 2)}\n{QuickSort[i].describe()}\n') if i < 2 else print(f'Tamanho da amostra {np.power(10, i + 2)}\n{sQuickSort[i].describe()}')











# Hipotese 1 -> BubbleSort e MergeSort possuem um desempeho extremamente similar para amostras menores

media1 = BubbleSort[0].mean()
media2 = MergeSort[0].mean()

alpha = 0.05

t_statistic, p_value = ttest_rel(bubbleSort[bubbleSort['sample_size'] == 100]['run_time'].mean(), mergeSort[mergeSort['sample_size'] == 100]['run_time'].mean())

if p_value < alpha:
    print("Para a amostra de tamanho 100, rejeitamos a hipótese nula.")
else:
    print("Para a amostra de tamanho 100, não temos evidências para rejeitar a hipótese nula.")