def min(*args, **kwargs):
    key = kwargs.get("key", None)
    if args and kwargs:
        if len(args)==1:
            return list(j for i in args for j in i
                        if key(j)==sorted(key(j)
                                          for i in args for j in i)[0])[0]
        return list(i for i in args if key(i) == sorted(key(i) for i in args)[0])[0]
    if len(args)==1:
        return sorted(i for i in args[0])[0]
    return sorted(x for x in args)[0]

def max(*args, **kwargs):
    key = kwargs.get("key", None)
    if args and kwargs:
        if len(args)==1:
            return list(j for i in args for j in i
                        if key(j)==sorted(key(j)
                                          for i in args for j in i)[-1])[0]
        return list(i for i in args if key(i) == sorted(key(i) for i in args)[-1])[0]
    if len(args) == 1:
        return sorted(i for i in args[0])[-1]
    return sorted(x for x in args)[-1]
