# class node:
#     def __init__(self,data) -> None:
#         self.data=data
#         self.next=None
# a=node(1)
# b=node(2)
# a.next=b
# print(a.next)
# print(b)


# class sll:
#     def __init__(self) -> None:
#         self.head=None
#     def insert_at_begining(self,data):
#         if(self.head==None):
#             self.head=node(data)
#         else:
#             new=node(data)
#             new.next=self.head
#             self.head=new
#     def insert_at_end(self,data):
#         if(self.head==None):
#             self.head=node(data)
#         else:
#             i=self.head
#             while(i.next):
#                 i=i.next
#             i.next=node(data)
#     def reverse(self):
#         prev=None
#         curr=self.head
#         nxt=None
#         while(curr):
#             nxt=curr.next
#             curr.next=prev
#             prev=curr
#             curr=nxt
#         self.head=prev

#     def printing(self):
#         if self.head==None:
#             return
#         i=self.head
#         c=0
#         while(i):
            
#             print(i.data,end=" ")
#             c+=1
#             i=i.next 
#         print("length is ",c)
            
            
# l=[1,2,3,4,5]
# o=sll()
# for i in l:
#     o.insert_at_end(i) 
# o.printing()
# o.reverse()
# o.printing()

# class node:
#     def __init__(self,data) -> None:
#         self.data=data
#         self.next=None
# class sll:
#     def __init__(self):
#         self.head=None
#     def insert_at_begining(self,data):
#         if self.head==None:
#             self.head=node(data)
#         else:
#             new=node(data)
#             new.next=self.head
#             self.head=new
#     def insert_at_end(self,data):
#         if self.head==None:
#             self.head=node(data)
#         else:
#             i=self.head 
#             while i.next:
#                 i=i.next
#             i.next=node(data)
#     def printing(self):
#         if self.head==None:
#             return
#         i=self.head
#         while i:
#             print(i.data)
#             i=i.next
#     def lengt(self):
#         if self.head==None:
#             return 
#         else:
#             c=0
#             i=self.head
#             while i:
#                 c+=1
#                 i=i.next
#             print("length is",c)
#     def middle(self):
#         if self.head==None:
#             return
#         else:
#             fast=self.head
#             slow=self.head
#             while fast and fast.next:
#                 slow=slow.next
#                 fast=fast.next.next
#             print("middle element is ",slow.data)

        
# l=[1,2,3,4,5]
# o=sll()
# for i in l:
#     o.insert_at_end(i)
# o.printing()
# o.lengt()
# o.middle()



# 23-04-2024

# class node:
#     def __init__(self,data) -> None:
#         self.data=data
#         self.next=None
#         self.prev=None
# class dll:
#     def __init__(self) -> None:
#         self.head=None
#         self.tail=None
#     def insertatfront(self,data):
#         if self.head==None:
#             self.head=node(data)
#             self.tail=self.head
#         else:
#             new=node(data)
#             new.next=self.head
#             self.head.prev=new
#             self.head=new
#     def insertatend(self,data):
#         if self.head==None:
#             self.head=node(data)
#             self.tail=self.head
#         else:
#             new=node(data)
#             self.tail.next=new
#             new.prev=self.tail
#             self.tail=new
#     def reverse(self):
#         i=self.tail
#         while i:
#             print(i.data)
#             i=i.prev

#     def printing(self):
#         c=0
#         if self.head==None:
#             return 
#         else:
#             i=self.head
#             while i:
#                 print(i.data)
#                 i=i.next
#                 c+=1
#             print("length is ",c)
# l=[1,2,3,4,5]
# o=dll()
# for i in l:
#     o.insertatend(i)
# # o.printing()
# o.reverse()
# # o.printing()
n=3
e=[[0,1],[1,2],[2,0]]
d={i:[] for i in range(n)}
for i,j in e:
    d[i].append(j)
    d[j].append(i)
q=[0]
vis={0}
while q:
    a=q.pop()
    
for i in d[a]:
    if i not in vis:
        q.append(i)
        vis.add(i)
if(a==2):
    print("present")
else:
    print("not present")