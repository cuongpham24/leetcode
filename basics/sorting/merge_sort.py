def mergeSort(arr, s, e):
    # stop condition
    if e - s < 1:
        return arr
    # Find middle index
    m = (s + e) // 2

    # Partition
    mergeSort(arr, s, m)
    mergeSort(arr, m + 1, e)

    # Merge
    merge(arr, s, m, e)
    return arr

def merge(arr, s, m, e):
    L = arr[s: m + 1]
    R = arr[m + 1: e + 1]

    l = 0
    r = 0
    i = s

    # Merge inplace left and right array
    while l < len(L) and r < len(R):
        if L[l] <= R[r]:
            arr[i] = L[l]
            l += 1
        else:
            arr[i] = R[r]
            r += 1
        i += 1
    
    # Merge the leftover element
    while l < len(L):
        arr[i] = L[l]
        l += 1
        i += 1

    while r < len(R):
        arr[i] = R[r]
        r += 1
        i += 1


if __name__ == "__main__":
    arr = [1, 3, 2, 8, 5, 9]
    mergeSort(arr, 0, len(arr))
    print(arr)