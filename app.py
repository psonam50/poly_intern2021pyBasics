# import module
# #<file_name>.<function_name>("Prameter")
# module.add(22,12)
# module.sub(34,3)
import json
import os


# JSON:
class students:
    def __init__(self, name, branch):
        self.name= name
        self.branch=branch
a1 = students("yashika", "CS")
print(a1.name)
a2 = ("neelam", "jyoti")

#json:
#dumps #dump: python to json
#loads #load: json to python

# python object to json object: dumps, python object to json file: dump,
# # json object to python object: loads, json file to python obj: load,  
print(type(a1))
print(type(a2))
obj1Json = json.dumps(a1.__dict__)
print(obj1Json)
print(type(obj1Json))

obj2Json = json.dumps(a2)
print(obj2Json)
print(type(obj2Json))

# obj2Python = json.loads(obj2Json)
# print(type(obj2Python))


# # "read": r, "write": w, "Append": a, "creart": x

# # "t", "b"

# f = open("./new/demo.txt","rt")
# a = f.read()
# print(a)

# f = open("./new/demo.txt","rt")
# print(f.readline())
# f.close()
# # f = open("./new/demo.txt","rt")
# # b = f.readlines()
# # print(b)

# file2 = open("pybasicRead.txt", "wt")
# file2.write("python is very powerfull language")
# file2.close()

if os.path.exists("pybasics.txt"):
    os.remove("pybasics.txt")
else:
    print("file not found")
# opening a file
f = open('object.json')

data = json.load(f)

for i in data['emp_detail']:
    print(i)
f.close()

x= {
            "name": "John",
            "age": 30,
            "married": True,
            "divorced": False,
            "children": ["Ann","Billy"],
            "pets": None,
            "cars": [
              {"model": "BMW 230", "mpg": 27.5},
              {"model": "Ford Edge", "mpg": 24.1}
            ]

          }

d1 = json.dumps(x)
print(d1)

with open('json_data.json','w') as outputFile:
    json.dump(x,outputFile, indent=6)



