def solve():
	m = {}
	sorted_lines = [l for l in open('input', 'r')]
	sorted_lines.sort()
	guards = {}
	g = None
	start = None
	end = None
	for line in sorted_lines:
		l = line.split()
		if l[2]=="Guard":
			g = l[3]
			start = None
			end = None
		if l[2]=="falls":
			start = l[1][3:5]
		if l[2]=="wakes":
			end = l[1][3:5]
			mins = range(int(start,10),int(end,10))
			if g not in guards:
				guards[g]=[]
			for m in mins:
				guards[g].append(m)
			start = None
			end = None
	best = (0,0,0)
	for i,v in guards.iteritems():
		minutes = {}
		for minute in v:
			if minute not in minutes:
				minutes[minute]=0
			minutes[minute]+=1
		best_min = (0,0)
		for i2,v2 in minutes.iteritems():
			if v2>best_min[1]:
				best_min = (i2,v2)
		if best_min[1]>best[2]:
			best = (i,best_min[0],best_min[1])
	print best
	
	return best[1]*int(best[0].strip('#'))


print solve()