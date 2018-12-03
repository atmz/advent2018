twos = 0
threes = 0
with open('input', 'r') as f:
	for line in f:
		counts = {}
		for c in line:
			if c not in counts:
				counts[c]=0
			counts[c]+=1
		two = False
		three = False
		for count in counts.values():
			if count == 2:
				two = True
			if count == 3:
				three = True
		if two:
			twos+=1
		if three:
			threes+=1
print twos*threes

