"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    txt = "fooziman"
    txt = txt.replace( 'o', '0').replace('i','1').replace('a', '@')
    txt = txt.upper()
    txt = list(txt)
    return txt 


print(fn_hack_10())

