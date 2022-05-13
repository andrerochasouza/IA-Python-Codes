'''

Desenvolvido por andre.rsouza no dia 13/05/2022

Email: andredarochasouza.12345@gmail.com

Algoritmo Bubble Sort

'''

arr = [1,3,6,3,2,7,2,9,5,2,9,3,8,4]
tam = len(arr) - 1

for j in range(tam):
    for i in range(len(arr)):
        if i < len(arr) - 1:
            if arr[i] > arr[i + 1]:
                temporario = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = arr[temporario]
            tam -= tam

print(arr)
