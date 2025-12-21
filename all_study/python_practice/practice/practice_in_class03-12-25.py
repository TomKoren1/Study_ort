import random

def guessing_game():
    d1=str(random.randint(0,9))
    d2=str(random.randint(0,9))
    d3=str(random.randint(0,9))
    d4=str(random.randint(0,9))
    full_random=d1+d2+d3+d4
    guessed=False
    while not guessed:
        guess=input('enter your guess: ')
        valid_guess=True
        if len(guess)!=4:
            valid_guess=False
            print('not the right lenght of guess (you need 4)')
        for c in guess:
            if c>'9' or c<'0':
                valid_guess=False
                print('not correct characters')
        if valid_guess:
            answer=''
            if guess == full_random:
                answer=('you guessed right!!!')
                guessed=True
            else:
                for i in range(4):
                    if(full_random[i]==guess[i]):
                        answer+='+'
                    if guess[i] in full_random and full_random[i]!=guess[i]:
                        answer+='*'
                    if guess[i] not in full_random:
                        answer+='-'
            print(answer)

def charnum_in_strlist(l):
    check=True
    for index,s in enumerate(l):
        if len(l)>26 or chr(ord('a')+index) not in s:
            check=False
    print(check)

def all_chars_in_all_str(l):
    all_letters=l[0]
    check=True
    for s1 in l:
        for ch in s1:
            if(ch not in all_letters):
                check=False
        if(len(all_letters)!= len(s1)):
            check=False
    print(check)

