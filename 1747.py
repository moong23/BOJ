prime_arr = [1] * 1005000
prime_arr[0], prime_arr[1] = 0,0

m = int(pow(1005000,1/2))

for i in range(2, m+1):
    if prime_arr[i] == 1:
        for j in range(i+i,1005000, i):
            prime_arr[j] = 0

def isPrime(x):
    for i in range(2, int(pow(x,1/2))+1):
        if x % i == 0:
            return False
    return True

def isPalindrome(x):
    x = str(x)
    if x == x[::-1]:
        return True
    else:
        return False

num = int(input())
while True:
    if isPalindrome(num):
        if isPrime(num):
            print(num)
            break