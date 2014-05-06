import unittest
import utils
from cormen import gordonGecko
from cormen import inversionOf
from cormen import sortAndCount
from cormen import subsetSumOfTwo

class TestStack(unittest.TestCase):

    def test_subset_sum(self):
        collection = [5,4,3,2,1]
        result = subsetSumOfTwo(collection, 9)
        self.assertEqual(True, result)
        result = subsetSumOfTwo(collection, 11)
        self.assertEqual(False, result)

    def test_sort_and_count(self):
        collection = [5,4,3,2,1]
        result = sortAndCount(collection)[0]
        self.assertEqual(10, result)
        collection = [4,3,2,1]
        result = sortAndCount(collection)[0]
        self.assertEqual(6, result)

    def test_inversion_of(self):
        collection = [4,3,2,1]
        result = inversionOf(collection)
        self.assertEqual([(4,3),(4,2),(4,1),(3,2),(3,1),(2,1)], result)

    def test_gordon_gecko(self):
        self.assertEqual((0,3,7), gordonGecko([2,5,2,9,3,4,0,2]))
        self.assertEqual((0,7,17), gordonGecko([3,5,7,9,4,4,7,20]))
        self.assertEqual((5,7,18), gordonGecko([3,19,7,9,4,2,7,20]))
        self.assertEqual((0,1,1), gordonGecko([1,2]))
        self.assertEqual((0,1,9), gordonGecko([1,10,2,2,1,1,0,0]))
        self.assertEqual((5,6,6), gordonGecko([5,3,7,5,6,2,8,5,1]))
        self.assertEqual((0,4,9), gordonGecko([1,2,3,4,10,6,7,8,9,10]))
        self.assertEqual((-1,-1,-1), gordonGecko([2,1]))
        self.assertEqual((-1,-1,-1), gordonGecko([2,2]))
        self.assertEqual((-1,-1,-1), gordonGecko([3,3,2,2,1,1,0,0]))

if __name__ == '__main__':
    unittest.main()