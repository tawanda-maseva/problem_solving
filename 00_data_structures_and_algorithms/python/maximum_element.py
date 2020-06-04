'''
Print maximum value from a sequence of values that are added to
the stack.

Difficulty: EASY
'''

import fileinput

stack = []
max_stack = []
for line in fileinput.input():
    input_given = line.rstrip() # remove newline
    instruction = input_given[:2].strip()
    if instruction == '1': # push command
    	element = int(input_given[2:])
    	if stack == []:
    		stack.append(element)
    		max_stack.append(element)
    	else:
    		stack.append(element) # push int into stack
    		if element >= max_stack[-1]:
    			max_stack.append(element)
    elif instruction == '2': # pop and address max
    	if stack == []:
    		pass
    	else:
    		removed_element = stack.pop()
    		if removed_element == max_stack[-1]:
    			max_stack.pop() # remove the max element
    elif instruction == '3':
    	# return maximum element
    	print(max_stack[-1])
    else:
    	pass


