'''

Desenvolvido por andre.rsouza no dia 19/05/2022

Email: andredarochasouza.12345@gmail.com

Algoritmo Quick Sort

'''

# Quick Sort
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        p = quick(arr, low, high)
        quick_sort(arr, low, p-1)
        quick_sort(arr, p+1, high)


# Partition to quick array
def quick(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i = i + 1
    arr[i], arr[high] = arr[high], arr[i]
    return i
