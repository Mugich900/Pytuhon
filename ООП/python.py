class SomeClass():
    __someHideNumber = 42
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __call__(self,x,y):
        return x*y
    @staticmethod
    def staticSayHello():
        print('Hello, world!')
    def Calculate(self):
        return self.x + self.y

def squareMethod(self,x):
    return x*x

SomeClass.square = squareMethod   #добавляет метод в класс
n = SomeClass(2,3)
print(n.square(3))
n.staticSayHello()                #обращение к статическому методу
SomeClass.staticSayHello()        #обращение к статическому методу
print(n(2,3)) #вызов __call__
print(n._SomeClass__someHideNumber)