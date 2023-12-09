	l = [[int(i) for i in s.split()] for s in open('day9.txt')]
	def r(m): return m[-1] + r([b-a for a, b in zip(m, m[1:])]) if any(m) else 0
	print(sum(r(i) for i in l), sum(r(i[::-1]) for i in l))
