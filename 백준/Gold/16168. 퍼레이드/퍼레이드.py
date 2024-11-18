def getParent(x):
    if x == parent[x]:
        return x
    
    return getParent(parent[x])

def isSameParent(x, y):
    return getParent(x) == getParent(y)

def unionParent(x, y):
    x = getParent(x)
    y = getParent(y)

    if x<y:
        parent[y] = x
    else:
        parent[x] = y


V, E = map(int, input().split())

parent = [i for i in range(V+1)]

edge = [[] for i in range(V+1)]

for _ in range(E):
    Va, Vb = map(int, input().split())
    edge[Va].append(Vb)
    edge[Vb].append(Va)

    if not isSameParent(Va, Vb):
        unionParent(Va, Vb)

root = getParent(1)

for i in range(2, V+1):
    if root != getParent(i):
        print("NO")
        exit(0)

cnt = 0

for i in range(1, V+1):
    if len(edge[i]) %2 == 1:
        cnt +=1
    if cnt > 2:
        break
if cnt %2 == 0:
    print("YES")
else:
    print("NO")