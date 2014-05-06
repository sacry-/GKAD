

def linear_search(elem, collection):
	idx = 0
	while idx < len(collection):
		if elem == collection[idx]:
			return True
		idx += 1
	return False


def faculty(n):
	result = 1
	for elem in range(0, n):
		result = result * (elem + 1)
	return result


def maximum(collection):
	idx = 0
	max_val = collection[idx]
	while idx < len(collection):
		possible_max = collection[idx]
		if possible_max > max_val:
			max_val = possible_max
		idx += 1
	return max_val

def maximumBy(cmpBy, collection):
	idx = 0
	max_val = collection[idx]
	while idx < len(collection):
		possible_max = collection[idx]
		if cmpBy(possible_max, max_val):
			max_val = possible_max
		idx += 1
	return max_val

def binary_search(elem, collection):
	first, last = 0, len(collection) - 1
	m, idx = 0, -1
	while first <= last and idx < 0:
		m = first + (last - first) / 2
		if collection[m] < elem:
			first = m + 1
		elif collection[m] > elem:
			last = m - 1
		else:
			idx = m
	return idx












