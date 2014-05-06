
# recursive Devide-Merge function
# to calculate the optimal investment time
def optInvest(k):
	
	def isNotPotenceOfTwo(k):
		k_len = len(k)
		has_ones  = filter(lambda x: x ==  '1', bin(k_len)[2:])
		has_exactly_one = len(has_ones) == 1 and k_len != 1
		if not has_exactly_one:
			print "You can't use a k with length of %d. It must be a potence of 2!" % k_len
			return True
		return False

	def divide(k, depth):
		if TRACEMODE:
			print "Divide(%s): %s" % (depth, str(k))
		
		size = len(k)
		
		if size == 2:
			# remember. devive is called with a midified k with indices
			fst, snd = k[0], k[1]
			t = (fst[1],snd[1],snd[0]-fst[0])
			return t if price(t) > 0 else (-1,-1,-1)
		
		left_side = k[:size/2]
		right_side = k[size/2:]

		# removed all the fuzz, coz it didn't help here...
		l_optimal = divide(left_side, depth + 1)
		r_optimal = divide(right_side, depth + 1)
		
		# calculate the minimum/maximum price of the left/right sublist
		# save them as (pricce, idx) tuples
		left_min = findTupleByKey(left_side, lambda x, y: x < y)
		right_max = findTupleByKey(right_side, lambda x, y: x > y)
		middle_price = right_max[0] - left_min[0]
		# now the best investment over the left-right boundry is composed
		
		middle = (left_min[1], right_max[1], middle_price)
		return merge(l_optimal, r_optimal, middle, depth)
	
	def merge(left, right, middle,  depth):
		if TRACEMODE:
			print "Merge(%s): left %s; right %s; middle %s" % (depth, left, right , middle)
		
		if price(left) <= -1 and price(right) <= -1 and price(middle) <= -1:
			return (-1,-1,-1)
		
		# take best of three
		b1 = mMax(left, right)
		return mMax(middle, b1)
	
	# given a course-list with indexed elements (f.e. [(2,0), (1,1), (6, 3), ..])
	# this function returns the (price, index) tuple with the
	# maximum/minimum price (depending on the lambda comp_func)
	def findTupleByKey(course, comp_func):
		m = course[0]
		for curr_tuple in course:
			if comp_func(curr_tuple[0], m[0]):	# compare prices
				m = curr_tuple
		return m
	
	if isNotPotenceOfTwo(k):
		return (-1, -1, -1)

	# make _k save it's original indices
	# this is to avoid hard debuggable index-pushing/index-correction
	_k = zip(k, [x for x in xrange(len(k))])
	
	return divide(_k, 0)


# Iterativ O(n**2) algorithm
def bestInvestment(k):
	time_i, time_j = k[0], k[1]
	best_of_all = (0, 1, time_j-time_i)

	i, n = 0, len(k)
	while i < n-1:

		j = i + 1
		while j < n:

			time_i, time_j = k[i], k[j]
			best_of_all = mMax(
				(i, j, time_j-time_i), 
				best_of_all
				)

			j += 1

		i += 1

	if price(best_of_all) > 0:
		return best_of_all
	# there was no optimal investment	
	return (-1,-1,-1)

# returns the tuple with the higher win
def mMax(t1, t2):
	if price(t1) > price(t2):
		return t1
	return t2

# display recursion trace or not
TRACEMODE = True

# Always comparing the thrd element of the tuple, because it represents the
# profit. it may be, that the actual indices are diffrent, however
# with identical amout of profit. they shall not be considered
# different.
def price(k):
	return k[2]

def assertEquPrice(expected, was, msg):
	a = price(expected)
	b = price(was)
	if a == b:
		print msg
		return True
	print "Was expected: %s" % str(a)
	print "Actually was: %s" % str(b)
	raise Exception("False! Error: " + str(msg))

def shouldBeAnOptimalOf(expected, course, err_message):
	assertEquPrice(expected, bestInvestment(course), err_message)
	assertEquPrice(bestInvestment(course),optInvest(course), err_message)

assertEquPrice((-1,-1,-1), optInvest([2,5,2,9,3,4,0,2,1]), "optInvest should not be able to process lists with non 2^n size")

shouldBeAnOptimalOf((0,3,7), [2,5,2,9,3,4,0,2], "")

shouldBeAnOptimalOf((0,7,17), [3,5,7,9,4,4,7,20], "")

shouldBeAnOptimalOf((5,7,18), [3,19,7,9,4,2,7,20], "")

shouldBeAnOptimalOf((0,1,1), [1,2], "")

shouldBeAnOptimalOf((-1,-1,-1), [2,1], "")

shouldBeAnOptimalOf((-1,-1,-1), [2,2], "")

shouldBeAnOptimalOf((-1,-1,-1), [3,3,2,2,1,1,0,0], "")

shouldBeAnOptimalOf((0,1,9), [1,10,2,2,1,1,0,0], "")

shouldBeAnOptimalOf((5,6,6), [5,3,7,5,6,2,8,5], "")

print "ALL TESTS SUCCEEDED' SWAG SWAG \u266b YOLOSAWAG \u266b"
# For those who cannot display it in shell:
# http://www.fileformat.info/info/unicode/char/266b/index.htm



