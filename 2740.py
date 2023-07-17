N,M=map(int,input().split())
arr_A=[list(map(int,input().split())) for _ in range(N)]

_,K=map(int,input().split())
arr_B=[list(map(int,input().split())) for _ in range(M)]

Res=[[] for _ in range(N)]
cnt=0

for n in range(N):
  for k in range(K):
    Num=0
    for m in range(M):
      Num+=arr_A[n][m]*arr_B[m][k]
    Res[cnt].append(Num)
  if cnt<M:
    cnt+=1

for i in Res:
  print(" ".join(list(map(str,i))))