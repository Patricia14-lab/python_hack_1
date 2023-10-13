"""
list: [1,3,5,7,9] output => [3,5,7]
"""

def fn_hack_8():
    ls = [1,3,5,7,9]
    del ls [0]
    del ls [3]
    return ls  
print(fn_hack_8())