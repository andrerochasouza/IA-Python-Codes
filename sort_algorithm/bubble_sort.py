'''

Desenvolvido por andre.rsouza no dia 13/05/2022

Email: andredarochasouza.12345@gmail.com

Algoritmo Bubble Sort

'''

import time
import random

start_time = time.time()

arr = []
for i in range(5000):
    arr.append(i * random.randint(1, 10))

for i in range(len(arr) - 1, -1, -1):
    for j in range(len(arr) - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

finish_time = time.time()
finish_time = finish_time - start_time

print(arr)
print("Tempo de execução: %.5f segundos" % finish_time)
