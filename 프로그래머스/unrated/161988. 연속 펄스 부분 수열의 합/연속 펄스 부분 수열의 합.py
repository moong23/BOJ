def partial_max(arr):
    cache = [None] * len(arr)
    cache[0] = arr[0]
    for i in range(1, len(arr)):
        cache[i] = max(0, cache[i-1]) + arr[i]
    return max(cache)


def solution(sequence):
    pos_seq, neg_seq = [], []
    pivot = -1
    for x in sequence:
        neg_seq.append(x * pivot)
        pivot *= -1
        pos_seq.append(x * pivot)
    # print(pos_seq, neg_seq)
    return max(partial_max(pos_seq), partial_max(neg_seq))