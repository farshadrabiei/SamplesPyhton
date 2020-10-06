def mainUtil():
    list1=[1,2,3,0,4,5,6]
    #TODO: any
    print(any(list1))
    # TODO: any
    #بخاطر وجود صفر 0
    #اگر صفر را برداریم درست می شود
    print(all(list1))
    #min and max
    print('min :', min(list1))
    print('max :', max(list1))
    print('sum :', sum(list1))

def iterator():
    days =['sun','mon','tue','wed','thu','fri','sat']
    daysFr =['dim','lun','mar','mer','jeu','ven','sam']
    # ctrl + /  Comment line
    # i= iter(days)
    # print(next(i))
    # print(next(i))
    # print(next(i))


    # with open('testfile.txt','r') as fp:
    #     for line in  iter(fp.readline,''):
    #         print(line)

    # for m in range(len(days)):
    #     print(m+1,days[m])

    for i,m in enumerate(days,start =1):
        print(i,m)

    for i,m in enumerate(zip(days,daysFr),start=1):
        print(i,m[0],'=',m[1],'in french')
def filterFunc(x):
    if x %2 == 0:
        return False
    return True


def filterFunc2(x):
     if x.isupper():
         return False
     return True
def squareFunc(x):
    return x**2

def toGrade(x):
    if(x>=90):
        return "A"
    elif(x>=80 and x<90):
        return "B"
    elif (x >= 70 and x < 80):
        return "C"
    elif (x >= 65 and x < 70):
        return "D"
    else:
        return "F"

def transform():
    nums=(1,8,4,5,13,26,381,410,58,47)
    chars="abcDeFGHiJKLmnioP"
    grades=(81,89,94,78,61,66,99,74)
    # odds=list(filter(filterFunc,nums))
    # print(odds)
    # lower=list(filter(filterFunc2,chars))
    # print(lower)


    # print(list(map(squareFunc, nums)))
    # print(list(filter(squareFunc, nums)))
    #
    # print(grades)

    grades = sorted(grades)
    print(grades)
    letters  = list(map(toGrade,grades))

    print(letters)
    