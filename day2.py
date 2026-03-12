# # mylist = ["prashant", "Ashish", "komal", "ankush", "Ashish", 77, "sandip", 60.52, "prashant"]

# # print(mylist)
# # print(type(mylist))
# # print(mylist[0])
# # print(mylist[1])
# # print(mylist[2])
# # print(mylist[-1])
# # print(mylist[2:5])
# # print(mylist[:5])
# # print(mylist[1:])
# # print(mylist[1:8:2])
# # print(mylist[:])
# # print(mylist[::-1])

# # mylist.append('harsh')
# # mylist.append("laxman")
# # print(mylist)

# # mylist.insert(1,"sanket")
# # print(mylist)

# # mylist.remove("sandip")
# # print(mylist)

# #  
# # mylist = [["prashant", "jha"], ["85.56"], [440022, "yyy"]]

# # print("example of multidimensional list: ")
# # print(mylist)

# # #print(mylist[row][col])

# # print(mylist[0][0])
# # print(mylist[0][1])
# # print(mylist[1][0])
# # print(mylist[2][0])
# # print(mylist[2][1]) 

# # list1=["prashant", "jha"]
# # print(list1*2)

# # list2=[50,25.50, 'prashant']
# # # print(list1+list2)
# # #del list2[2]
# # # del list2
# # # print(list2)
# # list2.clear()
# # print(list2)

# # name="prashant"
# # print(name)
# # myname=list(name)#typecasting
# # print(myname)

# # mylist=[44,22,77,0,9,88]
# # mylist.sort()
# # print(mylist)
# #default sorting order for number is ascending order
# #default sorting order for string is alphabetical order
# #we should know that list should contain homogenious
# #data otherwise we will get typr error
# #python2 first sort number then sorting follow
# #descending mylist.sort(reverse=true)

# # math=10
# # phy=10
# # print(id(math))
# # print(id(phy))
# #python intrepreter will not create a nw file if it already exist

# # #aliasing
# # mylist=[44,22,77,0,9,88]
# # newlist=mylist
# # print(id(mylist))
# # print(id(newlist))

# #for i in range(1,6) #there are two type of special operaator in python 1.membership(1.in 2. not in) and 2.special
# # name='prashant'
# # print('Z' in name)
# # print('Z' not in name)

# #looping
# # for i in range(6):
# #     print(i)
# # #i=0

# # #looping
# # for i in range(1,10,2):
# #     print(i)
# # #i=0

# # for i in range(5,0, -1):
# #     print(i)

# # for i in range(1,11):
# #     print(i*2)

# # for i in range(1,11):
# #     print([i*2], [i*3], [i*4], [i*5], [i*6], [i*7], [i*8], [i*9], [i*10])
# #     print()

# # for i in range(1,11):
# #     print([i*11], [i*12], [i*13], [i*14], [i*15], [i*16], [i*17], [i*18], [i*19], [i*20])

# #Simple if
# #WAP to accept any digit and check that pos, neg, zero
# #>< are relational operator
# # no=int(input("Enter any digit:"))
# # if no>0:
# #     print('positive')
# # if no<0:
# #     print('negative')
# # if no==0:
# #     print('zero')

# #WAP to accept days and check the working days and weekend
# # days=int(input("Enter any days"))
# # if days==[1,5]:
# #     print('weekdays')
# # if days==[6,7]:
# #     print('weekends')

# # days=input("Enter name of the day:")
# # if days=="SATURDAY" and "SUNDAY" and "saturday" and "sunday":
# #     print('weekend')
# # else:
# #     print('working days')

# # write a program to accept three paper marks and calculate total, percentage and if percentage is grater than equal to 60 then he or she is eligible for placement
# # phy=int(input("Enter marks for 1st subject:"))
# # chem=int(input("Enter marks for 2nd subject:"))
# # maths=int(input("Enter marks for 3rd subject:"))
# # total=phy+chem+maths
# # percentage=(total/3.0)
# # print(total)
# # print(percentage)
# # if percentage>=60:
# #     print("Eligible for placement")
# # else:
# #     print("Not eligible")

# #write a program to accept five different value in 5 different var and check max value and print b y using "simple if statement"
# one=int(input("Enter 1st value:"))
# two=int(input("Enter 2nd value:"))
# three=int(input("Enter 3rd value:"))
# Four=int(input("Enter 4th value:"))
# five=int(input("Enter 5th value:"))

# if one>two and one>two and one>three and one>Four and one>five:
#     print("one is greatest")