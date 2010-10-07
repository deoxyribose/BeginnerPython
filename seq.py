def find_s(seq, goal):
	s = 0
	vec = []
	for i in range(len(seq)-1, -1, -1):
		
		if (s+seq[i]<=goal):
			s += seq[i]
			vec.append(1)
		else:
			vec.append(0)
			
		if (s==goal):
			vec.reverse()
			return vec
		
	return -1;