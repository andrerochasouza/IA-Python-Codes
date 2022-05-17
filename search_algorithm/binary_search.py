'''

Desenvolvido por andre.rsouza no dia 13/05/2022

Email: andredarochasouza.12345@gmail.com

Algoritmo Binary Search

'''

import time
import random

# Insertion Sort
def inserction_sort(arr):
    for i in range(5000):
        arr.append(i * random.randint(1, 10))

    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            temp = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = temp
            j -= 1
    return arr

# Search Binary
def binary_search(arr, value):
    ind_menor = 0
    ind_maior = len(arr) - 1

    while ind_menor <= ind_maior:
        ind_central = round((ind_menor + ind_maior) / 2)
        temp = arr[ind_central]

        if temp == value:
            return ind_central
        if temp > value:
            ind_maior = ind_central - 1
        else:
            ind_menor = ind_central + 1

start_time = time.time()

num_buscas = 10
arr = []
inserction_sort(arr)

for i in range(10):
    print(binary_search(arr, random.randint(1, len(arr))))
    

finish_time = time.time()
finish_time = finish_time - start_time

print("Tempo de execução: %.5f segundos" % finish_time)
