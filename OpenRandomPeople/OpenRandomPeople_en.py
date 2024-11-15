import random
import os
if os.path.isfile("name.txt"):
    print('Error, please create a "name.txt" to the running directory, fill in the name of the person, and separate it with a space (the file name is case-sensitive, encoded as Utf-8)')
    os.system('pause')
    exit(1)
with open('name.txt','r') as f:
    name = f.read()
    name = name.split(' ')
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False
while True:
    os.system('color 97')
    lis = []
    print('Welcomeヾ(≧▽≦*)o')
    num = input('Please enter a random number of people(^///^):')
    if is_number(num):
        f = 1
    else:
        f = 0
    if f == 0:
        print('Error')
        continue
    num = int(num)
    if num > len(name):
        print('Error')
        continue
    for i in range(num):
        a = random.randint(0, len(name)-1)
        a = int(a)
        b = name[a]
        lis.append(b)
    listt = list(set(lis))
    while len(listt) != num:
        a = random.randint(0, len(name)-1)
        a = int(a)
        b = name[a]
        lis.append(b)
        listt = list(set(lis))
    for i in range(50):
        print('The person who was drawn was:','[‘',name[random.randint(0,len(name)-1)],'’]','（*＾-＾*）')
        os.system('cls')
    print('The person who was drawn was:',listt,'（*＾-＾*）')
    print('altogether',len(listt),'peoples(*^▽^*)')
    os.system('pause')
    del lis
    os.system('cls')
