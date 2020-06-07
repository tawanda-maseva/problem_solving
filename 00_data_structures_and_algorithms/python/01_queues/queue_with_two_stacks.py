'''This code implements a queue using two stacks'''
import fileinput

class Stack():
	'''Create a stack Abstract Data Type'''
	def __init__(self):
		self.items = []

	def push(self, element):
		self.items.append(element)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[-1]

	def is_empty(self):
		return self.items == []

	def size(self):
		return len(self.items)

class Queue():
	'''Implement a queue using two stacks'''
	def __init__(self):
		self.stackA = Stack()
		self.stackB = Stack()

	def enqueue(self, item):
		'''add a new element to the end of the queue'''
		if self.stackB.is_empty(): # push element to stackB.
			self.stackB.push(item)
		else:
			# pop elements from stackB and push into stackA
			while not self.stackB.is_empty():
				element = self.stackB.pop()
				self.stackA.push(element)

			self.stackA.push(item) # push the enqueued item
			# pop elements from stacA and push into stackB
			while not self.stackA.is_empty():
				element = self.stackA.pop()
				self.stackB.push(element)

	def deque(self):
		'''remove the element from the front of the queue
		and return it.
		'''
		return self.stackB.pop()
	def peek(self):
		'''Return the front element of the queue'''
		print(self.stackB.peek())

def main():
	'''Solve the hackerrank problem'''
	q_model = Queue()
	for line in fileinput.input():
		input_given = line.rstrip() # remove newline
		instruction = input_given[:2].strip()
		if instruction == '1':
			element = input_given[2:]
			q_model.enqueue(element)
		elif instruction == '2':
			q_model.deque()
		elif instruction == '3':
			q_model.peek()
		else:
			pass

main()





