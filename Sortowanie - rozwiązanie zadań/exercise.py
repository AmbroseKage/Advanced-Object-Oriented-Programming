from typing import List, Tuple


def quicksort(in_array: List[int]) -> List[int]:
    """Posortuj zakres tablicy metodą quicksort.

    :param in_array: tablica do posortowania
    :return: posortowana tablica
    """

    #! Została użyta funkcja pomocnicza sortująca "w miejscu" o ktorej wspomniano w PDF
    def quicksort_inplace(array: List[int], start_inx: int, stop_inx: int) -> None:
        if start_inx >= stop_inx:
            return

        pivot = array[(start_inx + stop_inx) // 2]
        left = start_inx
        right = stop_inx

        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1

        if start_inx < right:
            quicksort_inplace(array, start_inx, right)
        if left < stop_inx:
            quicksort_inplace(array, left, stop_inx)

    #! Tutaj utworzenie kopii listy w celiu nnie modyfikować oryginału
    
    sorted_array = in_array[:]
    quicksort_inplace(sorted_array, 0, len(sorted_array) - 1)
    return sorted_array


def bubblesort(in_array: List[int]) -> Tuple[List[int], int]:
    """Posortuj tablicę metodą bąbelkową.

    :param in_array: tablica do posortowania
    :return: krotka zawierająca posortowaną tablicę oraz liczbę wykonanych porównań
    """
    
    sorted_array = in_array[:]
    n = len(sorted_array)
    comparisons = 0

    for i in range(n):
        swapped = False
        for j in range(1, n - i):
            comparisons += 1
            if sorted_array[j - 1] > sorted_array[j]:
                sorted_array[j - 1], sorted_array[j] = sorted_array[j], sorted_array[j - 1]
                swapped = True
        if not swapped:
            break

    return sorted_array, comparisons
