import psycopg2
import pandas as pd

try:
    conexao = psycopg2.connect(
        host='localhost',
        database='performance_data',
        user='postgres',
        password='03jul2004'
    )

    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM PC_SPECS')

    dados = cursor.fetchall()

    colunas = [desc[0] for desc in cursor.description]
    pcSpecs = pd.DataFrame(dados, columns=colunas)



    cursor.execute('SELECT * FROM BUBBLESORT')

    dados = cursor.fetchall()

    colunas = [desc[0] for desc in cursor.description]
    bubbleSort = pd.DataFrame(dados, columns=colunas)



    cursor.execute('SELECT * FROM MERGESORT')

    dados = cursor.fetchall()

    colunas = [desc[0] for desc in cursor.description]
    mergeSort = pd.DataFrame(dados, columns=colunas)



    cursor.execute('SELECT * FROM QUICKSORT')

    dados = cursor.fetchall()

    colunas = [desc[0] for desc in cursor.description]
    quickSort = pd.DataFrame(dados, columns=colunas)



    cursor.execute('SELECT * FROM AllBubbleSortInfo')

    dados = cursor.fetchall()

    colunas = [desc[0] for desc in cursor.description]
    detailedBubbleSort = pd.DataFrame(dados, columns=colunas)



    cursor.execute('SELECT * FROM AllMergeSortInfo')

    dados = cursor.fetchall()

    colunas = [desc[0] for desc in cursor.description]
    detailedMergeSort = pd.DataFrame(dados, columns=colunas)



    cursor.execute('SELECT * FROM AllQuickSortInfo')

    dados = cursor.fetchall()

    colunas = [desc[0] for desc in cursor.description]
    detailedQuickSort = pd.DataFrame(dados, columns=colunas)

    # Agora você pode realizar operações no DataFrame se necessário

finally:
    # Certifique-se de fechar a conexão mesmo se ocorrer uma exceção
    conexao.close()

bubbleSort = bubbleSort.astype(float)
mergeSort = mergeSort.astype(float)
quickSort = quickSort.astype(float)