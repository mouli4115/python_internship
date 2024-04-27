# height=float(input("enter height"))
# if height>6:
#     print("you are tall")
# elif(height>=4 and height<=6):
#     print("you are average")
# elif(height<4):
#     print("You are dwarf")
# else:
#     print("enter proper vlaue")


# a=int(input("enter number"))
# if(a>0):
#     print("positive")
# elif(a<0):
#     print("negative")
# else:
#     print("zero")



#year=int(input("enter year"))
# if(year%4 == 0):
#     if(year % 100 == 0):
#         if(year % 400 == 0):
#             print("leap year")
#         else:
#             print("not a leap year")
#     else:
#         print("Leap year")        
# else: 
#     print("Not a leap year")

# if(year%4 == 0 and year % 400 == 0):
#  print("leap year")
# elif( year % 4 ==0 and year % 100 !=0):
#  print("leap year")
# else:
#  print("not a leap year")

# if(year%400 == 0 or year % 100!=0):
#     print("leap year")
# else:
#     print("not a leap year")



# sub1=int(input("enter marks of sub1"))
# sub2=int(input("enter marks of sub2"))
# sub3=int(input("enter marks of sub3"))
# sub4=int(input("enter marks of sub4"))
# sub5=int(input("enter marks of sub5"))
# total=sub1+sub2+sub3+sub4+sub5
# print("Marks=",total)
# percentage=(total/500) * 100
# print("Percentage=",percentage)
# if(percentage>75):
#     print("Grade A")
# elif(percentage>=60 and percentage<=74):
#     print("Grade B")
# elif(percentage>=35 and percentage<=59):
#     print("Grade c")
# else:
#     print("fail")


cr=input("Enter an alphabet")
# if (cr=='a'or cr=='e' or cr=='i' or cr=='o' or cr=='u' or cr=='A'or cr=='E' or cr=='I' or cr=='O' or cr=='U'):
#     print("vowel")
# else:
#     print("consonant")
if(cr in 'aeiou' or cr in 'AEIOU'):
    print("vowel")
else:
    print("consonant")

