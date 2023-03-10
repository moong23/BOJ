import sys
a, b = map(int, input().split())
pokemon = dict()
pokemon2 = dict()
for i in range(a):
    t_str = input()
    pokemon[i+1] = t_str
    pokemon2[t_str] = i+1

for _ in range(b):
    c = sys.stdin.readline().rstrip()
    if c.isdigit():
        print(pokemon[int(c)])
    else:
        print(pokemon2[c])
