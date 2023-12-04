c=[len({*l[10:39].split()}&{*l[42:].split()})for l in open("day4.txt")]
q=[1]*len(c)
for i,x in enumerate(c):
 for j in range(x):q[i+j+1]+=q[i]
print(sum(2**x//2 for x in c),sum(q))
