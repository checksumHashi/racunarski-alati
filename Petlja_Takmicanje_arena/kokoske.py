# nit radi nit je gotov nit je dobar pokusaj
def funk() -> int:
    #define
    ID = []
    POS = []
    counted_chickens = set()
    #input
    N = int(input())
    for _ in range(N):
        temp = [int(x) for x in input().split()]
        ID.append(temp[0])
        POS.append(temp[1])

    checked = set()
    fast = -1
    for i in range[ID]:
        for j in range[POS]:
            if ID[i] not in checked:
                if fast != POS[j]: 
                    fast+=1
        checked.add(ID[i])
        

    return 1

print(funk())