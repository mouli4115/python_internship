# class rectangle:
    
#     def __init__(self,l,b):
#         self.len=l
#         self.bre=b
#     def printing(self):
#         print("area is ",self.len*self.bre)
# a=int(input("enter length"))
# d=int(input("enter breadth"))
# obj=rectangle(a,d)
# obj.printing()

# class circle:
#     def __init__(self,radius) -> None:
#         self.r=radius
#     def printing(self):
#         print("area is ",3.14*self.r*self.r)
# r=int(input("enter radius"))
# obj=circle(r)
# obj.printing()   

# class royal_enfield:
#     def __init__(self,model_name,color,milage):
#         self.model_name=model_name
#         self.color=color
#         self.milage=milage 
# o1=royal_enfield("classic","black",50)
# o2=royal_enfield("interceptor","grey",50)
# o3=royal_enfield("continental gt","black",30)
# print(o1.model_name,o1.color,o1.milage)
# print(o2.model_name,o2.color,o2.milage) 
# print(o3.model_name,o3.color,o3.milage)


# import turtle
# s=turtle.Turtle()
# s.shape("circle")
# s.speed(0)
# s.width(1)
# # s.color("black")
# turtle.bgcolor("black")
# s.pencolor("green")
# for i in range(200):
#     s.circle(i)
#     s.left(10)
# for i in range(3):
#     s.forward(100)
#     s.left(120)

# import turtle
# import random

# # Setup the screen
# screen = turtle.Screen()
# screen.bgcolor("black")

# # Create a turtle
# t = turtle.Turtle()
# t.speed(0)
# t.width(2)

# # List of colors
# colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# # Function to draw a square
# def square(size):
#     for _ in range(4):
#         t.forward(size)
#         t.right(90)

# # Function to draw a complex pattern
# def draw_pattern():
#     for _ in range(36):
#         color = random.choice(colors)
#         t.color(color)
#         square(100)
#         t.right(10)

# # Draw the pattern
# draw_pattern()

# # Hide the turtle and display the result
# t.hideturtle()
# screen.mainloop()




#20-04-2024




# class a:
#     def fun1(self):
#         print("fun1")
#     def fun2(self):
#         print("fun2")
# class b(a):
#     def fun2(self):
#         print("fun3")
#         a.fun1(self)
#     def fun4(self):
#         print("fun4")
# # o=a()
# p=b()
# p.fun2()



# import math
# x=math.log2(6)
# if(6==2**x):
#     print("ghjf")







# 22-04-2024



# word="Mouli"
# x=list(word)
# print(x) 
# count=0
# c=len(x)
# for i in range(len(x)):
#     if x[i].isupper():
#         count+=1
# print(count)
# if(count==c):
#     print("true")
# elif(count==1):
#     print("true")
# else:
#     print("false")


# import turtle
# s=turtle.Turtle()
# turtle.bgcolor("light blue")
# s.hideturtle()
# s.fillcolor("yellow")
# s.penup()
# s.goto(0,50)
# s.pendown()
# for i in range(10):
#     s.forward(100)
#     s.goto(0,50)
#     s.right(36)

# digits=[1,2,3]
# s=""
# for i in digits :
#     s=s+str(i)
# # print(s) 
# ans=int(s)
# ans+=1
# print(ans)
# d=str(ans)
# # digits=list(d)
# l=[]
# for i in d:
#     l.append(int(i))
# print(l)



# 24-04-2024

# l=[1,2,3,4,5]
# se=9
# si=0
# li=len(l)-1
# while(si<=li):
#     mid=(si+li)//2
#     if(l[mid]==se):
#         print("found")
#         break
#     elif(se>l[mid]):
#         si=mid+1
#     else:
#         li=mid-1
# else:
#     print("not present")




# 25-04-2024

# def fact(n):
#     if n==0  or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# ans=fact(5)
# print(ans)

# def fun(n):
#     if n==0:
#         return
#     else:
#         fun(n-1)
#         print(5*n)
# fun(10)

class node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None
    def bfs(self):
        q =[]
        q.append(self)
        while q:
            a=q.pop(0)
            print(a.data)
            if(a.left):
                q.append(a.left)
            if a.right:
                q.append(a.right)
            
root=node(4)
root.left=node(2)
root.right=node(6)
root.left.left=node(1)
root.left.right=node(3)
root.right.left=node(5)
# print(root.data)
root.bfs()
