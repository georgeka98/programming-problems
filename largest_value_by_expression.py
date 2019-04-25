import sys

def largest_result(a,b,c):
    
    params = [x for x in [a,b,c] if x >= 1 if x <= 9]
    
    if len(params) == 3:
        result = 1
        if a*b > a+b and b*c > b+c:
            result = a*b*c
        elif a*b <= a+b and b*c > b+c:
            result = (a+b)*c
        elif a*b > a+b and b*c <= b+c:
            result = a*(b+c)
        else:
            result = (a+b)*c if (a+b)*c >= a*(b+c) else a*(b+c)
        return result
    
    return 0

a,b,c = input().split()
a,b,c = int(a),int(b),int(c)]

print(largest_result(a,b,c))
