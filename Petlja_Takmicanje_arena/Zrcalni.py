#100 poena
def zrcalni(num):
    for digit in num:
        if digit in ['1','2','3','4','5','6','7','9']: return "NE"
    
    if len(num) == 1: return "DA"

    if num[-1] == '0': return "NE"
    
    return "DA"

print(zrcalni(input()))