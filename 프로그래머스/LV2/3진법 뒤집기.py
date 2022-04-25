def convert(n, m):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, m)
        rev_base += str(mod)

    return rev_base[::-1]


def solution(n):
    temp = convert(n, 3)

    answer = int(temp[::-1], 3)
    return answer