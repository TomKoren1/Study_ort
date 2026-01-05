class Person:
    def __init__(self,name,age,tz):
        self.name=name
        if age<0:
            age=0
        if age>130:
            age=130
        self.age=age
        self.tz=tz
    
    def __str__(self):
        return f"name: {self.name} | age: {self.age} | tz: {self.tz}"

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_tz(self):
        return self.tz
    
    def set_name(self,name):
        self.name=name
    def set_age(self,age):
        if 0<=age<=130:
            self.age=age
    def set_tz(self,tz):
        self.tz=tz

    
    



persons= [Person("tom",24,"32130941"),Person("ron",5,"1245356"),Person("meni",2,"63624264")]

for p in persons:
    print(p)
        