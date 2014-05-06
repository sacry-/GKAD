
DEBUG = True

def bestInvestment(kurs=[]):
	minimum = minimumList(kurs)
	maximum = maximumList(kurs)
	result = bestInvest(minimum, maximum)

	if DEBUG:
		print "initial list: %s" % str(kurs)
		print "minimum list: %s" % str(minimum)
		print "maximum list: %s" % str(maximum)
		print "min_max list: %s" % str(zip(minimum, maximum))
		print "result: %s" % str(result)

	return result


def bestInvest(minimum, maximum):

	kzip = zip(minimum, maximum)

	def minimumIndex():
		max_diff, min_idx = -1, -1
		for idx, elem in enumerate(kzip):
			possible_max = elem[1] - elem[0]
			if possible_max > max_diff:
				max_diff, min_idx = possible_max, idx
		return min_idx

	def maximumIndex(min_idx, max_val):
		k_from_min = kzip[min_idx:]
		max_offset = min_idx - 1
		for elem in k_from_min:
			if elem != max_val:
				return max_offset
			max_offset += 1
		return max_offset

	min_idx = minimumIndex()
	max_val = kzip[min_idx]
	max_idx = maximumIndex(min_idx, max_val)
	max_diff = max_val[1] - max_val[0]

	if max_diff <= 0:
		return (-1, -1, -1)

	return (min_idx, max_idx, max_diff)


def maximumList(kurs):
	result = kurs[:] # copy kurs
	maximum = kurs[-1] # last element
	idx = len(kurs)-1

	# kurs = [2,5,2,9,3,4,0,2]
	# result = [9, 9, 9, 9, 4, 4, 2, 2]
	while idx >= 0:
		if kurs[idx] > maximum:
			maximum = kurs[idx]

		result[idx] = maximum
		idx = idx-1

	return result


def minimumList(kurs):
	result = []
	minimum = kurs[0]
	
	for elem in kurs:
		if elem < minimum:
			minimum = elem
		result.append(minimum)

	return result



# TEST
def price(k):
	return k[2]

def assertEquPrice(expected, was, msg):
	a = expected
	b = was
	if a == b:
		print msg
		return True
	print "Was expected: %s" % str(a)
	print "Actually was: %s" % str(b)
	raise Exception("False! Error: " + str(msg))

def shouldBeAnOptimalOf(expected, course, err_message):
	assertEquPrice(expected, bestInvestment(course), err_message)

def positive_test():
	print "Positive Test"
	shouldBeAnOptimalOf((0,3,7), [2,5,2,9,3,4,0,2], "")

	shouldBeAnOptimalOf((0,7,17), [3,5,7,9,4,4,7,20], "")

	shouldBeAnOptimalOf((5,7,18), [3,19,7,9,4,2,7,20], "")

	shouldBeAnOptimalOf((0,1,1), [1,2], "")

	shouldBeAnOptimalOf((0,1,9), [1,10,2,2,1,1,0,0], "")
	
	shouldBeAnOptimalOf((5,6,6), [5,3,7,5,6,2,8,5,1], "")

	shouldBeAnOptimalOf((0,9,9), [1,2,3,4,10,6,7,8,9,10], "")

def negative_test():
	print "Negative Test"
	shouldBeAnOptimalOf((-1,-1,-1), [2,1], "")

	shouldBeAnOptimalOf((-1,-1,-1), [2,2], "")

	shouldBeAnOptimalOf((-1,-1,-1), [3,3,2,2,1,1,0,0], "")


positive_test()
negative_test()

print "ALL TESTS SUCCEEDED' SWAG SWAG \u266b YOLOSAWAG \u266b"

