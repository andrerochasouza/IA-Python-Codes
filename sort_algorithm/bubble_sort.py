arr = [1,3,6,3,2,7,2,9,5,2,9,3,8,4]
tam = arr.len() - 1

for j in tam:
    for i in range(arr):
        if arr[i] > arr[i + 1]:
            temporario = arr[i + 1]
            arr[i + 1] = arr[i]
            arr[i]  [temporario]
        tam -= tam

print(arr)
