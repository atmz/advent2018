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
	best = (0,0)
	for i,v in guards.iteritems():
		best_min = max(set(v), key=v.count)
		if best_min>best[1]:
			best = (i,best_min)
	print best
	
	return best_min*int(best[0].strip('#'))


print solve()