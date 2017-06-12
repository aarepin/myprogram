import collections
def checkio(data):
    
    ### create alphabet w index
    alpha='abcdefghijklmnopqrstuvwxyz'
    dical={}
    for x in range(len(alpha)):
        dical[alpha[x]]=x+10 
        
    ### change indexes for new alphabet 
    for k in range(len(data)+1):
        for x in data:
            for z in range(len(x)):
                for y in range(len(x)-1):
                    if dical[x[y]]>=dical[x[y+1]] and x[y]!=x[y+1]:
                        dical[x[y]]=dical[x[y+1]]-0.1
    ### union data
    data=''.join(y for x in data for y in x)
    
    ### sort dictionary by value
    dical=collections.OrderedDict(sorted(dical.items(), key=lambda t: t[1]))
    return ''.join(x for x in dical.keys()if x in data)
