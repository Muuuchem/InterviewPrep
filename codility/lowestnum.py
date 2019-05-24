def solution(A):
    # write your code in Python 3.6
    current = 1
    max_el = max(A)
    while current <= max_el:
        if (current <= 0):
            continue
        elif (current not in A):
            return current
        current += 1
    return current

if __name__ == '__main__':
    ans = solution([1, 3, 6, 4, 1, 2])
    bool_1 = ans == 5
    print(bool_1)
