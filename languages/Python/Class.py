class User():
    #constuctor
    def __init__(self, _name, _age): #initialize:一打開就一定有的背景資訊
        self.name=_name
        self.age=_age
        self.shopping_cart=[]

    def __str__(self):
        answer=str(self.age)+" years old"+", "+"Name: "+str(self.name)
        return answer
#__str__是後面在print(user1或2)的時候會跑出來的字
    
    def __eq__(self, other):
        try:
            other.age
            other.name
            other.shopping_cart
        except:
            return False
        
        return self.age==other.age and self.name==other.name and \
        self.shopping_cart==other.shoppingcart
#__eq__是用來比較兩個instance的, 後面有程式碼print(user1==user2),那user1就是self而user2是other

    def update_name(self,_new_name):
        self.name=_new_name

    def update_age(self,_new_age):
        self.name=_new_age


    def update_shopping_cart(self,item):
        self.shopping_cart.append(item)
    
    def display_shopping_cart(self):
        current_shopping_cart=self.shopping_cart


user1= User("Janice",16)
user2= User("Jasmine",16)
print(user1.age)
print(user2.name)
user1.update_name("Wendy")
print(user1.name)

#對應__eq__ and __str__
print(user1)
print(user1==user2)
