from collections import OrderedDict

def Orders():
    sportTeams =[("Royals",(18,12)),("Royals",(18,12)),
                 ("Cardinals",(20,20)),("Dragons",(22,8)),
                 ("Kings",(15,15)),("Chargers",(20,10)),
                 ("Jets",(16,14)),("Warriprs",(25,5))]
    sortedTeams =sorted(sportTeams,key=lambda x:x[1][0] ,reverse=True)
    teams= OrderedDict(sortedTeams)
    print(teams)

    tm,wl= teams.popitem(False)
    print("Top teams:",tm,wl)


    for i,team in enumerate(teams,start=1):
        print(i,team)
        if i== 4:
            break
    a = OrderedDict({"a" :1,"b" : 2 ,"c":1})
    b = OrderedDict({"a" :1,"b" : 2 ,"c":1})
    c = {"a" :1,"c":1,"b" : 2 }
    d= OrderedDict({"a": 1, "c": 1, "b": 2})
    print("Is Equal a and b: ", a==b)
    print("Is Equal a and b: ", a == c)
    print("Is Equal a and b: ", a == d)