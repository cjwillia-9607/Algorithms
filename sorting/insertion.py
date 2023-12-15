# implement insertion sort

def insertion_sort(array):
    for i in range(1, len(array)):
        current = array[i]
        j = i - 1
        while j >= 0 and array[j] > current:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current
    return array

if __name__ == '__main__':
    array = [5, 4, 3, 2, 1]
    print(insertion_sort(array))