def checkio(gr):

###горизонталь
    for i in (-1,0,1):
        a=gr[1+i]
        if len(set(a))==1 and a!='...':
            return a[0]

### диагональ
    a="".join(gr[1+i][1+j] for i in (-1,0,1) for j in (-1,0,1) if i==j)
    if len(set(a))==1 and a!='...':
        return a[0]

####диагональ обратная
    a="".join(gr[1+i][1+j] for i in (-1,0,1) for j in (-1,0,1) if i==-j)
    if len(set(a))==1 and a!='...':
        return a[0]

#### вертикаль
    for k in (-1,0,1):
        a="".join(gr[1+i][1+k] for i in (-1,0,1))
        if len(set(a))==1 and a!='...':
            return a[0]

    return 'D'

if __name__ == '__main__':
 #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

