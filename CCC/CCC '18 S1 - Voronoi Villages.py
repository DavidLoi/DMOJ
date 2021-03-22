n = int(input())

villages = []
for i in range(n):
    v = int(input())
    villages.append(v)

villages.sort()

dist = []
for i in range(n-1):
  dist.append(villages[i+1] - villages[i])

sizes = []
for i in range(len(dist) - 1):
  sizes.append(dist[i] / 2 + dist[i+1] / 2)

sizes.sort()
print(sizes[0])