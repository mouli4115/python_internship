print("hello world",end="----")
print("hello","i am","mouli",sep="__")


#16-4-24


# a=int(input("enter a"))
# b=int(input("enter b"))
# print("sum is ",a+b) 
# a=5
# print(type(a))
# a=int(input("enter a"))
# if a%2==0:
#     print("even")
# else:
#     print("odd")
# print("outside")

#if(cond):
   #stat inside 
#stat outside 
#if(cond):
  #true
#else:
  #false 
#outside 



# number=int(input("enter a number below 4"))
# match number:
#     case 1:
#         print('1')
#     case 2:
#         print('2')
#     case 3:
#         print('3')
#     case _:
#         print("invalid")

# s='agdnvkddfk'
# for i in s:
#     print(i)

# name=input("enter name")
# for i in name:
#     if(i in 'aeiouAEIOU'):
#         print(i,end=" ")
    
# s='abcd efgh'
# i=0
# while i<len(s) and s[i]!=" ":
#         print(s[i])
#         i+=1
# print(i)




#17-04-2024


# def add(m:int,n:int)->int:
#     return m+n
# m=int(input())  
# n=int(input())  
# print(add(m,n))


# flag=0
# i=2
def prime(n):
   for i in range(2,n):
       if n%i == 0:
           return False
       else:
           return True
             
# c=prime(number)
# if c==1:
#     print("not prime")
# else:
#     print("prime")
# a=int(input('enter a number'))
# b=int(input('enter a number'))
# for i in range(a,b+1):
#     if prime(i):
#         print(i)

# a=int(input('enter a number'))
# temp=a
# i=0
# while(a!=0):
#     rem=a%10
#     i=i*10+rem
#     a=a//10
# print(i)

# s='abcdefg'
# print(s.find('d'))
# candies = [2,3,5,1,3]
# l=max(candies)
# print(l)

#19-04-24


# a={'a','b','c','d'}
# b={'e','f','g'}

# #print(a.pop(),a)
# #print(a.remove(2),a)
# #print(a.discard('e'),a)

# print(a|b)

# d={1:23,'a':24,'abc':90}
# for i in d:
#     print(i)

# class cse:
#     def __init__(self,name,rollno):
#         self.n=name
#     def fun(self):
#         print(self.n)
# obj=cse('mouli','27')
# obj.fun()


class rectangle:
    
    def __init__(self,l,b):
        self.len=l
        self.bre=b
    def printing(self):
        print("area is ",self.len*self.bre)
a=int(input("enter length"))
d=int(input("enter breadth"))
obj=rectangle(a,d)
obj.printing()

class circle:
    def __init__(self,radius) -> None:
        self.r=radius
    def printing(self):
        print("area is ",3.14*self.r*self.r)
r=int(input("enter radius"))
obj=circle(r)
obj.printing()        