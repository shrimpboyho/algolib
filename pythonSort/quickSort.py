# coding=utf-8
from randArray import createRandArray


def partition(array, start, end):
    pivot = array[(start + end) // 2]
    i = start
    j = end

    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

            i += 1
            j -= 1

    return i

def quickSort(array, start, end):
    if start < end:
        temp = partition(array, start, end)

        quickSort(array, start, temp - 1)
        quickSort(array, temp, end)

if __name__ == '__main__':
    # Using the random array function to create a random array to test
    # quick sort
    A = createRandArray(10,100)
    print(qSort(A, 0, len(A) - 1))