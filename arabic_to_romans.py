def checkio(data):
    romans = 'IVXLCDM'
    res = ''
    i = ([i for i in str(data)])
    for j in range(len(i)):
        if( 4 > int(i[len(i)-j-1]) > 0 ):
            res = romans[0+j*2]*int(i[len(i)-j-1])+res
        if( int(i[len(i)-j-1]) == 4 ):
            res = romans[0+j*2]+romans[1+j*2]+res
        if( 9> int(i[len(i)-j-1]) > 4):
            res = romans[1+j*2]+romans[0+j*2]*(int(i[len(i)-j-1])-5)+res
        if( int(i[len(i)-j-1]) == 9 ):
            res = romans[0+j*2]+romans[2+j*2]+res
    return res

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
