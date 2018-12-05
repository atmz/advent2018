def solve(p):
	i = 0
	while i < (len(p)-1):
			if p[i].lower() == p[i+1].lower() and p[i]!=p[i+1]:
				p = p[:i] + p[(i+2):]
				i=i-1
			else:
				i=i+1
	return len(p)

def solve_2():
	best =9999999999
	sorted_lines = [foo for foo in open('input', 'r')]
	a = [foo.lower() for foo in sorted_lines[0]]
	a.sort()
	a = set(a)
	for l in set(a):
		p = [foo for foo in open('input', 'r')][0]
		p = p.replace(l,'')
		p = p.replace(l.upper(),'')
		size =  solve(p)
		if size < best:
			best = size
	return best

print solve([foo for foo in open('input', 'r')][0])
print solve_2()