n = int(input())
arr = [0 if pow(i,0.5) % 1 else 1 for i in range(n+1)] 

_min = 4
for i in range(int(pow(n,0.5)), 0, -1):
    if arr[n]: 
        _min=1
        break
    elif arr[n-i**2] : 
        _min=2
        break
    else:
        for j in range(int(pow(n-pow(i,2),0.5)), 0, -1):
            if arr[(n-i**2)-j**2]: 
                _min=3
print(_min)