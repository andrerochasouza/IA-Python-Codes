'''

Desenvolvido por andre.rsouza no dia 13/05/2022

Email: andredarochasouza.12345@gmail.com

Algoritmo Insertion Sort

'''

# Insertion Sort
def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            temp = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = temp
            j -= 1
