"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    count = 5
    while(count>=0):
        result.append(count)
        count-=1
    return result 

print(fn_hack_7())