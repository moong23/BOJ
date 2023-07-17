in_str = input()

str_len = len(in_str)
if in_str == str_len * in_str[0]:
    print(-1)
else:
    if in_str == in_str[::-1]:
        print(str_len - 1)
    else:
        print(str_len)