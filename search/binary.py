# implement binary search

def binary_search(array, target):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    print(binary_search(array, 3))
    print(binary_search(array, 6))