def rotate(mtrx):
    s=''.join(mtrx[len(mtrx)-j-1][i] for i in range(len(mtrx))for j in range(len(mtrx[i])))
    return [s[0:4],s[4:8],s[8:12],s[12:16]]
                   

def recall_password(grl, pwd):
    result=''
    for i in range(4):
        result=result+''.join(pwd[i][j] for i in range(len(pwd)) for j in range(len(pwd[i]))if grl[i][j]=='X')
        grl=rotate(grl)
    return result 
