
# LIFO - Last in First Out
class Stack():

	def __init__(self):
		self.stack = []

	def pushAll(self, elems):
		for elem in elems:
			self.stack.append(elem)

	def push(self, elem):
		self.stack.append(elem)

	def pop(self):
		try:
			self.stack.pop()
			return self
		except IndexError:
			print "Cannot pop from an empty Stack!"

	def empty(self):
		return self.stack == []

	def head(self):
		try:
			return self.stack.pop(0)
		except IndexError:
			print "Cannot take a head from an empty Stack!"

	def __repr__(self):
		return "Stack( " + ", ".join(map(str, self.stack)) + " )"

