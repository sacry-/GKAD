import unittest
import stack
import queue
import heap
import btree
import utils
from random import shuffle
from sorting import isSorted

class TestStack(unittest.TestCase):

    def test_stack(self):
    	s = stack.Stack()
    	self.assertEqual(True, s.empty())
    	s.push(1)
    	self.assertEqual(False, s.empty())
    	self.assertEqual(1, s.head())
    	self.assertEqual(True, s.empty())
    	s.pushAll([4,3,5,2])
    	self.assertEqual(False, s.empty())
    	self.assertEqual(4, s.head())
    	self.assertEqual(3, s.head())
    	self.assertEqual(s, s.pop())
    	self.assertEqual(s, s.pop())
    	self.assertEqual(True, s.empty())


class TestQueue(unittest.TestCase):

    def test_queue(self):
    	q = queue.Queue()
    	self.assertEqual(True, q.empty())
    	q.enqueue(1)
    	self.assertEqual(False, q.empty())
    	self.assertEqual(1, q.front())
    	self.assertEqual(True, q.empty())
    	q.enqueueAll([4,3,5,2])
    	self.assertEqual(False, q.empty())
    	self.assertEqual(4, q.front())
    	self.assertEqual(3, q.front())
    	self.assertEqual(q, q.dequeue())
    	self.assertEqual(q, q.dequeue())
    	self.assertEqual(True, q.empty())

class TestHeap(unittest.TestCase):

    def test_heap(self):
        # Randomization
        shuffled = [16, 12, 15, 11, 8, 7, 13, 7, 6, 1, 2, 4, 5, 9, 0, -1]
        shuffle(shuffled)
        # Creation
        h = heap.Heap(shuffled)
        self.assertEqual(False, h.isMaxHeap())
        h.buildMaxHeap()
        self.assertEqual(True, h.isMaxHeap())
        self.assertEqual(16, h.maximum())
        self.assertEqual(-1, h.minimum())
        # increaseKey
        h.insert(19)
        self.assertEqual(19, h.maximum())
        self.assertEqual(True, h.isMaxHeap())
        # Merge
        h2 = heap.Heap(shuffled)
        self.assertEqual(False, h2.isMaxHeap())
        h2.buildMaxHeap()
        self.assertEqual(True, h2.isMaxHeap())
        h.merge(h2)
        self.assertEqual(True, h.isMaxHeap())
        self.assertEqual(19, h.maximum())
        self.assertEqual(-1, h.minimum())
        # extractMaximum
        m = h.extractMaximum()
        self.assertEqual(16, h.maximum())
        self.assertEqual(19, m)
        # Insertion
        h.insert(17)
        self.assertEqual(17, h.maximum())
        m = h.extractMaximum()
        self.assertEqual(17, m)
        self.assertEqual(16, h.maximum())
        # Immutable Heapsort
        result = h.heapSort()
        is_sorted = isSorted(result)
        self.assertEqual(True, is_sorted)
        self.assertEqual(True, h.isMaxHeap())
        self.assertEqual(16, h.maximum())
        self.assertEqual(-1, h.minimum())

class TestBinaryTree(unittest.TestCase):

    def test_binary_tree(self):
        l = utils.sorted_list(0, 7)
        # Creation
        b = btree.BinTree()
        while l:
            b.tinsert(utils.takeRdm(l))
        # Functions
        result = b.treeSort()
        is_sorted = isSorted(result)
        self.assertEqual(True, is_sorted)
        b.treeMap(b.getRoot(), lambda x: x + 1)
        for idx, elem in enumerate(b.treeSort()):
            self.assertTrue(result[idx] < elem)
        # Search/Min/Max
        b.tinsert(16)
        searched = b.search(b.getRoot(), 16)
        self.assertEqual(btree.Node(16), searched)
        mi = b.minimum(b.getRoot())
        self.assertEqual(1, mi)
        ma = b.maximum(b.getRoot())
        self.assertEqual(16, ma)
        # Special To String
        #btree.TreeRepr(b).toS()
        #print b.pathCount(b.getRoot())

if __name__ == '__main__':
    unittest.main()

