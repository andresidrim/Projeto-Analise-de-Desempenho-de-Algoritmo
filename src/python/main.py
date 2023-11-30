from funcoes import *

def main():
    # Verificando se os dados coletaos seguem a ordem de complexidade correta
    CalculandoBubbleSortR2() # Bubble Sort
    print('\n\n')
    CalculandoMergeSortR2() # Merge Sort
    print('\n\n')
    CalculandoQuickSortR2() # Quick Sort
    print('\n\n\n\n\n')




    # Calculos básicos
    for i in range(0, pcSpecs['id'].count() + 1, 1):
        if (i == 0):
            print('No geral:')
            DescricaoAlgoritimo(GetBubbleSort(), 'Bubble Sort') # Descrição do Bubble Sort
            print('\n\n')
            DescricaoAlgoritimo(GetMergeSort(), 'Merge Sort') # Descrição do Merge Sort
            print('\n\n')
            DescricaoAlgoritimo(GetQuickSort(), 'Quick Sort') # Descrição do Quick Sort
            print('\n\n\n\n\n')

        else:
            print(f'Para o computador {i}:')
            DescricaoAlgoritimo(GetBubbleSort(i), 'Bubble Sort') # Descrição do Bubble Sort
            print('\n\n')
            DescricaoAlgoritimo(GetMergeSort(i), 'Merge Sort') # Descrição do Merge Sort
            print('\n\n')
            DescricaoAlgoritimo(GetQuickSort(i), 'Quick Sort') # Descrição do Quick Sort
            print('\n\n\n\n\n')




    # Hipotese -> Bubble Sort e Merge Sort possuem um desempeho extremamente similar para amostras menores 
    for i in range(0, pcSpecs['id'].count() + 1, 1):
        if (i == 0):
            print('No geral:')
            Hipotese1()
            print('\n\n')

        else:
            print(f'Para o computador {i}:')
            Hipotese1(i)
            print('\n\n')
    # Hipotese1() # Compara o Bubble Sort e Merge Sort com amostras de tamanho 100
    
    for i in range(0, pcSpecs['id'].count() + 1, 1):
        if (i == 0):
            print('No geral:')
            MergeMaisRapido()
            print('\n\n')
        
        else:
            print(f'Para o computador {i}:')
            MergeMaisRapido(i)
            print('\n\n')

    print('\n\n\n')
    
    for i in range(0, pcSpecs['id'].count() + 1, 1):
        if (i == 0):
            print('No geral:')
            ClassificacaoAlgoritimos()
            print('\n\n')

        else:
            print(f'Para o computador {i}')
            ClassificacaoAlgoritimos(i) # Qual o algoritimo mais rapido para cada tamanho de amostra?
            print('\n\n')
    print('\n\n\n')
    
            
    



    for i in range(0, pcSpecs['id'].count() + 1, 1):
        if (i == 0):
            print('No geral:')
            MaisRapidoPorcentagem(GetBubbleSort(), GetMergeSort(), GetQuickSort())
            print('\n\n')

        else:
            print(f'Para o computador {i}')
            MaisRapidoPorcentagem(GetBubbleSort(i), GetMergeSort(i), GetQuickSort(i))
            print('\n\n')
    print('\n\n\n')


    for i in range(0, pcSpecs['id'].count() + 1, 1):
        if (i == 0):
            print('No geral:')
            IntervaloConfianca(GetBubbleSort(), 'Bubble Sort') # Intervalo Bubble Sort
            print('\n\n')
            IntervaloConfianca(GetMergeSort(), 'Merge Sort') # Intervalo Merge Sort
            print('\n\n')
            IntervaloConfianca(GetQuickSort(), 'Quick Sort') # Intervalo Quick Sort
            print('\n\n')

        else:
            print(f'Para o computador {i}')
            IntervaloConfianca(GetBubbleSort(i), 'Bubble Sort') # Intervalo Bubble Sort
            print('\n\n')
            IntervaloConfianca(GetMergeSort(i), 'Merge Sort') # Intervalo Merge Sort
            print('\n\n')
            IntervaloConfianca(GetQuickSort(i), 'Quick Sort') # Intervalo Quick Sort
            print('\n\n')



if __name__ == "__main__":
    main()






