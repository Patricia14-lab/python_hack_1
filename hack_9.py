"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    count = 1
    limit = 5
    while (count <= limit):
        result.insert (count, '@')
        count += 2 
    return result 

print(fn_hack_9())


