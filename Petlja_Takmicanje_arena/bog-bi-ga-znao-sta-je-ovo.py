def neopadajuci(n):
    n=str(n)
    for i in range(0,len(n)-1):
        if n[i+1]<n[i]:
            return False
    return True


def najblizii(n):
    n=str(n)
    if neopadajuci(n):
        print(str(n))
    else:
        m=""
        for i in range(len(n)-1):
            if int(n[i])>=int(n[i+1]):
                if n[i+1]=='0':
                    if n[i]=="1":
                        m=m+'9'*(len(n)-i-1)
                        break
                    else:
                        m=m+str(int(n[i])-1)+'9'*(len(n)-i-1)
                        break
                elif int(n[i+1])>=int(n[i])//2:
                    m=m+n[i]*(len(n)-i)
                    break
                else:
                    m=m+str(int(n[i])-1)+"9"*(len(n)-i-1)
                    break
            else:
                m=m+n[i]
        if neopadajuci(int(n)-int(m)+int(n)):
            print(str(min(int(n)-int(m)+int(n),int(m))),str(max(int(n)-int(m)+int(n),int(m))))
        else:
            print(m)



n1=input()
najblizii(n1)