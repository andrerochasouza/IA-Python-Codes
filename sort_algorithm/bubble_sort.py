'''

Desenvolvido por andre.rsouza no dia 15/05/2022

Email: andredarochasouza.12345@gmail.com

Algoritmo Bubble Sort

'''

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]