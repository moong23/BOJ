N = int(input())
save = []

for _ in range(N):
    testcase = list(map(str, input().split()))
    for i, word in enumerate(testcase):
        if word[0].lower() not in save:
            save.append(word[0].lower())
            testcase[i] = f"[{word[0]}]{word[1:]}"
            print(" ".join(testcase))
            break
    else:
        for i, word in enumerate(testcase):
            for j, char in enumerate(word):
                if char.lower() not in save:
                    save.append(char.lower())
                    testcase[i] = word[:j] + f"[{char}]" + word[j + 1:]
                    print(" ".join(testcase))
                    break
            else:
                continue
            break
        else:
            print(" ".join(testcase))
