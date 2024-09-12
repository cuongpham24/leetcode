def binarySearch(arr, target):
    L, R = 0, len(arr) - 1

    while L <= R:
        mid = (L + R) // 2
        if arr[mid] > target:
            R = mid - 1
        elif arr[mid] < target:
            L = mid + 1
        else:
            return mid
    return -1

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8]

    print(binarySearch(arr, 3))