# class Solution:
#     def runningSum(self, nums: list[int]) -> list[int]:
#         l=[]
#         x=nums[0]
#         l.append(x)
#         j=1
#         while(j<len(nums)):
#             x=x+nums[j]
#             l.append(x)
#             j+=1
#         return l

# class Solution:
#     def reverse(self, x: int) -> int:
#         if(x<0):
#             x=-(x)
#             rem=0
#             rev=0
#             while(x!=0):
#                 rem=rem%10
#                 rev=rev*10+rem
#                 x=x//10
#             return -(rev)
#         elif(x>0):
#             rem=0
#             rev=0
#             while(x!=0):
#                 rem=rem%10
#                 rev=rev*10+rem
#                 x=x//10
#             return (rev)

        

# x=-123
# x=-(x)
# print(x)
# rem=0
# rev=0
# while(x!=0):
#     rem=x%10
#     rev=rev*10+rem
#     x=x//10
# print(-(rev))

# raise ValueError("hgfhgfghf")/

# class Solution: #520
#     def detectCapitalUse(self, word: str) -> bool:
#         new_word=list(word)
#         count=0
#         cou=0
#         c=len(new_word)
#         if(c>0):
#             res=False
#             res=all(ele==new_word[0] for ele in new_word)
#             if(res):
#                 return True
#         if(c!=1):
#             for i in range(len(new_word)):
#                 if new_word[i].isupper():
#                     count+=1
#                 if new_word[i].islower():
#                     cou+=1
#             if(count==c):
#                 return True
#             elif(cou==c):
#                 return True
#             elif(new_word[0].isupper() and count==1):
#                 return True
#             else:
#                 return False
#         else:
#             return True
        

# strs=["flower","flow","flight"]
# for i in range(len(strs)):
#     str[i+1]=strs[i]

# c=min(len(str))
# print(c)
# l=""
# for i in range(c):
#     if(str1[i]==str2[i]==str3[i]):

#         l=l+str1[i]
# print(l)



# s='ABFCACDB'
# l=[]
# print(ord(s[0]))
# if(ord(s[0])==65 and ord(s[0])==67):
# for i in range(len(s)):
#     if(len(s)==0):
#         l.append(s[i])
#     elif(ord(s[0])==65 and ord(s[0])==67):
#         l.pop()
#     elif(ord(s[0])==68 and ord(s[0])==69):
#         l.pop()
#     else:
#         l.append(s[i])

# s=''
# c=0
# for i in range(len(s)):
#     if(s[i]=='('):
#         c+=1
#     elif(s[i]==')'):
#         c+=-1
#     elif(s[i]=='{'):
#         c+=2
#     elif(s[i]=='}'):
#         c+=-2
#     elif(s[i]=='['):
#         c+=3
#     elif(s[i]==']'):
#         c+=-3
    
# if(c==0):
#     print("true ")



# s = "A man, a plan, a canal: Panama" 
# a=''
# for i in s:
#     if(i.isalnum()):
#         a=a+i
# a=a.lower()
# b=a[::-1]
# print(b)
# print(a)    
# if(a==b):
#     print("correct")

# head=[1,2,2,1]
# s=''
# while(p):
#     s+=str(p)
#     p=p.next
# print(s)

# arr=[1,2,3,2,0]
# j=len(arr)-1
# flag=0
# p=max(arr)
# peak=arr.index(p)
# print(peak)
# i=0
# while i<peak:    
#     if(arr[i]==arr[i+1]):
#         break
#     if(arr[i+1]>arr[i]):
#         flag=1
#     else:
#         flag=0
#         break
#     i+=1

# while j>peak:
#     if(arr[j]==arr[j+1]):
#         break
#     if(arr[j+1]<arr[j] and flag==1):
#         flag=1
#     else:
#         flag=0
#         break
#     j+=1
# if(flag==1):
#     print("mountain")
# else:
#     print("not a mountain")

# n=3
# p=(bin(n))
# c=0
# i=0
# print(p)
# for i in p:
#     if(i=='1'):
#         c+=1
    
# print(c)

# a=[1,2,3,1]
# b=set(a)
# print(b)
# if len(b)<len(a):
#     print("true ")

# nums=[1,2,1]
# nums1=[]
# nums1=(nums)
# print(nums1)
# s='abcd'
# t='abcde'
# print(s xor t)


print(chr(65))