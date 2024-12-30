code = list(map(int, input()))

_len = len(code)

dp = [0] * (_len + 1)
dp[0], dp[1] = 1, 1

if code[0] == 0:
    print(0)
else:
    for k in range(1, _len):
        i = k + 1  
        if code[k] > 0:  
            dp[i] += dp[i-1]
        if 10 <= code[k] + code[k-1]*10 <= 26:  
            dp[i] += dp[i-2]
    print(dp[_len] % 1000000)