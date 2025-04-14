import unittest
from exercise import quicksort, bubblesort
from timeit import timeit

class TestFunctions(unittest.TestCase):

    def setUp(self):
        #! DANE DO PRZEPROWADZENIA TESTÓW
        self.sorted_list = list(range(1000))
        self.reversed_list = list(range(999, -1, -1))
        self.equal_values_list = [7] * 1000
        self.random_list = [5, 3, 8, 1, 9, 6]
        self.iterations = 1000

    #! Sprawdzenie czy funkcja quicksort działa poprawnie:
    def test_quicksort(self):
        self.assertEqual(quicksort(self.sorted_list), self.sorted_list)
        self.assertEqual(quicksort(self.reversed_list), self.sorted_list)
        self.assertEqual(quicksort(self.equal_values_list), self.equal_values_list)
        self.assertEqual(quicksort(self.random_list), sorted(self.random_list))

    #! Sprawdzenie czy funkcja bubblesort działa poprawnie:
    def test_bubblesort(self):
        sorted_list, _ = bubblesort(self.sorted_list)
        self.assertEqual(sorted_list, self.sorted_list)
        
        sorted_list, _ = bubblesort(self.reversed_list)
        self.assertEqual(sorted_list, self.sorted_list)

        sorted_list, _ = bubblesort(self.equal_values_list)
        self.assertEqual(sorted_list, self.equal_values_list)

        sorted_list, _ = bubblesort(self.random_list)
        self.assertEqual(sorted_list, sorted(self.random_list))

    #! Sprawdzenie liczby porównań w bubblesort:
    def test_bubblesort_comparisons(self):
        _, comparisons = bubblesort(self.sorted_list)
        self.assertLessEqual(comparisons, 1000 * (1000 - 1) // 2)

        _, comparisons = bubblesort(self.reversed_list)
        self.assertLessEqual(comparisons, 1000 * (1000 - 1) // 2)

    #! Testy czasowe dla quicksort
    def test_quicksort_performance(self):
        t_sorted = timeit(lambda: quicksort(self.sorted_list), number=self.iterations)
        print(f"Quicksort sorted list: {t_sorted / self.iterations:.6f} sec")

        t_reversed = timeit(lambda: quicksort(self.reversed_list), number=self.iterations)
        print(f"Quicksort reversed list: {t_reversed / self.iterations:.6f} sec")

        t_equal = timeit(lambda: quicksort(self.equal_values_list), number=self.iterations)
        print(f"Quicksort equal values list: {t_equal / self.iterations:.6f} sec")

        t_random = timeit(lambda: quicksort(self.random_list), number=self.iterations)
        print(f"Quicksort random list: {t_random / self.iterations:.6f} sec")

    #! Testy czasowe dla bubblesort
    def test_bubblesort_performance(self):
        t_sorted = timeit(lambda: bubblesort(self.sorted_list), number=self.iterations)
        print(f"Bubblesort sorted list: {t_sorted / self.iterations:.6f} sec")

        t_reversed = timeit(lambda: bubblesort(self.reversed_list), number=self.iterations)
        print(f"Bubblesort reversed list: {t_reversed / self.iterations:.6f} sec")

        t_equal = timeit(lambda: bubblesort(self.equal_values_list), number=self.iterations)
        print(f"Bubblesort equal values list: {t_equal / self.iterations:.6f} sec")

        t_random = timeit(lambda: bubblesort(self.random_list), number=self.iterations)
        print(f"Bubblesort random list: {t_random / self.iterations:.6f} sec")

if __name__ == '__main__':
    unittest.main()
