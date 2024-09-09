def quickSort(arr, s, e):
    # Stop condition
    if e - s <= 0:
        return
    
    # Select the last value as a pivot point 
    pivot = arr[e]
    # Set left pointer
    pointer = s

    # Partition
    for i in range(s, e):
        if arr[i] <= pivot:
            temp = arr[pointer]
            arr[pointer] = arr[i]
            arr[i] = temp
            pointer += 1

    # Swap pointer and pivot point
    temp = arr[pointer]
    arr[pointer] = arr[e]
    arr[e] = temp

    # Continue to sort left and right partition
    quickSort(arr, s, pointer - 1)
    quickSort(arr, pointer + 1, e)

    return arr

if __name__ == "__main__":
    arr = [2, 7, 1, 9, 8,3, 4, 4]
    quickSort(arr, 0, len(arr) - 1)
    print(arr)