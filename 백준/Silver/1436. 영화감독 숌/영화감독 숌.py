n = int(input())

cnt = 0

find_str = 666

while True:
    if '666' in str(find_str):
        cnt += 1
    if cnt == n:
        print(find_str)
        break
    find_str += 1
