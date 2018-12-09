big = 99999999999999999999
def sort_string(s):
	s = [l for l in s]
	s.sort()
	return ''.join(s)

def input():
	return [line for line in open('input', 'r')]

def sorted_input():
	i = [line for line in open('input', 'r')]
	i.sort()
	return i


def process_child_old(stack):
	result = 0
	children = stack.pop()
	metadata = stack.pop()
	child_values= []
	for i in range(0,children):
		result+=process_child(stack)
	for i in range (0,metadata):
		result+=stack.pop()
	return result

def process_child(stack):
	result = 0
	children = stack.pop()
	metadata = stack.pop()
	child_values= []
	if children==0:
		for i in range (0,metadata):
			result+=stack.pop()
	else:
		for i in range(0,children):
			child_values.append(process_child(stack))
		for i in range (0,metadata):
			index = stack.pop()
			if index>0 and index <=children:
				result+=child_values[index-1]
	return result

def solve():
	s = input()[0].split()
	s.reverse()
	stack = [int(i) for i in s]
	print stack
	return process_child(stack)



print solve()