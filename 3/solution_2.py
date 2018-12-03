def solve():
	result = {}
	answer =0 
	for line in open('input', 'r'):
		l = line.split()
		x,y = l[2].split(',')
		w,h = l[3].split('x')
		x=int(x)
		y=int(y[:len(y)-1])
		w=int(w)
		h=int(h)
		for a in range(x,x+w):
			for b in range(y,y+h):
				if a not in result:
					result[a]={}
				if b not in result[a]:
					result[a][b]=0
				result[a][b]+=1

	for line in open('input', 'r'):
		l = line.split()
		x,y = l[2].split(',')
		w,h = l[3].split('x')
		x=int(x)
		y=int(y[:len(y)-1])
		w=int(w)
		h=int(h)
		ok = True
		for a in range(x,x+w):
			for b in range(y,y+h):
				if(result[a][b]>1):
					ok = False
		if ok == True:
			return line
print solve()