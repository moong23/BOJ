import sys
from collections import deque, defaultdict

flip_position = [
    [1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0, 1, 0, 0]
]


class Node:
    def __init__(self, coins, move):
        self.coins = coins
        self.move = move


def is_answer(coins):
    return coins == "HHHHHHHHH" or coins == "TTTTTTTTT"


def get_next_strings(curr):
    next_strings = []
    for i in range(8):
        next = ''
        for j in range(9):
            if flip_position[i][j] == 1:
                next += flip(curr[j])
            else:
                next += curr[j]
        next_strings.append(next)
    return next_strings


def flip(a):
    return 'T' if a == 'H' else 'H'


def solve(cases):
    results = []
    for coins in cases:
        map = defaultdict(lambda: -1)
        deque_obj = deque([Node(coins, 0)])
        map[coins] = 0
        answer_move = -1

        while deque_obj:
            curr = deque_obj.popleft()
            if is_answer(curr.coins):
                answer_move = curr.move
                break
            next_list = get_next_strings(curr.coins)
            for next_str in next_list:
                if map[next_str] == -1:
                    map[next_str] = curr.move + 1
                    deque_obj.append(Node(next_str, curr.move + 1))
        results.append(answer_move)
    return results


input = sys.stdin.read
data = input().strip().split()

tc = int(data[0])
cases = [''.join(data[1 + i*9:10 + i*9]) for i in range(tc)]

results = solve(cases)
for result in results:
    print(result)
