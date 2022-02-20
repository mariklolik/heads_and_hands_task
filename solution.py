from random import randint


def solution1(n):
    # Размеры не совпадают (т.к они постоянно растут)

    return [sorted([randint(1, 1000) for j in range(i)], reverse=i % 2 == 1) for i in range(1, n + 1)]


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def solution2(n):
    # Ожидаемое решение
    sizes = []
    while len(sizes) < n:
        a = randint(1, (n + 1) ** 3)
        sizes.append(a)
        sizes = list(set(sizes))
    ans = []
    for i in range(n):
        ln = sizes[i]
        ans.append([])
        for j in range(ln):
            ans[i].append(randint(1, 1000))
        if i % 2 == 0:
            mergeSort(ans[i])
        else:
            mergeSort(ans[i])
            ans[i] = ans[i][::-1]
    return ans


