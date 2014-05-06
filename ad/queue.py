

# FIFO - First in First Out
class Queue():

	def __init__(self):
		self.queue = []

	def front(self):
		try:
			return self.queue.pop(0)
		except IndexError:
			print "Cannot take the front from an empty Queue!"

	def enqueueAll(self, elems):
		for elem in elems:
			self.enqueue(elem)

	def enqueue(self, elem):
		self.queue.append(elem)

	def dequeue(self):
		try:
			self.queue.pop(0)
			return self
		except IndexError:
			print "Cannot dequeue from an empty Queue!"

	def empty(self):
		return self.queue == []

	def __repr__(self):
		return "[" + ", ".join(map(str, self.queue)) + "]"

