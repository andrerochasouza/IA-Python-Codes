'''

Desenvolvido por andre.rsouza no dia 15/05/2022

Email: andredarochasouza.12345@gmail.com

Algoritmo Bubble Sort

'''

# Bubble Sort
def bubble_sort(arr):
    for i in range(len(arr) - 1, -1, -1):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
