
class fruit():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

    class new_fruit():
        pass
    
    
    
def fruit_list(**kwargs):
    """this function show the list of the fruit"""
    for key,value in kwargs.items():
        print(key,value)

#print(fruit_list.__doc__)
fruit_list(apple=12, banana =5 , passion= 2, mango =3 ,melon =20)

