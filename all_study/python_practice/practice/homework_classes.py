
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
    def lend_book(self):
        self.copies-=1
    def return_book(self):
        self.copies+=1
    def something(self,other):
        print(other)



class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    def after(self,other):
        if self.year > other.year:
            return True
        elif self.year==other.year:
            if self.month > other.month:
                return True
            elif self.month == other.year:
                if self.day> other.day:
                    return True
        return False
    
    def after2(self,other):
        if self.year <other.year:
            return False
        if self.month < other.month:
            return False
        if self.day < self.day:
            return False
        return True

class Worker:

    def __init__(self,name,day,month,year):
        self.name=name
        self.birthday=Date(day,month,year)
    
    def youngest(arr):
        minWorker=arr[0]
        for item in arr:
            if item.birthday.after(minWorker.birthday):
                minWorker=item
        return minWorker.name        
    
class Calendar2024:
    def __init__(self):
        self.days=[31,29,31,30,31,30,31,31,30,31,30,31]
        for i,d in enumerate(self.days):
            print(i,d)
    def num_of_days(self,day,month):
        sum=day
        for i in range(month-1):
            sum+=self.days[i]
        return sum
    
    
cal24=Calendar2024()


d1=Date(5,2,2020)
d2=Date(12,3,2015)




def showAllBooks(arr):
    for b in arr:
        print(b.title)



class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    def borrow_book(self, book):
        self.borrow_book.append(book)
    def return_book(self, book):
        self.borrow_book.remove(book)
    def display_catalog(books):
        for book in books:
            print(f'book: {book.title} {book.author}, copies: {book.copies}')
    def display_members(members):
        for member in members:
            print(f'member: {member.name}')
            for i,book in enumerate(member.borrowed_books):
                print(f'book {i+1}: {book.title} by {book.author}')



class Animal:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        self.adopted=False
    def adopt(self):
        self.adopted=True
    def __str__(self):
        return f'name:{self.name} | age: {self.age} | gender: {self.gender}'

class Adopter:
    def __init__(self,name):
        self.name=name
        self.adopted_animals = []
    def adopt(self,animal):
        self.adopted_animals.append(animal)
        animal.adopt()
    def aviable_for_adoption(animals):
        for animal in animals:
            if animal.adopted==False:
                print(animal)
    def people_adopted(adopters):
        for adopter in adopters:
            print(f'name: {adopter.name} adopted ->')
            for animal in adopter.adopted_animals:
                print(animal)


class Product:
    def __init__(self,name,price,amount):
        self.name = name
        self.price = price
        self.amount = amount
    def updateAmount(self,newAmount):
        self.amount=newAmount
    def __str__(self):
        return f'{self.name}, cost: {self.price}, amount aviable: {self.amount}'


class Order:
    def __init__(self,products,amounts):
        self.orders = []
        for i in products:
            self.orders.append((products[i],amounts[i]))
    def add_product(self,product):
        flag=False
        for order in self.orders:
            if order[0].name == product.name:
                order[1]+=1
                flag=True
        if not flag:
            self.orders.append((product,1))
    def caculateSum(self):
        sum=0
        for order in self.orders:
            sum+=order[0].price * order[1]
        print(f'total cost: {sum}')
        return sum
    def aviableProducts(products):
        for product in products:
            print(product)
    def show_order(self):
        for order in self.orders:
            print(f'{order[1]} {order[0]}')
            
    