from itertools import permutations


def isPrime(x):
    # print(x)
    if(x == 0):
        return False
    if(x == 1):
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True  # 소수임


def cnt_prime(val):
    cnt = 0
    # print(val)
    for i in val:
        if(isPrime(int(i))):
            cnt += 1
    # print('cnt: '+str(cnt))
    return cnt


def solution(numbers):
    answer = 0
    for i in range(len(numbers)):
        tmp_str = list()
        check_list = list()
        for tmp in list(permutations(list(numbers), i+1)):
            tmpp_str = ''
            for j in tmp:
                tmpp_str += j
            for k in check_list:
                if(k == (tmpp_str)):
                    break
            else:
                check_list.append((tmpp_str))
                # if(i != len(str(int(tmpp_str)))):
                if(tmpp_str[0] != '0'):
                    tmp_str.append((tmpp_str))
        # print(tmp_str)
        answer += cnt_prime(tmp_str)
    return answer


numbers = "002"
print('sol : ' + str(solution(numbers)))
