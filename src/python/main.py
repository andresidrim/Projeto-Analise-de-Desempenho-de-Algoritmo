from funcoes import *

def main():
    DescricaoAlgoritimo(BubbleSortRunTime, 'Bubble Sort') # Descrição do Bubble Sort
    print('\n\n')
    DescricaoAlgoritimo(MergeSortRunTime, 'Merge Sort') # Descrição do Merge Sort
    print('\n\n')
    DescricaoAlgoritimo(QuickSortRunTime, 'Quick Sort') # Descrição do Quick Sort
    print('\n\n\n\n\n')
    Hipotese1() # Hipotese 1 -> BubbleSortRunTime e MergeSortRunTime possuem um desempeho extremamente similar para amostras menores 
    print('\n\n\n\n\n')
    MergeMaisRapido() # Quão mais rápido é o Merge Sort em relação ao Bubble Sort?
    print('\n\n\n\n\n')
    ClassificacaoAlgoritimos() # Qual o algoritimo mais rapido para cada tamanho de amostra?
    print('\n\n\n\n\n')
    IntervaloConfianca(BubbleSortRunTime, 'Bubble Sort') # Intervalo Quick Sort
    print('\n\n')
    IntervaloConfianca(MergeSortRunTime, 'Merge Sort') # Intervalo Merge Sort
    print('\n\n')
    IntervaloConfianca(QuickSortRunTime, 'Quick Sort') # Intervalo Quick Sort
    print('\n\n\n\n\n')
    MaisRapidoPorcentagem() # Qual o algoritimo mais rapido para cada tamanho de amostra?
    




if __name__ == "__main__":
    main()






