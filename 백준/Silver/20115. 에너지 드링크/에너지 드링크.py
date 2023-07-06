# https://www.acmicpc.net/problem/20115

Num = int(input())

drinks = list(map(int, input().split(' ')))

drinks.sort(reverse=True)

print(sum(drinks[1:])/2 + drinks[0])