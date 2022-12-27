el = "abcdefghijklmnopqrstuvwxyz"
eu = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(a):
    l , q , w = [i for i in a.split()] , [], ''
    for j in l:
        k = 0
        for s in j:
            if s.isalpha():
                k+=1
        q.append(k)
    e = 0
    for j in l:
        for s in j:
            if s.isalpha():
                if s in el:
                    w += el[(el.index(s)+q[e])%26]
                elif s in eu:
                    w += eu[(eu.index(s)+q[e])%26]
            else :
                w += s
        e += 1
        w += ' '
    print(w)

y = input()
encrypt(y)