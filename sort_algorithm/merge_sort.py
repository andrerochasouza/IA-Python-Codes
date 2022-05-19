'''

Desenvolvido por andre.rsouza no dia 19/05/2022

Email: andredarochasouza.12345@gmail.com

Algoritmo Merge Sort

'''

# Merge Sort
def merge_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr)

    if (high - low) > 1:
        mid = (high + low) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid, high)
        merge(arr, low, mid, high)

# Merge to array
def merge(arr, low, mid, high):
    esq = arr[low:mid]
    dir = arr[mid:high]
    top_esq, top_dir = 0, 0

    for k in range(low, high):
        if top_esq >= len(esq):
            arr[k] = dir[top_dir]
            top_dir = top_dir + 1
        elif top_dir >= len(dir):
            arr[k] = esq[top_esq]
            top_esq = top_esq + 1
        elif esq[top_esq] < dir[top_dir]:
            arr[k] = esq[top_esq]
            top_esq = top_esq + 1
        else:
            arr[k] = dir[top_dir]
            top_dir = top_dir + 1
