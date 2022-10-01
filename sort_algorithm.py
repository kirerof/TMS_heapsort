lst = [12, 11, 15, 13, 5, 56, 6, 7, 99, 10, 1]
print(lst)
n = len(lst)


def heapify(arr, n, ind):
    largest = ind
    left = 2 * ind + 1
    right = 2 * ind + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != ind:
        arr[ind], arr[largest] = arr[largest], arr[ind]

        heapify(arr, n, largest)


def heapsort(arr, n):

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


heapsort(lst, n)
print(lst)