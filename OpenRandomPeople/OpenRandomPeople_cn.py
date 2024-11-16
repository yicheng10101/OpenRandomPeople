import random
import os
if os.path.isfile("/name.txt"):
    print('错误,请创建"name.txt"到运行目录下,里面填人名,用空格隔开(文件名区分大小写,编码为Utf-8)')
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
    print('欢迎ヾ(≧▽≦*)o')
    num = input('请输入随机人数(^///^):')
    if is_number(num):
        f = 1
    else:
        f = 0
    if f == 0:
        print('输入错误')
        continue
    num = int(num)
    if num > len(name):
        print('输入错误')
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
        print('被抽中的人是:','[‘',name[random.randint(0,len(name)-1)],'’]','（*＾-＾*）')
        os.system('cls')
    print('被抽中的人是:',listt,'（*＾-＾*）')
    print('一共',len(listt),'人(*^▽^*)')
    os.system('pause')
    del lis
    os.system('cls')
