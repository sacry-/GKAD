import math
import copy

class Heap():

	# Initialization
	def __init__(self, seq=[]):
		self.heap = seq[:]
		self.size = len(self.heap)

	# n * log n sort
	def heapSort(self):
		if not self.isMaxHeap():
			self.heapify()
		idx, h = self.size - 1, self.copy()
		while idx > 0:
			h.swap(0, idx)
			h.setSize(h.getSize()-1)
			h.maxHeapify(0)
			idx -= 1
		return h.getHeap()	

	def copy(self):
		return copy.deepcopy(self)

	# Mutators
	def buildMaxHeap(self):
		midx = self.father(self.size)
		while midx >= 0:
			self.maxHeapify(midx)
			midx -= 1

	def maxHeapify(self, idx):
		l = self.left(idx)
		r = self.right(idx)

		if l <= self.size-1 and self.heap[l] > self.heap[idx]:
			m = l 
		else:	
			m = idx

		if r <= self.size-1 and self.heap[r] > self.heap[m]:
			m = r

		if m != idx:
			self.swap(idx, m)
			self.maxHeapify(m)

	def isMaxHeap(self):
		return all(self.isMaxIdx(idx) for idx, _ in enumerate(self.heap))

	def maximum(self):
		return self.heap[0]

	def minimum(self):
		mini = None
		for possible_min in self.heap:
			if (possible_min < mini and possible_min != None) or mini == None:
				mini = possible_min 
		return mini

	def insert(self, key):
		self.increaseKey(self.size, key)

	def increaseKey(self, idx, key):
		idx = idx - 1
		self.appendNone(idx)
		self.heap.append(key)
		self.size += 1
		idx = self.size-1
		while idx > 0 and self.heap[self.father(idx)] < self.heap[idx]:
			self.swap(idx, self.father(idx))
			idx = self.father(idx)

	def merge(self, heap):
		for elem in heap.getHeap():
			self.insert(elem)

	def swap(self, idx1, idx2):
		self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

	def extractMaximum(self):
		if self.size < 1:
			return None
		m = self.maximum()
		self.heap[0] = self.heap.pop(self.size-1)
		self.size -= 1
		self.maxHeapify(0)
		return m

	# Helper
	def appendNone(self, idx):
		if idx > self.size:
			for _ in range(self.size, idx):
				self.heap.append(None)
				self.size += 1

	def isMaxIdx(self, idx):
		return self.heap[self.father(idx)] >= self.heap[idx]

	def father(self, idx):
		if idx <= 0: 
			return 0
		return int(math.ceil((idx / 2) - 0.5))

	def left(self, idx):
		return 2 * idx

	def right(self, idx):
		return 2 * idx + 1 


	# Set + Get
	def setHeap(self, seq):
		self.heap = seq[:]
		self.size = len(self.heap)

	def get(self, idx):
		return self.heap[idx - 1]

	def getHeap(self):
		return self.heap[:]

	def getSize(self):
		return self.size

	def setSize(self, size):
		self.size = size

	# To String
	def __repr__(self):
		return "Heap( " + ", ".join(map(str, self.heap)) + " )"

	def cool_repr(self):
		l = [self.heap[0]]
		mod, idx = 2, 1
		temp_l = []
		for elem in self.heap[1:]:
			temp_l.append(elem)
			if idx % mod == 0:
				mod = mod * 2
				idx = 0
				l.append(temp_l)
				temp_l = []
			idx += 1
		if temp_l:
			l.append(temp_l)
		return l
		result = "\n".join(map(lambda x: "\t" + str(x), l))
		return "Heap( \n" + result + "\n)"




