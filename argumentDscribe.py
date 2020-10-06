def additional(base,*args):
    result = base
    for arg in args:
        result += arg
    return result


def mainArg():
    print(additional(5,10,15,20))
    print(additional(1,2,3))

    myNum=[5,10,15,20]
    print(additional(*myNum))
