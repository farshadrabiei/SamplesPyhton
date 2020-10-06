from collections import Counter
def Counters():
    class1=["B1","B2","C1","D1","F1","H1","K1","J1","J1","M1","P1","S1"]
    class2=["B2","B3","C2","D2","G1","K2","J1","J2","Sam","Tara","Z1"]


    c1 =Counter(class1)
    c2 =Counter(class2)

    print(c1["J1"])

    print(sum(c1.values())," students in class 1")

    c1.update(class2)
    print(sum(c1.values()), " students in class 1")

    print(c1.most_common(5))

    c1.subtract(class2)
    print(sum(c1.values()), " students in class 1")
    print(c1.most_common(5))
    # اشتراک میباشد
    print(c1 & c2)

