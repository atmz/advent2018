def solution():
	seen = set([0])
	current = 0
	with open('input', 'r') as f:
		while True:
			for line in f:
				current+=int(line)
				if current in seen:
					return current
				seen.add(current)
			f.seek(0)


print solution()
