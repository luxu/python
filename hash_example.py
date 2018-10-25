# coding=utf-8

from hashlib import md5
from pdb import set_trace

a='abcdefghijklmnopqrstuvwxyz'
b='0123456789'
m=input('hash: ')
n=0
c=str(m)
d=0
f=0
e=''
# set_trace()
while(e!=m):
    print(c)
    if str(c[d]) in b:
        memory=b.find(str(c[d]))
        print(f'Memory.: {memory}')
        e+=a[memory]
        d+=1
        f+=1
        print(f'\nMemory.: {memory}\n')


    j=md5(e.encode()).hexdigest()
    print(j)
    if e==m:
        print(f'{m} is {e}')
        break
    else:
        n+=1
    print(n)
