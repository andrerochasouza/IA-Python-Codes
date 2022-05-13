'''

Desenvolvido por andre.rsouza no dia 13/05/2022

Email: andredarochasouza.12345@gmail.com

Algoritmo Selection Sort

'''

arr = [1,3,6,3,2,7,2,9,5,2,9,3,8,4]

for i in range(len(arr)):
    for j in range(i, len(arr)):
        if arr[j] < arr[i]:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp

print(arr)