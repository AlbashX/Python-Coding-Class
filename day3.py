# Nested IF-Else
# if condition-1:
#     if condition-2:
#         #statement
#     else:
#         #statement
# else:
#     if condition-2:
#         #statement
#     else:
#         #statement

#WAP to accept 3 papeer marks and check max marks using nested if else
# phy=int(input("Enter marks for 1st subject:"))
# chem=int(input("Enter marks for 2nd subjec:"))
# maths=int(input("Enter marks for 3rd subject:"))
# if phy>chem:
#     if phy>maths:
#         phy is max
#     else:
#         print("maths is max")
# else:
#     if chem>maths:
#         print("chem is max")
#     else:
#         print("maths is max")

# phy=int(input("Enter marks for 1st subject:"))
# chem=int(input("Enter marks for 2nd subjec:"))
# maths=int(input("Enter marks for 3rd subject:"))
# if phy<chem:
#     if phy<maths:
#         print("phy is lesser")
#     else:
#         print("maths is lesser")
# else:
#     if chem<maths:
#         print("chem is lesser")
#     else:
#         print("maths is lesser")


#Else if
# if condition:
#     statement
# elif condition:
#     statement
# elif condition:
#     statement
# else:
#     default block
# Write a program to accept percentage>90 grade-A, percentage>80 grade-B, per>60 grade C, per<60 grade Fail
# phy=int(input("Enter marks for 1st subject:"))
# chem=int(input("Enter marks for 2nd subjec:"))
# maths=int(input("Enter marks for 3rd subject:"))
# total=phy+chem+maths
# percentage=(total/3.0)
# print(total)
# print(percentage)
# if percentage>=90:
#     print("Grade A")
# elif percentage>=80 and percentage<90:
#     print("Grade B")
# elif percentage>=60 and percentage<80:
#     print("Grade C")
# else:
#     print("Fail")


#Dictionary
# mydict={
#     "name": "albash",
#     "professional": "cricketer",
#     "empid":1001
# }
# print(mydict)
# print(type(mydict))

# mydict={
#     101: "albash",
#     102:"ashish",
#     "103": "mohini",
#     "104":"trivani",
#     101:"ashish",
#     104:"ashish"
# }
#print(mydict)

#with the help of key we have to print values
# a=mydict[102]
# print(a)

#We will replace the old value with new value
# mydict[102]="peter"
# print(mydict)

#only print key=0,1
# for x in mydict:
#     print(x)

#only print values
# for x in mydict.values():
#     print(x)

# Printing key and values both
# for x,y in mydict.items():
#     print(x,y)

#if i have to add new key and value pair in my dictionary
# mydict["mobile_no"]=463287349478
# print(mydict)

#imp: if we want to replace to represent binary dataike images 
# mydict.pop(101)
# print(mydict)
#most of the que are based on List, string and dictionary


#Slicing
#name="prashantjha"
#indexing=012345678910
# print(name[0])
# print(name[1])
# print(name[-1])
# #print(name[15])
# print(name[0:5])
# print(name[1:])
# print(name[:5])
# print(name[:])
# print(name[1:8:2])
# print(name[::-1])


#Find function
# s="help4code is a best platform for practicing programming"
# print(s.find("help4code"))
# print(s.find("python"))  #python not found o/p=0
# print(s.find("programming"))


#join function
# s="prashant", "ashish", "sandip"
# m='*'.join(s)
# print(m)


# s="Python is a high level Programming language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())


#dot format function
# print('Sunject Marks:')
# phy=50
# chem=60
# math=70
# print("physics={} chemistry={} Math={} ".format(phy,chem,math))
# print("physics={0} chemistry={1} Math={2} ".format(phy,chem,math))
# print("physics={x} chemistry={y} Math={z} ".format(x=phy,y=chem,z=math))
# total=phy+chem+math
# print("Total Marks",f"{total} ")
# print("Roll No=","7".zfill(4))


# print('prashantjha777'.isalnum())  # True
# print('prashantjha'.isalpha())     # True
# print('777f'.isdigit())
# print('sfgdsdsd'.islower())
# print(''.islower())
# print('PRASHANT'.isupper())
# print('My Name Is Prashant'.istitle())
# print(''.istitle())
# print(' '.isspace())
# print('Hello'.startswith("He"))
# print('Hello'.endswith("lo"))


#BODMAS
# a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d) #160
# print((a-b)*(c/d)) #40
# print(a+(b*c)/d) #110


# x=['A', 'B', 'C']
# y=['A', 'B', 'C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x!=z)


name="prashant"
data=['a', 'e', 'i', 'o', 'u',]
vowels=0
con=0
for i in name:
    if i in data:
        vowels +=1
    else:
        con +=1
    print("vowels=", vowels)
    print("consonent", con)
    

