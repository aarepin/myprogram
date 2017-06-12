def check_connection(network, first, second):
    p=[first]
    i=([{i.split('-')[0],i.split('-')[1]} for i in network])
    for z in range(len(i)):
        for j in i:
            if j.intersection(p):
                p+=j
    return bool(second in set(p))
