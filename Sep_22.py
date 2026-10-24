'''

Usage of Super()
#super with arguments --> super().__init__(args)



class Father:
    """Father class with fproperty argument"""
    def __init__(self,fproperty):
        self.fproperty = fproperty
    def father_property(self):
        print(f'Father Property is {self.fproperty}')
class kid(Father):
    """Kid class with kproperty argument"""
    def __init__(self,kproperty,fproperty):
        super().__init__(fproperty) #calling superclass constructor with args
        self.kproperty = kproperty
    def kid_property(self):
        print(f'Kid Property is {self.kproperty}')
        print(f'Total Combined Property is {self.fproperty + self.kproperty}')

u1 = kid(500000,250000)
u1.kid_property()
u1.father_property()
print(u1.__dict__)


#Method Overriding --> Calling supercalss method

super().method()
'''
'''
#Calculating the area of Square,Rectangle

class Square:
    """Area of Square"""
    def __init__(self,x):
        self.x = x
    def area_s(self):
        return f'Area of Square {self.x * self.x}'
    
class Rectangle(Square):
    """Area of Rectangle"""
    def __init__(self,x,y):
        self.y = y
        super().__init__(x)
    def area_r(self):
        return f'area of recatangle {self.x * self.y}'
        super().area()
x,y = map(int,input("Enter values").split(','))
obj1 = Rectangle(2,3)
print(obj1.area_s())
print(obj1.area_r())
x,y = map(int,input("Enter values").split(','))
obj2 = Square(x)

'''

#Multiple Inheritance --> Whatsapp Scenario --> Users,Business Users, Premium Users

'''
Multiple base classes with single derived class

syntax:-

class base1:
    statemenet/......
    .....
class base2:
    statement..........
    .....
class base3:
    statement........
    .....
    
'''
'''
class Users:
    """Users class with basic features"""
    def voice_call(self):
        print("User can make voice calls")
class Notifications:
    """Notification reaching out"""
    def send_notifications(self):
        print("User can get pop-up notification")
class PremiumUsers(Users,Notifications):
    """Extra feature added"""
    def verification_badge(self):
        print("User is verified and bluetrick added")
u1 = PremiumUsers()
u1.verification_badge()
u1.voice_call()
print(dir(u1))


'''
'''
#Multilevel Inhertance --> level by level

class base1:
    statement........
    ......
class base2(base1):
    statement...
    ....
class base3(base2):
    statement......
    ....
'''
'''
class User:
    """User class with base function"""
    def send_message(self):
        print("User can send messages")
    def voice_call(self):
        print("Making voice calls")
class BusinessUsers(User):
    """First derived class"""
    def create_catalog(self):
        print("Details added successfully")
class PremiumUsers(BusinessUsers):
    """Second derived class"""
    def verification_badge(self):
        print("Account is verified")

u1 = PremiumUsers()
u1.verification_badge()
u1.create_catalog()
u1.send_message()
u1.voice_call()



'''


class Company:
    """Company budget"""
    def __init__(self, amt):
        self.amt = amt
    def budget(self):
        print(f"Total budget of the company: {self.amt}")

class AI(Company):
    def __init__(self, amt, amt_ai):
        super().__init__(amt)
        self.amt_ai = amt_ai
    def bud1(self):
        print(f"Budget allotted to AI: {self.amt_ai}")

class Infrastructure(Company):
    def __init__(self, amt, amt_inf):
        super().__init__(amt)
        self.amt_inf = amt_inf
    def bud2(self):
        print(f"Budget allotted to Infra: {self.amt_inf}")

class Fundings(Company):
    def __init__(self, amt_f):
        super().__init__(amt, amt_ai, amt_inf)
        self.amt_f = amt_f
    def bud3(self):
        print(f"Budget allotted to Fundings: {self.amt_f}")
        print(f"Remaining budget: {self.amt - self.amt_ai - self.amt_inf - self.amt_f}")

ai_dept = AI(100000, 30000)
ai_dept.budget()
ai_dept.bud1()
print("-" * 30)

infra_dept = Infrastructure(100000, 25000)
infra_dept.budget()
infra_dept.bud2()
print("-" * 30)

fundings_dept = Fundings(100000, 30000, 25000, 20000)
fundings_dept.budget()
fundings_dept.bud3()








        
