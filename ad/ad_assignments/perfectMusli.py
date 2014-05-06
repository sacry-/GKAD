from itertools import combinations
import time
import random

MAX_VOL = 30
INFINITY_CORRECTION = 1.0001


def printList(l):
	for idx, elem in enumerate(l):
		print "%d. %s" % (idx + 1, str(elem))


### RATING
def calculateRatio(atuple):
	vol, price = atuple[1], atuple[2]

	# Zero division error (none, eliminated before)
	# INFINITY_CORRECTION -> if calc is infinity correct it by factor
	atuple[3] = 1.0 / (price * (MAX_VOL * INFINITY_CORRECTION - vol))

	return atuple


def accuPriceVol(combi):
	for prod in combi[0]:
		vol, price = prod[1], prod[2]
		# accum volume of this combination
		combi[1] += vol
		# accum price of this combination
		combi[2] += price
		# if partially accumulated volume is higher than max_vol
		# don't calculate any longer and return instead
		if combi[1] > MAX_VOL:
			return []
	return combi


### HEURISTICS
def maxPossibleListSize(prodl):

	# Worstcase is O(n^2) because we'd have to call 
	# the min function n times on n comparisons

	idx, accu = 0, 0
	# copy..
	tmp_prodl = prodl[:]

	# closure..
	def popAndMin(tmp_prodl):
		m = tmp_prodl[0]
		outeridx = 0
		for idx, elem in enumerate(tmp_prodl[1:]):
			if elem[1] < m[1]:
				outeridx = idx
		# Remove element at outerindex and get item.
		# from that item just return the volume
		return tmp_prodl.pop(outeridx)[1]

	# Actual loop -> terminates if accu is higher
	# than volume or the temporary list is empty
	while accu < MAX_VOL and tmp_prodl:
		accu += popAndMin(tmp_prodl)
		idx += 1

	return idx



### MAIN ALGORITHM
def maxRatioByPartialPowerset(aset):

	# Sum up from smallest to largest element in this list and
	# return the index of the maximum size the smallest elements 
	# could actually have before stepping over the MAX_VOL.
	# In the next step only generate powerset of max_len size.
	max_len = maxPossibleListSize(aset)
	print "Maximal Length: %d" % max_len

	max_rated_elem = ["None", 0, 0, -1]

	for step in range(1, max_len + 1):
		for comb in combinations(aset, step):

			# Calculate Ratio
			tmp = accuPriceVol(
				# [Set, vol, price, ratio]
					[comb, 0, 0, 0]
					)
				
			if tmp:
				# Only Calculate the rating if the tmp
				# has any actual elements
				currCombination = calculateRatio(tmp)
				if currCombination[3] > max_rated_elem[3]:
					max_rated_elem = currCombination

	return max_rated_elem


### MAIN CALL	
def perfectCereal(prodl):
	# Filter all Products that are equal or lower to
	# the MAX_VOL
	prodl = filter(lambda x: x[1] <= MAX_VOL, prodl)

	# No Products left cause none fits in the cup
	if prodl:
		return maxRatioByPartialPowerset(prodl)

	else:
		return []


## Testcases
prods = [
	("cherry", 5, 2),
	("walnut", 10, 14),
	("banana", 20, 14),
	("honey", 13, 6),
	("sugar", 21, 6), #5
	("chocolate", 1, 9),
	("strawberry", 34, 10),
	("apple", 20, 12),
	("corn", 17, 8),
	("blueberry", 1, 1) #10
]

prods6 = [
	("cherry", 5.0, 2.0),
	("walnut", 5.0, 8.0),
	("banana", 2.0, 7.0),
	("honey", 13.0, 6.0),
	("sugar", 21.0, 6.0),
	("chocolate", 1.0, 4.0)
]

prods7 = [
	("cherry", 10.0, 2.0),
	("walnut", 10.0, 2.0),
	("banana", 10.0, 2.0),
	("honey", 10.0, 6.0),
	("sugar", 10.0, 6.0),
	("chocolate", 10.0, 4.0),
	("apple", 20, 4.5)
]

def createList(vol_from, vol_to):
	volumes = [x for x in xrange(vol_from, vol_to)]
	prices = [x for x in xrange(5,45)]
	names = ["x"+str(name) for name in xrange(vol_from, vol_to)]
	return zip(names, volumes, prices)

def createRandomList(size, vol_from, vol_to):
	volumes = [random.randint(vol_from, vol_to) for x in range(size)]
	prices = [x for x in xrange(5,45)]
	names = ["x"+str(name) for name in xrange(0, size)]
	return zip(names, volumes, prices)

def time_it(f, args):
	print "With size of List: %d and Max Volume of: %d" % (len(args), MAX_VOL)
	t1 = time.time()
	res = f(args)
	t2 = time.time()
	print "Total Time needed: %d Seconds" % (t2-t1)
	return res

def printInt():	
	print perfectCereal(prods)
	print perfectCereal(prods6)
	print perfectCereal(prods7)

#print time_it(perfectCereal, createList(1, 32))
print time_it(perfectCereal, createRandomList(25, 1, 5))

