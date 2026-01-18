
class Account:
    def __init__(self,userName:str,password:str):
        self.userName=userName
        self.current_pass=password
        self.pass_history=[password]+['']*9
    
    def valid_password(self,password):
        number_flag=0
        big_letters_flag=0
        len_flag=len(password)>=8
        special_letters_flag=False
        same_pairs_flag=True
        for i,ch in enumerate(password):
            if '9'>=ch>='0':
                number_flag=1
            if 'A'>=ch>='Z':
                big_letters_flag=1
            if not 'A'<=ch<='Z' and not 'a'<=ch<='z' and not '0'<=ch<='9':
                print('here')
                special_letters_flag=True
            if i>0 and ch==password[i-1]:
                same_pairs_flag=False
        return (number_flag+big_letters_flag+special_letters_flag+same_pairs_flag+len_flag)>=3
            
   



p1=Account("tom","24")
print(p1.valid_password('111#aB'))




class dog:

    def __init__(self,name):
        self.name=name
        self.color='black'
        self.geza=''

class dogs:
    def __init__(self):
        self.allDogs=[]
    def anotherdog(self,name):
        if name in self.allDogs:
            print('ewdfa')
        else:
            abc=dog(name)
            self.allDogs.append(abc)








