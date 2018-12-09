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

def solve():
	coordss = input()
	coords=[]
	maxes =[0,0]
	mins=[999999,999999]
	for s in coordss:
		split = s.split()
		x =int(split[0].strip(','))
		y = int(split[1])
		coords.append([x,y])
		if x>maxes[0]:
			maxes[0]=x
		if y>maxes[1]:
			maxes[1]=y
		if x<mins[0]:
			mins[0]=x
		if y<mins[1]:
			mins[1]=y
	closest =[]
	for x in range(mins[0],maxes[0]+1):
		for y in range(mins[1],maxes[1]+1):
			closest = big
			closest_coord = None
			for i in range(0, len(coords)):
				distance = abs(coords[i][0]-x) + abs(coords[i][1]-y)
				if distance<closest:
					closest_coord=i
					closest = distance
				elif  distance==closest:
					closest_coord = None
			if(closest_coord is not None):
				coords[closest_coord][2]+=1
				if x in [mins[0],maxes[0]]or y in [mins[1],maxes[1]]:
					coords[closest_coord][2]=-big

	best = 0
	print coords
	for coord in coords:
		if coord[2]>best:
			best=coord[2]
	return best

def solve_2():
	coordss = input()
	coords=[]
	maxes =[0,0]
	mins=[999999,999999]
	for s in coordss:
		split = s.split()
		x =int(split[0].strip(','))
		y = int(split[1])
		coords.append([x,y,0])
		if x>maxes[0]:
			maxes[0]=x
		if y>maxes[1]:
			maxes[1]=y
		if x<mins[0]:
			mins[0]=x
		if y<mins[1]:
			mins[1]=y
	answer=0
	for x in range(mins[0]-99,maxes[0]+99):
		for y in range(mins[1]-99,maxes[1]+99):
			closest = 99999999999
			closest_coord = None
			distance = 0
			for i in range(0, len(coords)):
				distance+= (abs(coords[i][0]-x) + abs(coords[i][1]-y))
			if distance < 10000:
				answer+=1
	return answer

print solve()
print solve_2()