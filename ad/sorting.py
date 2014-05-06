import heap
import time

DEBUG = True

# Sorting
def max_sort(mlist):
	idx = len(mlist)-1
	while idx > 0:
		m_idx = max_idx(mlist[:idx+1])
		swap(mlist, idx, m_idx)
		idx -= 1
	return mlist

# Sorting
def max_sort_inplace(mlist):
	idx = len(mlist)-1
	size = len(mlist)
	while idx > 0:
		m_idx = 0
		for i in range(1, size):
			if mlist[i] > mlist[m_idx]:
				m_idx = i
		swap(mlist, idx, m_idx)
		idx -= 1
		size -= 1
	return mlist

def swap(seq, i, j):
	seq[i], seq[j] = seq[j], seq[i]

def insertion_sort(mlist):
	for i in xrange(1, len(mlist)):
		j = i-1
		key = mlist[i]
		while (mlist[j] > key) and (j >= 0):
			mlist[j+1] = mlist[j]
			j -= 1
		mlist[j+1] = key
	return mlist

def bubble_sort(mlist):
	changed = True
	while changed:
		changed = False
		for i in xrange(len(mlist) - 1):
			if mlist[i] > mlist[i+1]:
				mlist[i], mlist[i+1] = mlist[i+1], mlist[i]
				changed = True
	return mlist

def heap_sort(mlist):
	h = heap.Heap(mlist)
	h.buildMaxHeap()
	idx = h.getSize()-1
	while idx > 0:
		h.swap(0, idx)
		h.setSize(h.getSize()-1)
		h.maxHeapify(0)
		idx -= 1
	return h.getHeap()

def merge_sort(mlist):

	def merge(a, b):
		merged = []
		idx_a, idx_b = 0, 0
		while idx_a < len(a) and idx_b < len(b):
			if a[idx_a] < b[idx_b]:
				merged.append(a[idx_a])
				idx_a += 1
			else:
				merged.append(b[idx_b])
				idx_b += 1
		merged.extend(a[idx_a:])
		merged.extend(b[idx_b:])
		return merged

	def divide(mlist):
		size = len(mlist)
		if size < 2:
			return mlist
		middle = size / 2
		return merge(
			divide(mlist[:middle]), 
			divide(mlist[middle:]))

	return divide(mlist)

def quick_sort_rec(mlist):
	size = len(mlist)
	if size <= 1:
		return mlist
	pivot = mlist.pop(size / 2)
	lower = quick_sort_rec(filter(lambda x: x <= pivot, mlist))
	higher = quick_sort_rec(filter(lambda x: x > pivot, mlist))
	return lower + [pivot] + higher

def qs(l):
	if len(l) <= 1: return l 
	p = l.pop(len(l) / 2)
	lo, hi = partition(l, p)
	return qs(lo) + [p] + qs(hi)


def partition(mlist, p):
	t = ([], [])
	for elem in mlist:
		if elem <= p:
			t[0].append(elem)
		else:
			t[1].append(elem)
	return t

def qs_inplace(l):

	def partition(left, right, pivot_idx):
		pivot = l[pivot_idx]
		l[pivot_idx], l[right] = l[right], l[pivot_idx]
		store_idx = left
		for idx in range(left, right):
			if l[idx] <= pivot:
				l[idx], l[store_idx] = l[store_idx], l[idx]
				store_idx += 1
		l[store_idx], l[right] = l[right], l[store_idx]
		return store_idx

	def qs(left, right):
		if left < right:
			pivot_idx = left + (right - left) / 2
			pivot_new_idx = partition(left, right, pivot_idx)
			qs(left, pivot_new_idx - 1)
			qs(pivot_new_idx + 1, right)

	qs(0, len(l)-1)

def counting_sort(array):
	max_val = max(array) + 1 # n
	count = [0] * max_val
	for key in array: # n
		count[key] += 1
	key = idx = 0
	while key < max_val: # n
		c = 0
		while c < count[key]: # bei kleinen ranges <= log(n) = e
			array[idx] = key
			idx += 1
			c += 1
		key += 1
	# 2 * n + n * e => n * (2 + e)
	return array

def min_sort2(l, result=[]):
	return min_sort2(l, result + [l.pop(min(enumerate(l),key=lambda x: x[1])[0])]
		) if l else result

def min_sort1(l, result=[]):
	return min_sort1(l, result + [l.pop(min_idx(l))]) if l else result


def min_idx(mlist):
	idx, minidx = 0, 0
	max_val = mlist[idx]
	while idx < len(mlist):
		if mlist[idx] < mlist[minidx]:
			minidx = idx
		idx += 1
	return minidx


# Helpers
def max_idx(A):
	idxMax = 0
	for i in range(1, len(A)):
		if A[i] > A[idxMax]:
			idxMax = i
	return idxMax;

def minimum(mlist):
	idx = 0
	min_val = mlist[idx]
	while idx < len(mlist):
		possible_min = mlist[idx]
		if possible_min < min_val:
			min_val = possible_min
		idx += 1
	return min_val

def isSorted(mlist):
	idx = 0
	maximum = mlist[idx]
	while idx < len(mlist):
		possible_max = mlist[idx]
		if possible_max >= maximum:
			maximum = possible_max
		else:
			return False
		idx += 1
	return True





