
def solve():
	#input is just 2 numbers, so I have hardcoded them
	players = 479
	last_marble = 71035
	state=[0]
	scores = [0 for i in range(0,players)]
	current_player = 0
	current_marble_index = 0
	for i in range(1, last_marble+1):
		current_player+=1
		if current_player>= players:
			current_player=0
		if i % 23 != 0:
			current_marble_index+=2
			if current_marble_index>len(state):
				current_marble_index-=len(state)
			state.insert(current_marble_index,i)
		else:
			scores[current_player]+=i
			current_marble_index-=7
			if current_marble_index<0:
				current_marble_index+=len(state)
			scores[current_player]+=state[current_marble_index]
			del state[current_marble_index]
		#print state
	return max(scores)

# Initial implementation was too slow for part 2 - list insertion/deletion is not constant time in Python
# Instead, let's use a linked list
class Node:
    def __init__(self, val=None):
        self.val = val
        self.pre = None
        self.next = None

def p(state):
	i = 0
	first = state
	s = ''
	while first!=state or i==0:
		i+=1
		s+= str(state.val) 
		s+= ' '
		state = state.next
	print s

def solve2():
	#input is just 2 numbers, so I have hardcoded them
	players = 479
	last_marble = 7103500
	state_len=1
	state=Node(0)
	state.pre=state
	state.next=state
	scores = [0 for i in range(0,players)]
	current_player = 0
	for i in range(1, last_marble+1):
		current_player+=1
		if current_player>= players:
			current_player=0
		if i % 23 != 0:
			state = state.next
			old_next = state.next
			new_node = Node(i)
			new_node.next=state.next
			new_node.pre=state
			state.next.pre=new_node
			state.next=new_node
			state=new_node
		else:
			scores[current_player]+=i
			for foo in range(0,7):
				state = state.pre
			scores[current_player]+=state.val
			state.pre.next = state.next
			state.next.pre = state.pre
			state=state.next
	return max(scores)

print solve()
print solve2()