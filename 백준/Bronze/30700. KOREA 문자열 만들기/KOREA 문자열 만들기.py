inString = input()

answer = 'KOREA' * 200

idx = 0


for x in inString:
  if x == answer[idx]:
    idx += 1

print(idx)