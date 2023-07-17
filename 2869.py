a, b, v = map(int, input().split())
k = (v-b)/(a-b)
print(int(k) if k == int(k) else int(k)+1)


#a, b, k

# (a-b) * x + b >= v

# x = (v-b)/(a-b)

# int(x) == x => x
# int(x) != x => x+1
