import unittest
import sorting
import utils

class TestSorting(unittest.TestCase):

    def test_max_sort(self):
    	collection = utils.random_list(100, 1, 1000)
    	result = sorting.max_sort(collection)
    	is_sorted = sorting.isSorted(result)
    	self.assertEqual(True, is_sorted)
    	collection = utils.reversed_sorted_list(1, 100)
    	result = sorting.max_sort(collection)
    	is_sorted = sorting.isSorted(result)
    	self.assertEqual(True, is_sorted)
        collection = utils.sorted_list(1, 1000)
        result = sorting.max_sort(collection)
        is_sorted = sorting.isSorted(result)
        self.assertEqual(True, is_sorted)

    def test_max_sort_inplace(self):
        collection = utils.random_list(100, 1, 1000)
        result = sorting.max_sort_inplace(collection)
        is_sorted = sorting.isSorted(result)
        self.assertEqual(True, is_sorted)
        collection = utils.reversed_sorted_list(1, 100)
        result = sorting.max_sort_inplace(collection)
        is_sorted = sorting.isSorted(result)
        self.assertEqual(True, is_sorted)
        collection = utils.sorted_list(1, 1000)
        result = sorting.max_sort_inplace(collection)
        is_sorted = sorting.isSorted(result)
        self.assertEqual(True, is_sorted)

    def test_insertion_sort(self):
    	collection = utils.random_list(100, 1, 1000)
    	result = sorting.insertion_sort(collection)
    	is_sorted = sorting.isSorted(result)
    	self.assertEqual(True, is_sorted)
    	collection = utils.reversed_sorted_list(1, 100)
    	result = sorting.insertion_sort(collection)
    	is_sorted = sorting.isSorted(result)
    	self.assertEqual(True, is_sorted)
        collection = utils.sorted_list(1, 1000)
        result = sorting.insertion_sort(collection)
        is_sorted = sorting.isSorted(result)
        self.assertEqual(True, is_sorted)

    def test_bubble_sort(self):
    	collection = utils.random_list(100, 1, 1000)
    	result = sorting.bubble_sort(collection)
    	is_sorted = sorting.isSorted(result)
    	self.assertEqual(True, is_sorted)
    	collection = utils.reversed_sorted_list(1, 100)
    	result = sorting.bubble_sort(collection)
    	is_sorted = sorting.isSorted(result)
    	self.assertEqual(True, is_sorted)
        collection = utils.sorted_list(1, 10000)
        result = sorting.bubble_sort(collection)
        is_sorted = sorting.isSorted(result)
        self.assertEqual(True, is_sorted)

    def test_heap_sort(self):
        collection = utils.random_list(10000, 1, 1000)
        result = sorting.heap_sort(collection)
        is_sorted = sorting.isSorted(result)
        self.assertEqual(True, is_sorted)
        collection = utils.reversed_sorted_list(1, 10000)
        result = sorting.heap_sort(collection)
        is_sorted = sorting.isSorted(result)
        self.assertEqual(True, is_sorted)
        collection = utils.sorted_list(1, 1000)
        result = sorting.heap_sort(collection)
        is_sorted = sorting.isSorted(result)
        self.assertEqual(True, is_sorted)

    def test_merge_sort(self):
        collection = utils.random_list(10000, 1, 1000)
        result = sorting.merge_sort(collection)
        is_sorted = sorting.isSorted(result)
        self.assertEqual(True, is_sorted)
        collection = utils.reversed_sorted_list(1, 10000)
        result = sorting.merge_sort(collection)
        is_sorted = sorting.isSorted(result)
        self.assertEqual(True, is_sorted)
        collection = utils.sorted_list(1, 10000)
        result = sorting.merge_sort(collection)
        is_sorted = sorting.isSorted(result)
        self.assertEqual(True, is_sorted)

    def test_quick_sort_rec(self):
        collection = utils.random_list(10000, 1, 1000)
        result = sorting.qs(collection)
        is_sorted = sorting.isSorted(result)
        self.assertEqual(True, is_sorted)
        collection = utils.reversed_sorted_list(1, 10000)
        result = sorting.quick_sort_rec(collection)
        is_sorted = sorting.isSorted(result)
        self.assertEqual(True, is_sorted)
        collection = utils.sorted_list(1, 10000)
        result = sorting.quick_sort_rec(collection)
        is_sorted = sorting.isSorted(result)
        self.assertEqual(True, is_sorted)

    def test_quick_sort_inplace(self):
        collection = utils.random_list(10000, 1, 1000)
        sorting.qs_inplace(collection)
        is_sorted = sorting.isSorted(collection)
        self.assertEqual(True, is_sorted)
        collection = utils.reversed_sorted_list(1, 10000)
        sorting.qs_inplace(collection)
        is_sorted = sorting.isSorted(collection)
        self.assertEqual(True, is_sorted)
        collection = utils.sorted_list(1, 10000)
        sorting.qs_inplace(collection)
        is_sorted = sorting.isSorted(collection)
        self.assertEqual(True, is_sorted)

    def test_counting_sort(self):
        collection = utils.random_list(100, 1, 100)
        sorting.counting_sort(collection)
        is_sorted = sorting.isSorted(collection)
        self.assertEqual(True, is_sorted)
        collection = utils.reversed_sorted_list(1, 100)
        sorting.counting_sort(collection)
        is_sorted = sorting.isSorted(collection)
        self.assertEqual(True, is_sorted)
        collection = utils.sorted_list(1, 10000)
        result = sorting.counting_sort(collection)
        is_sorted = sorting.isSorted(result)
        self.assertEqual(True, is_sorted)


class TestSortingHelpers(unittest.TestCase):

	def test_issorted(self):
		collection = utils.sorted_list(1, 1000)
		result = sorting.isSorted(collection)
		self.assertEqual(True, result)
		collection = utils.reversed_sorted_list(1, 1000)
		result = sorting.isSorted(collection)
		self.assertEqual(False, result)


if __name__ == '__main__':
    unittest.main()



