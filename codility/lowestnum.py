#def solution(A):
#    # write your code in Python 3.6
#    current = 1
#    max_el = max(A)
#    while current <= max_el:
#        if (current <= 0):
#            continue
#        elif (current not in A):
#            return current
#        current += 1
#    return current

def solution(S): 
    # write your code in Python 3.6
    #2 restrictions: at least one uppercase char & cannot contain digits
    #gonna brute force and then optimize
    strings = []
    string = ""
    max = -1
    for i in S:
        if (i.isdigit()):
            if (len(string) >= max and string.lower() != string):
                print(string)
                max = len(string)
            strings.append(string)
            string = ""
            continue
        else:
            string += i
    
    return max

if __name__ == '__main__':
    #ans = solution([1, 3, 6, 4, 1, 2])
    #bool_1 = ans == 5
    #print(bool_1)
    print(solution('a0Ba'))