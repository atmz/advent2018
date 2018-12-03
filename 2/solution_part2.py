def solve():
	for i in range(0,25):
		lines = [l[:i] + l[i+1:] for l in open('input', 'r')]
		lines.sort()
		last = ""
		for line in lines:
			if line == last:
				return line
			last = line

print solve()