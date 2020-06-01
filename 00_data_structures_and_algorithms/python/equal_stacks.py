import time

def equalStacks(h1, h2, h3):
    '''Function to find the maximum possible height of stacks
    such that all of the stacks are exactly the same height'''

    if h1 == [] or h2 ==[] or h3 == []:
        return 0 # max is zero if any one is zero

    tot_stack1, tot_stack2, tot_stack3 = [],[],[] # stack of sums at each push
    height_freq = {} # dict of key = height, value = number of stacks with that height
    while (h1 !=[]) or (h2 != []) or (h3 != []):
        # push sums into each of the stacks
        if h1 == []:
            pass
        else:
            if tot_stack1 ==[]:
                tot_height = h1.pop()
                tot_stack1.append(tot_height) # push first element
            else:
                tot_height = h1.pop() + tot_stack1[-1]
                tot_stack1.append(tot_height)
            try:
                height_freq[tot_height] #
            except KeyError:
                height_freq[tot_height] = 1 #set first time frequency
            else:
                height_freq[tot_height] +=1 # increment frequency

        if h2 == []:
            pass
        else:
            if tot_stack2 ==[]:
                tot_height = h2.pop()
                tot_stack2.append(tot_height) # push first element
            else:
                tot_height = h2.pop() + tot_stack2[-1]
                tot_stack2.append(tot_height)
            try:
                height_freq[tot_height]
            except KeyError:
                height_freq[tot_height] = 1 #set first time frequency
            else:
                height_freq[tot_height] +=1 # increment frequency

        if h3 == []:
            pass
        else:
            if tot_stack3 ==[]:
                tot_height = h3.pop()
                tot_stack3.append(tot_height) # push first element
            else:
                tot_height = h3.pop() + tot_stack3[-1]
                tot_stack3.append(tot_height)
            try:
                height_freq[tot_height]
            except KeyError:
                height_freq[tot_height] = 1 #set first time frequency
            else:
                height_freq[tot_height] +=1 # increment frequency

    if 3 not in height_freq.values():
        return 0 # no common heights amongst stacks
    else:
        all_equal_heights = [key for key, value in height_freq.items() if value == 3]
        return max(all_equal_heights)

# tests
#print(equalStacks(h1 = [3,2,1,1,1], h2 = [4,3,2], h3 = [1,1,4,1]))
#print(equalStacks(h1 = [1], h2 = [1], h3 = [1]))

