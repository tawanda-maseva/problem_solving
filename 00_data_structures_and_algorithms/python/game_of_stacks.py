# Status: In progress...
# This solution currrently fails 9/14 tests; wrong results
def twoStacks(x, a, b):
	'''Print max that can be removed from stack'''
	stackA, stackB, picked_stack = [], [], []
	total = 0
	while a != [] or b != []: # reveser the input stacks
		if a != []:
			stackA.append(a.pop())
		if b != []:
			stackB.append(b.pop())
	while total <= x:
		if (len(stackA) != 0) & (len(stackB) != 0):
			if (stackA[-1] <= stackB[-1]) & (stackA[-1]+total <= x):
				pick = stackA.pop()
				total += pick
				picked_stack.append(pick)
			elif (stackB[-1] <= stackA[-1]) & (stackB[-1]+total <= x):
				pick = stackB.pop()
				total += pick
				picked_stack.append(pick)
			else:
				return len(picked_stack)
		elif (len(stackA) == 0) & (len(stackB) == 0):
			return len(picked_stack)
		else: #(len(stackA)== 0) or (len(stackB) == 0):
			if len(stackA) == 0:
				if stackB[-1]+total <= x:
					pick = stackB.pop()
					total += pick
					picked_stack.append(pick)
				else:
					return len(picked_stack)
			else: #len(stackB) == 0
				if stackA[-1]+total <= x:
					pick = stackA.pop()
					total += pick
					picked_stack.append(pick)
				else:
					return len(picked_stack)

#a = [4,2,4,6,1]
#b = [2,1,8,5]
a = [1,1,1,1,1]
b = [1,1,1,1]
#a = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22,
# 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
#b = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25,
# 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
print(twoStacks(10, a, b))




				