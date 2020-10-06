class personnel():
    def __init__(self):
        self.fname ="farshad"
        self.lname = "rabiei"
        self.age = 40

    def __repr__(self):
        return "<Personel class fname:{0},lname:{1},age:{2}>".format(self.fname,self.lname,self.age)

    def __str__(self):
        return "personnel({0},{1},{2})".format(self.fname,self.lname,self.age)

    def __bytes__(self):
        val = "personnel byte:{0},{1},{2}".format(self.fname,self.lname,self.age)
        return bytes(val.encode('utf-8'))

def startUseClass():
    c1 = personnel()
    # print(c1)
    # print(repr(c1))
    print(bytes(c1))