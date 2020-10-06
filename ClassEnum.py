from enum import Enum,unique,auto

@unique
class Fruit(Enum):
    Apple =1
    BANANA =2
    ORANGE =3
    TOMATO =4
    PEAR = auto()



def classDef():
     print(Fruit.BANANA)
     print(type(Fruit.BANANA))
     print( Fruit.BANANA.name ,Fruit.BANANA.value )
     print( Fruit.PEAR.name ,Fruit.PEAR.value )


     myFruits ={}
     myFruits[Fruit.BANANA] ="Come Mr Rabiei"
     print(myFruits[Fruit.BANANA] )

