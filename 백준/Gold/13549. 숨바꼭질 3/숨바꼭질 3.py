from heapq import *

n, k = map(int, input().split())
INF = int(1e9)
visited = set()

q = []
heappush(q, (0, n))
	
while q: 
	d, v = heappop(q)
	if v in visited:
		continue
		
	visited.add(v)

	if v == k:
		print(d)
		break 	
	if v*2 <= 100000 and v*2 not in visited:
		heappush(q, (d, v*2))
		
	if v+1 <= 100000 and v+1 not in visited:
		heappush(q, (d+1, v+1))
		
	if v-1 > -1 and v-1 not in visited:
		heappush(q, (d+1, v-1))