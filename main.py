

# concat and add
# x = 6
# y= "8"
# print(str(x)+y)
# print(x+int(y))


# # print(q)
# # y is in feet and x is in meter

# def mToF():
#     f = 3.28*m
#     return f
# m = float(input("Enter values in meter: "))
# ValueInFeet=mToF()
# print(ValueInFeet,"Feet")

# # Arguments and prameter

# def mToF(m):
#     f= 3.28*m
#     return f
# F=mToF(12)
# print(F)


# # feet to inch
# # 1 inch = 0.083 feet

# def fToI(f,r):
#     i = 0.083*f+r
#     return i
# x = float(input("enter value in feet:"))
# y=int(input("enter any number:"))
# print(fToI(x,y))


# slicing of a string:
# a = "i am an Engineering Student"
# print(a[8:19])
# print(a[20:])
# print(a[:4])

# E = "Engineering"
# print(E[-4])

# print(E[-4:-2])



# # method: function : a.method()

# #lower
# x= E.lower()

# print(x)
# y = E.upper()
# print(y)

# A = " I am an  Engg student and I am doing study "
# print(len(A))

# # to remove whitespaces we use strip method
# print(len(A.strip()))


# # replace method:
# print(A.replace("Engg student", "software Engineer").replace("study","work").replace("an", "a"))

# # format method:

# A = " I am {1} and I am doing {0} "
# print(A.format("a software engineer","work"))


# # Escape character:
# text= " I am an  \'Engg student\' and I'\
#     am doing\
#          study"
# print(text)


# A = " I am an  Engg student and \bI am doing study "
# print(A)



# print(A.index("Engg"))


# list:
# ordered, # changable, # allow duplicates

# c = ["lohaghat", "almora", "champawat", "haldwani","123","3##45@@", "True"]
# print(len(c))
# print(type(c))
# a = tuple(c)
# print(type(a))

# print(c[1:3])
# print(c[:3])
# print(c[3:])
# print(c[-4:])
# print(c[-6:-3])

# c[-3]="almora"
# print(c)
# c[2:3]= ["delhi", "dehradun"]

# print(c[2])

# c.append("Neeraj")
# print(c)



# from http import client


# list1 = ["delhi", "dehradun"]
# list1[1]="Haldwani"
# print(list1)
# name = "Renu"
# # string[1]="i"
# tuple1 = ("babita", "himani")
# tuple2= list(tuple1)
# tuple2[1]="jyoti"
# print(tuple(tuple2))
# print(name.replace("e","i"))
# list1[0:1]=["Lohaghat","Almora"]
# print(list1)


# # append # insert
# list1.append("champawat")
# print(list1)

# list1.insert(1,"Lucknow")
# print(list1)
# list1.append("Lucknow")
# # to add two list
# list1.extend(tuple2)
# print(list1)


# # remove(), pop()
# list1.remove("Lucknow")
# print(list1)
# #pop: particular index
# list1.pop(2)
# print(list1)
# # pop: to remove last item
# list1.pop()
# print(list1)

# # to delete
# # list1.clear()
# # print(list1)
# # del list1
# # print(list1)

# # for and while


# # for <variable> in <collection>,<string>:
# #     Statement1

# # for i in list1:
# #     print(i)


# # x = 0
# # for i in range(10,101):
    
# #     x+=i
# #     print(x)
# # print("loop is ended")
# y=0
# while y< len(list1):
#     print(list1[y])
#     y=y+1

# #sort
# list1.sort()
# print(list1)
# list1.sort(key=str.lower)
# print(list1) 
# list1.sort(reverse=True, key=str.lower)
# print(list1)


# #replace # format

# # A = "I am learning python and sql which is a useful language"
# # print(A.replace("a","an"))
# # A = "I am learning {1} and {0} which is {2} useful language"
# # print(A.format("HTML","python","very"))


# #tuple:
# t = (1,2,3,4,1,2,"Lohaghat","12num")
# # tuple[1]="renu"


# var1 = (1,2,3)
# #ordered #unchangeable *() # allow duplicate

# # we will convert it to list
# a = list(t)
# a.append("champawat")
# t=tuple(a)
# print(t)
# x=10
# for x in t:

#     if str(x).isdigit():
#         print(x,"is a number")
#     elif x.isalpha():
#         print(x, "is alpha")
#     elif x.isalnum():
#         print(x, "is alphanum")
# print("end")

# # dictionary:
# # key value pair:

# clientInfo = {
#     "name": "Sohan",
#     "project": "flask",
#     "time": "20 Days",
    
# }

# print((clientInfo["project"]))

# print(clientInfo.keys())
# clientInfo["project"] = "React"

# clientInfo.update({"time":"1 month"})
# clientInfo["price"]= 20000


# clientInfo.pop("price")
# print(clientInfo)


# #class:
# # all object # properties # methods

class Student:
    def __init__(self,name,standard, age ):
        self.name = name
        self.standard = standard
        self.age = age
x1 = Student("Sohan", "IT",20)
x2 = Student("Bhaskar", "CS", 20)
print(x1.standard)


# Scope
#LEGB rule: LOcal, 

x =3
def add():
    
    y = 4
    z=x+y
    return z
print(add())
a = x+2
print(a)

print("HEllo World")
print("python")