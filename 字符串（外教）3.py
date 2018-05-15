# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 15:31:31 2017

@author: lenovo
"""
#String可以直接相加
x='hello '
y='world'
print(x+y)
#任何Input进来的都默认为string 可以进行类型转换
'''
int_num=int(input("Enter a number"))
'''
#sting里面的对应的数字
berry="Strawberry"   #排列方法为0 1 2 3 4 ……
print(berry[:-2])
print(berry[:2])
print(berry[3])      #中括号里面可以为任何的式子得出整数
print(berry[-1])     #表示倒数第一个数
#len()函数，算出string里面有几个元素
print(len(berry))
#用for遍历
count=0
for letter in berry:
    if(letter=='r'):
        count=count+1
print(count)
#在string里面用：
print(berry[0:5])#指的是下标为0到下标为4的数，不包括5
print(berry[6:25])#如果下标溢出，那么就一直从前面那个下标到最后，不会报错
berry[:2]#最前面到下标为2，但是不包括2
berry[2:]#下标为2到最后
berry[:]#全部
#if  in 
if 'r' in berry:
   print('found a r')
#string比大小
'''1.字母按照字典的顺序
   2.大写的字母都小于小写的字母
   3.>.<.>=.==.!=.等，都可以用来比较
ASCLL码： 48开始 0
         65开始 A
         97开始 a
'''
#一些内置函数对String进行修改
#.str.lower()  将其中的字母全部改为小写字母
#str.upper()
print(berry.lower())
#type()
print(type(berry))
#dir()   查看哪些内置函数可以用于这个字符串
'''print(dir(berry))'''
#str.capitalize()   返回一个首字母为大写的字符串
x="hello world"
print(x.capitalize())
#str.center(width[,fillchar])   #将字符串居中，两侧用其他东西补充 或者空格
print(x.center(20,'-'))
#strip即为去掉两边的自己想要去掉的内容（默认为空格）  下面是去掉了两边的'-'
a=x.center(20,'-')
print(a)
print(x.strip('-'))
#rstrip 去掉右边的
b='***hello***'
print(b)
print(b.rstrip('*'))
#find()  返回这个字符串相应的小标 如果有多个 返回最小的那个，如果没有，返回-1
print(x.find('h'))

#format函数可以用来在后面添加要输出的东西  多加在{}
#%d也可以加在里面，不过只能加数字
#%s加字母
i=1
print(" the file has {} lines {}".format(i,i))
print('a b %d'   %1 )
print('a b %s'   %'s')

print("hello",end=' ')       #end='' 可以使输出的时候不换行
print('"world"')
print('hello')

a='hello'
print('h' in a)              #in  返回值为true false
print('h' not in a)          #not in 返回值为true false
print('\n')
print(r'\n')                 #r 使得所有字符串按照字面意思来用



print('bb'>'Ab')


print('a'>'1')

