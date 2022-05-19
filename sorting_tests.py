'''

Desenvolvido por andre.rsouza no dia 19/05/2022

Email: andredarochasouza.12345@gmail.com

Algoritmo Merge Sort

'''

from sort_algorithm import bubble_sort as bubble, insertion_sort as insertion, merge_sort as merge, selection_sort as selection
import time
import random

start_time = time.time()

arr = []
for i in range(5000):
    arr.append(i * random.randint(1, 10))

i = random.randint(1, 4)

if i == 1:
    selection.selection_sort(arr)
    print("Selection Sort")
elif i == 2:
    print("Bubble Sort")
    bubble.bubble_sort(arr)
elif i == 3:
    print("Insertion Sort")
    insertion.insertion_sort(arr)
else:
    print("Merge Sort")
    merge.merge_sort(arr)


finish_time = time.time()
finish_time = finish_time - start_time

print(arr)
print("Tempo de execução: %.5f segundos" % finish_time)