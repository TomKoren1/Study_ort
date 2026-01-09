
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
    def lend_book(self):
        self.copies-=1
    def return_book(self):
        self.copies+=1

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
            
    