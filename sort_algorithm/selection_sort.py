'''

Desenvolvido por andre.rsouza no dia 13/05/2022

Email: andredarochasouza.12345@gmail.com

Algoritmo Selection Sort

'''

# Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[j] < arr[i]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp