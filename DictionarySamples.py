from collections import defaultdict
def dicSample():
    fruits=['apple','pear','orange','banana','apple','grape','banana','banana']
    # fruitCounter =defaultdict(int)
    fruitCounter =defaultdict(lambda :100)
    for fruit in fruits:
        # if fruit in fruitCounter.keys():
            fruitCounter[fruit] +=1
        # else:
        #     fruitCounter[fruit] =1

    for (k,v) in fruitCounter.items():
        print(k+':'+str(v))