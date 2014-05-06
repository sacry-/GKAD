import re
import utils
import math

class BinTree():

	def __init__(self, root_val=None):
		if root_val != None:
			self.root = Node(root_val)
		else:
			self.root = root_val

	def inorderTreeWalk(self, node):
		if node:
			self.inorderTreeWalk(node.left)
			print node.data
			self.inorderTreeWalk(node.right)
	
	def pathCount(self, node):
		if node:
			if node.isLeaf():
				return 1
			return (self.pathCount(node.left) + 
				self.pathCount(node.right))
		return 0
		
	def treeSort(self):
		acc = []
		def sort_walk(node):
			if node:
				sort_walk(node.left)
				acc.append(node.data)
				sort_walk(node.right)
		sort_walk(self.root)
		return acc

	def treeMap(self, node, f):
		def inner_map(node):
			if node:
				inner_map(node.left)
				node.setData(f(node.data))
				inner_map(node.right)
		return inner_map(node)

	def search(self, node, k):
		if node == None or k == node.data:
			return node
		if k < node.data:
			return self.search(node.left, k)
		return self.search(node.right, k)

	def minimum(self, node):
		while node.left:
			node = node.left
		return node.data

	def maximum(self, node):
		while node.right:
			node = node.right
		return node.data

	def tdelete(self, val):
		pass

	def tinsert(self, val):
		z = Node(val)
		y = None
		x = self.root
		while x != None:
			y = x
			if z.data < x.data:
				x = x.left
			else:
				x = x.right
		z.setParent(y)
		if y == None:
			self.root = z
		elif z.data < y.data:
			y.left = z
		else:
			y.right = z

	def successorTree(self, node):
		if node.right:
			return self.minimum(node.right)
		y = node.getParent()
		while y and node == y.right:
			node = y
			y = y.getParent()
		if y:
			return y.data
		return None

	def getRoot(self):
		return self.root

	def __repr__(self):
		return "Root(" + str(self.root) + ")"


class Node():

	left, right, data = None, None, None

	def __init__(self, data, left=None, right=None):
		self.parent = None
		self.left = left
		self.data = data
		self.right = right

	def __repr__(self):
		if self.left or self.right:
			return "Node(" + str(self.left) + ", " + str(self.data) + ", " + str(self.right) + ")"
		return "Leaf(" + str(self.data) + ")"

	def setParent(self, parent):
		self.parent = parent

	def isLeaf(self):
		return self.left == None and self.right == None

	def getParent(self):
		return self.parent

	def setLeft(self, left):
		self.left = left

	def setRight(self, right):
		self.right = right

	def setData(self, data):
		self.data = data

	def __eq__(self, other):
		if isinstance(other, Node):
			return (self.data == other.data and 
				self.left == other.left and 
				self.right == other.right)
		return False


class TreeRepr():

	def __init__(self, btree):
		self.root = btree.getRoot()
		self.token = self.tokenize(str(self.root))
		self.to_s = self.parse()

	def toS(self):
		print self.to_s

	def tokenize(self, str_repr):
		token = filter(lambda x: x, 
			map(lambda x: x.strip(), 
				re.split("(\(|\,|\))", str_repr)
				)
			)
		token.insert(0, "(")
		token.insert(0, "Root")
		return token

	def parse(self):
		token = self.token
		t_count, t_offset, t_offset2 = 0, "   ", "..."
		comma = 0
		idx = 0
		acc = "---------------\n"
		while idx < len(token):

			if token[idx] == "Leaf":
				idx += 2
				acc += "Leaf(" + token[idx] + ")"
				acc += "\n" + t_offset*t_count
				idx += 2

			if token[idx] == "(":
				t_count += 1
				acc += "(" + "\n" + t_offset2*t_count

			if token[idx] == ")":
				t_count -= 1
				acc += ")" + "\n" + t_offset*t_count
			
			if token[idx] == "None":
				acc += "None" + "\n" + t_offset*t_count
			
			if token[idx] == ",":
				comma += 1
				if comma % 2 == 0:
					acc += ",\n" + t_offset2*t_count
				else:
					acc += ","

			if token[idx] not in ["(", ")", ",", "Leaf", "None"]:	
				acc += token[idx]

			idx += 1

		acc += ")\n---------------"
		return acc


