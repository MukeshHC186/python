# x,y,z="hello",3,5
# print(x)
# print(y)
# print(z)

# x=y=z="hello"
# print(x)
# print(y)
# print(z)

# myList=["one","two","three"]
# print(myList[0])
# print(myList[1])
# print(myList[2])
# print(myList[-1])
# print(myList[-2])
# print(myList[-3])
# x,y,z=myList
# print(x)
# print(type(x))

# fruits=["appla","banana","cherry"]
# x,y,z=fruits
# print(x)
# print(y)
# print(z)
# --------------last item print-----------------
# print(fruits[-1])  # last print

#******************function**************
# x=20
# def myFunction():
#     print("Hello, World!"+str(x))
# myFunction()

# age=20
# def myFunction():
#     print("This is my age "+str(age))
# myFunction()
#************local & globel variables************
# age=20
# def myFunction():
#     age=10
#     print("This is my age "+str(age))
# myFunction()
# print(age)

# ************global keyword**************
age=20
def myFunction():
    global age
    age=10
    print("This is my age "+str(age))
myFunction()
print(age)

#***********lambda function**************
x=lambda a,b:a+b
print(x(5,7))
# ***********map function**************
numbers=[1,2,3,4,5]
squares=list(map(lambda x:x**2,numbers))
print(squares)









