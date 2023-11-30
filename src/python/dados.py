from dbconnection import *

def GetBubbleSort(spec_id = ''):
    if spec_id == '':
        BubbleSortRunTime = [bubbleSort[(bubbleSort['sample_size'] == 100)]['run_time'],
            bubbleSort[(bubbleSort['sample_size'] == 1000)]['run_time'],
            bubbleSort[(bubbleSort['sample_size'] == 10000)]['run_time']]

    else:
        BubbleSortRunTime = [bubbleSort[(bubbleSort['sample_size'] == 100) & (bubbleSort['pc_specs_id'] == spec_id)]['run_time'],
            bubbleSort[(bubbleSort['sample_size'] == 1000) & (bubbleSort['pc_specs_id'] == spec_id)]['run_time'],
            bubbleSort[(bubbleSort['sample_size'] == 10000) & (bubbleSort['pc_specs_id'] == spec_id)]['run_time']]

    return BubbleSortRunTime


def GetMergeSort(spec_id = ''):
    if spec_id == '':
        MergeSortRunTime = [mergeSort[(mergeSort['sample_size'] == 100)]['run_time'],
            mergeSort[(mergeSort['sample_size'] == 1000)]['run_time'],
            mergeSort[(mergeSort['sample_size'] == 10000)]['run_time']]

    else:
        MergeSortRunTime = [mergeSort[(mergeSort['sample_size'] == 100) & (mergeSort['pc_specs_id'] == spec_id)]['run_time'],
            mergeSort[(mergeSort['sample_size'] == 1000) & (mergeSort['pc_specs_id'] == spec_id)]['run_time'],
            mergeSort[(mergeSort['sample_size'] == 10000) & (mergeSort['pc_specs_id'] == spec_id)]['run_time']]

    return MergeSortRunTime



def GetQuickSort(spec_id = ''):
    if spec_id == '':
        QuickSortRunTime = [quickSort[(quickSort['sample_size'] == 100)]['run_time'],
            quickSort[(quickSort['sample_size'] == 1000)]['run_time'],
            quickSort[(quickSort['sample_size'] == 10000)]['run_time']]

    else:
        QuickSortRunTime = [quickSort[(quickSort['sample_size'] == 100) & (quickSort['pc_specs_id'] == spec_id)]['run_time'],
            quickSort[(quickSort['sample_size'] == 1000) & (quickSort['pc_specs_id'] == spec_id)]['run_time'],
            quickSort[(quickSort['sample_size'] == 10000) & (quickSort['pc_specs_id'] == spec_id)]['run_time']]

    return QuickSortRunTime