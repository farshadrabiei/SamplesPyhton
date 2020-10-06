def CelsisusToFarenhite(temp):
    return (temp * 9/5) +32

def FarenhiteTocelsisus(temp):
    return (temp- 32 ) + 5/9

def mainLambda():
    ctemps=[0,12,34,100]
    ftemps=[32,65,100,212]

    #TODO:
    print(list(map(FarenhiteTocelsisus,ftemps)))
    print(list(map(CelsisusToFarenhite,ctemps)))

    print(list(map(lambda  x : (x- 32 ) + 5/9, ftemps)))
    print(list(map(lambda  x: (x * 9/5) +32, ctemps)))