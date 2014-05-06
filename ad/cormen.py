import math
import utils

def inversionOf(seq):

	result = []
	for idx1, e1 in enumerate(seq):

		for idx2, e2 in enumerate(seq):

			t1, t2 = seq[idx1], seq[idx2]
			if idx1 < idx2 and t1 > t2: 
				result.append((t1, t2))

	return result

def subsetSumOfTwo(seq, x):
	idx1 = 0
	while idx1 < len(seq):
		idx2 = 0
		while idx2 < len(seq):
			if idx1 != idx2:
				s = seq[idx1] + seq[idx2]
				if s == x:
					return True
			idx2 += 1
		idx1 += 1
	return False


def sortAndCount(l):
	if len(l) <= 1:
		return (0, l)
	else:
		middle = len(l) / 2
		a = l[:middle]
		b = l[middle:]
		ca = sortAndCount(a)
		cb = sortAndCount(b)
		cl = mergeAndCount(a, b)
	return (ca[0] + cb[0] + cl[0], l)

def mergeAndCount(a, b):
	merged = []
	count, a_size = 0, len(a)
	aidx, bidx = 0, 0
	while aidx < a_size and bidx < len(b):
		if a[aidx] <= b[bidx]:
			merged.append(a[aidx])
			aidx += 1
		else:
			merged.append(b[bidx])
			bidx += 1
			count += (a_size - aidx)
	merged.extend(a[aidx:])
	merged.extend(b[bidx:])
	return (count, merged)


# A[x]-A[y] | x>y
def gordonGecko(A):
	res = -1
	min_idx, max_idx = 0, 1
	min_value = A[0]
	for i in range(1, len(A)):
	    tmp_max = max(res, A[i] - min_value)
	    if tmp_max > res:
	    	max_idx = i
	    	res = tmp_max
	    min_value = min(min_value, A[i])
	    i += 1
	if res <= 0:
		return (-1, -1, -1)
	min_idx = min(enumerate(A[:max_idx]), key=lambda x: x[1])[0]
	return (min_idx, max_idx, res)




