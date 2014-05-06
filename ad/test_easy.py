import unittest
import algorithm_easy
import utils

class TestEasyAlgos(unittest.TestCase):

    def test_linear_search(self):
    	test_list = utils.random_list(20, 1, 100)
    	test_list.append(1)
    	result = algorithm_easy.linear_search(1, test_list)
    	self.assertEqual(True, result)
    	result = algorithm_easy.linear_search(101, test_list)
    	self.assertEqual(False, result)

    def test_faculty(self):
    	result = algorithm_easy.faculty(0)
    	self.assertEqual(1, result)
    	result = algorithm_easy.faculty(1)
    	self.assertEqual(1, result)
    	result = algorithm_easy.faculty(2)
    	self.assertEqual(2, result)
    	result = algorithm_easy.faculty(3)
    	self.assertEqual(6, result)
    	result = algorithm_easy.faculty(4)
    	self.assertEqual(24, result)
    	result = algorithm_easy.faculty(5)
    	self.assertEqual(120, result)

    def test_maximum(self):
    	collection = utils.max_list(100, 1, 500, 501)
    	result = algorithm_easy.maximum(collection)
    	self.assertEqual(501, result)
    	collection = utils.max_list(100, 1, 500, 501)
    	result = algorithm_easy.maximumBy(lambda x, y: x > y, collection)
    	self.assertEqual(501, result)

    def test_binary_search(self):
    	collection = utils.sorted_list(1, 1000)
    	result = algorithm_easy.binary_search(4, collection)
    	self.assertEqual(3, result)
    	result = algorithm_easy.binary_search(0, collection)
    	self.assertEqual(-1, result)
    	collection = []
    	result = algorithm_easy.binary_search(10, collection)
    	self.assertEqual(-1, result)
    	collection = [1]
    	result = algorithm_easy.binary_search(1, collection)
    	self.assertEqual(0, result)
    	collection = [1, 2]
    	result = algorithm_easy.binary_search(2, collection)
    	self.assertEqual(1, result)
    	result = algorithm_easy.binary_search(3, collection)
    	self.assertEqual(-1, result)


if __name__ == '__main__':
    unittest.main()


    
