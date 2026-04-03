def binary_search(arr, value):
    low = 0
    heigh = len(arr) - 1

    while low <= heigh:
        middle = (low + heigh) // 2
        if arr[middle] == value:
            return middle
        elif arr[middle] > value:
            heigh = middle - 1
        else:
            low = middle + 1
    return -1


number_list = [1, 4, 3, 5, 6, 7, 43, 53, 45, 67, 66]

print(binary_search(number_list, 66),  (len(number_list) - 1))
