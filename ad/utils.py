import random
import sys
import math
import time

def timeit(f):
	def decorator(*args):
		t1 = time.time()
		l = f(*args)
		t2 = time.time()
		print "needed: %s" % str(t2-t1)
	return decorator

def random_list(size, _from, _to):
	return [random.randint(_from, _to) for _ in xrange(size)]

def sorted_list(_from, _to):
	return [_ for _ in xrange(_from, _to)]

def takeRdm(seq):
	if len(seq) == 1:
		return seq.pop(0)
	return seq.pop(random.randint(0, len(seq)-1))

def reversed_sorted_list(_from, _to):
	return sorted_list(_from, _to)[::-1]

def max_list(size, _from, _to, max_elem):
	collection = random_list(size, _from, _to)
	return random_insert(collection, max_elem)

def random_insert(collection, elem):
	size = len(collection)
	rdm_idx = random.randint(0,size)
	collection.insert(rdm_idx, elem)
	return collection

def findNextPotenceOfTwoBy(size):
	return int(2**math.ceil(math.log(size, 2)))
