# for i in range(int(input())):
#     str = input()
#     score = 0
#     o_score = 1
#     for x in str:
#         if x == 'O':
#             score += o_score
#             o_score += 1
#         else:
#             o_score = 1
#     print(score)

for a in range(int(input())):
    score = 0
    o_score = 1
    ox = input()  # OOXXOXXOOO
    for x in ox:  # OOXXOXXOOO
        if x == 'O':
            score += o_score
            o_score += 1
        elif x == 'X':
            o_score = 1
    print(score)
