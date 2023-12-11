# data types:-

# 1. numericals:-(integers,float,complex)

# integers:-

# a = 2000
# print(a,type(a))

# b = 2164
# print(b,type(b))

# c = 1428
# print(c,type(c))


# float:-

# a = 25.24
# print(a,type(a))

# b = 136.00
# print(b,type(b))

# c = 96.15
# print(c,type(c))

# complex:-

# a = 2000j
# print(a,type(a))

# b = complex(50,20)
# print(b,type(b))

# c = complex(52,65)
# print(c,type(c))
# print(c.real)
# print(c.imag)

# ----------------------------------------------------------

# 2. sequence:-

# string:-

# a = "today is the profitable day"
# print(a,type(a))

# b = 'learn and grow'
# print(b,type(b))

# c = '''name
# email
# course
# collage
# year'''
# print(c,type(c))

# a = "name%@$_2000"
# print(a,type(a))


# list:- (homogenious and hetrogenious)

# a = [10,20,30,40,50]
# print(a,type(a))

# b = [15,86,45,"python",153]
# print(b,type(b))

# c = [9,8,7,6,5,4,3,2,1]
# print(c,type(c))


# Tuple:- (homogenious and hetrogenious)

# a = ("pythonB10",2023)
# print(a,type(a))

# b = ("python","java","data science",2023)
# print(b,type(b))

# c = (2000,"pythonB10",256.255,12j)
# print(c,type(c))


# set:-( homogenious & hetrogenious)
    #  (duplicates number are not allowed)

#  a = {1,2,3,4,5,6}
# print(a,type(a))

# b ={"class",12,52,96}
# print(b,type(b))

# c = {25,85,44,85,651}
# print(c,type(c))


# frozenset:-( homogenious & hetrogenious)
    #        (duplicates number are not allowed)

# a = frozenset({"rohit",14052000})
# print(a,type(a))

# b = frozenset({"ice","water",90})
# print(b,type(b))

# c = frozenset({9,8,7,6,5,4,3,2,1,0})
# print(c,type(c))


# range:-

# a = range(1,100)
# print(a,type(a))

# b = range(1000)
# print(b,type(b))

# ----------------------------------------------------

# 3.mapping:-

# dictionary:- (duplicate key are not allowed)

# a = {"name":"rohit","PRN":2021321612042}
# print(a,type(a))

# b = {"math":18,"sci":19,"history":20}
# print(b,type(b))

# c = {"apple":"red","mango":"yellow","orange":"orange"}
# print(c,type(c))

# -----------------------------------------------------

# 4.bool:-

# True:-

# a = (True)
# print(a,type(a))


# false:-

# b = (False)
# print(b,type(b))

# ----------------------------------------------------

# 5.None:-

# a = None
# print(a,type(a))

# --------------------------------------------------

# 6.indexing:-

# positive indexing :- (+)

# a = "regular exercise it can make you feel happier"
# print(a[0:10:1])

# b = (10,20,30,40,50,60)
# print(b[0:5:1])

# c = [10,20,30,40,50,60,70,80]
# print(c[3:8:1])


# Negative indexing:-

# a = "jawahar lal nehru engineering collage aurangabad"
# print(a[-1:29:-1])

# b = [9,8,7,6,5,4,3,2,1,0]
# print(b[-1:3:-1])

# c = [1,2,3,4,5,6,7,8,9]
# print(c[-1:-10:-1])

# -----------------------------------------------------

# built if function:-

# 1. id:-

# a = "pythonB10"
# print(id(a))

# b = [10,20,30,40,50]
# print(id(b))

# c = {10,20,30,40,50}
# print(id(c))

# 2.Type:-

# a = "aurangabad"
# print(type(a))

# b = [10,20,30]
# print(type(b))

# c = {"name":"jnec"}
# print(type(c))


# 3.length:-

# a = [1,2,3,4,5,6,7,8,9]
# print(len(a))

# b = "python is a simple language as compare to other language"
# print(type(b))

# c = ("rohit",1254,14.28,[12.21],{"python"})
# print(len(c))


# --------------------------------------------------------

#                         operators:-

# 1.arthmatic operator:-

# additional operator:-

# a = 258 + 369
# print(a)


# multipication operator:-

# a = 258 * 852
# print(a)

# subtraction operator:-

# a = 9589 - 8546
# print(a)


# divison operator:-

# a = 256 / 123
# print(a)
               #  answer without float

# b = 640 // 81
# print(b)



# power operator:- 

# a = 100 ** 2
# print(a)

# ---------------------------------------------------

# 2. relation comparison operator:- (< , > , <= , >=)

# less than :-(<)

# a = 500
# b = 200
# c = b < a
# print(c)


# greater than:- ( >)

# a = 100
# b = 50
# c = a > b
# print(c)


# less than equal to :- (<=)

# a = 10
# b = 20
# print(a <= b)

# greater than equal to:-(>=)

# a = 100
# b = 50
# print(a >= b)

# ---------------------------------------------------


# 3. special operator:-

# membership:-(in, not in)

# in:-

# a = "math,science,marathi,hostory"
# a2 = "math,science,marathi,hostory"
# print(a in a2)


# b = "python,java,data science"
# b2 = "python,java,data science"
# print("python " in b2)


# c = [10,20,30,40,50]
# c2 = [10,20,30,40,50]
# print(60 in c2)


# not in:-

# a = "rohit,suraj,kiran,ayush"
# a2 = "saurabh,pratik,vinay,raj"
# print(a not in a2)


# b = [1,2,3,4,5]
# b2 = [9,8,7,4,5]
# print(b2 not in b)


# c = [10,20,30,40]
# c2 = [10,20,30,40]
# print(10 not in c2)


# 4. identity operator:-(is,is not)

# is:-

# a = "jawahar lal nehru engineering collage aurangabad"
# b = "baliram patil vidhyalaya"
# print(id(a),id(b))
# print(a is b)


# a = "Your attitude is critical to success"
# b = "Your attitude is critical to success"
# print(a is b)


# is not:-

# a = [10,20,30,40,50,60]
# b = [10,20,30,40,50,60]
# print(a is not b)
# print(id(a),id(b))


# a = [1,2,3,4,5,6]
# b = [1,2,3,4,5,6]
# print("rohit" is not b)

# ----------------------------------------------------

# 5.equility operator:-

# equal to:- (==)

# a = 30
# b = 30
# print(a == b)

# not equal to:-(!=)

# a = 100
# b = 500
# print(a != b)

# ----------------------------------------------------

# 6.logical:- (and , or , not)

# and type:-(always looks for false)

# a = 500
# b = 400
# if a > b and b < a:
#     print("true")
# else:
#     print("false")


# a = 100
# b = 200
# c = 300
# if a != b and a + b == c:
#     print("true")
# else:
    # print("false")


# a = 10
# b = 20
# c = 30
# d = 40
# if a != b and a + c == d and a + b == c:
#     print("true")
# else:
#     print("false")

# -----------------------------------------------------


# OR type:-(always looks for true)

# a = 100
# b = 150 
# c = 250
# if a + b == c or type(a) == str:
#     print("true")
# else:
#     print("false")

# a = 1000
# b = 2000
# c = 3000
# d = 6000
# if a + b == c or b - c != a:
#     print("true")
# else:
#     print("false") 


# a = 10
# b = 20
# c = 30
# if a == 10 or a + b == c or type(c) == int:
#     print("true")
# else:
#     print("false")

# ------------------------------------------------------

# not type:-

# a = 50
# b = 60
# if a != b:
#     print("true")
# else:
#     print("false")


# a = 100
# b = 200
# if a == 100:
#     print("true")
# else:
#     print("false")

# ---------------------------------------------------------

# slice operator:-

# a = 10 + 25j
# print(a.real)
# print(a.imag)

# b = complex(50,100)
# print(b)
# print(b.real)
# print(b.imag)

# c = 25j
# print(c.real)
# print(c.imag)

# ----------------------------------------------------

# type conversion:-

# str to int:- (only single number taken)

# a = "2000"
# print(type(a))

# b = int(a)
# print(type(b))


# a = "rohit"
# print(type(a))

# b = set(a)
# print(type(b))


# a = (10,20,30)
# print(type(a))

# b = list(a)
# print(type(b))


# a = {"python,java"}
# print(type(a))

# b= str(a)
# print(type(b))


# a = {1,2,3,4,5,6}
# print(type(a))

# b = tuple(a)
# print(type(b))

# --------------------------------------------------


# empty:-

# a = list()
# print(a)


# b = set()
# print(b)


# c = dict()
# print(c)


# d = tuple()
# print(d)

# ------------------------------------------------------


# bool:- (true of false depends on value)

# a = bool(0)
# print(a)

# b = bool(125)
# print(b)

# c = bool(0.00)
# print(c)


#       (true false depends on data types)


# a = bool ([""])
# print(a)

# b = bool ([])
# print(b)

# c = bool(["rohit"])
# print(c)

# d = bool([500])
# print(d)

# --------------------------------------------------------

# ternary operator:-

# a = 1565
# b = 5161
# c = 3161
# minimum = a if a < b and a < c else b if b < a and b < c else c
# print(minimum)


# a = 100
# b = 500
# c = 1000
# maximum  = a if a > b and b > c else b if b < a and b > c else c
# print(maximum)


# a = 245
# b = 25465
# c = 5422
# d = 56516
# minimum = a if a < b and a < c and a < d else b if b < a and b < c and b < d else c if c < a and c < b and c < d else d
# maximum = a if a > b and a > c and a > d else b if b > a and b > c and b > d else c if c > a and c > b and c > d else d
# print(maximum)
# print(minimum)


# -------------------------------------------------------------

# import math

# pi :- 
# import math
# print(math.pi)

# sqrt:-

# import math
# print(math.sqrt(1000))


# factorial:-

# import math
# print(math.factorial(20))

# ceil:-

# import math
# print(math.ceil(15/8))

# ---------------------------------------------------------

# input and output:- 

# a = (input("enter the name:-"))
# b = (input("enter the surname:-"))
# print(a + " " + b)


# for int:- (only intergers can take)

# a = int(input("enter the firsst number:-"))
# b = int(input("enter the second number:-"))
# print(a + b)


# for eval:-

# a = eval(input("enter the first number:-"))
# b = eval(input("enter the second number:-"))
# print(a - b)

# -----------------------------------------------------
# summation:- 

# num1 = 654
# num2 = 216
# print(f"summation of {num1} and {num2} is {num1/num2}")

# a = "rohit"
# b = "gaikwad"
# print(f"summation of {a} and {b} is {a+b}")

# ---------------------------------------------------------

# a = 10
# b = 50.20
# c = "python"
# print("the value of a is %i"%a)
# print("the value of b is %f"%b)
# print("the value of c is %s"%c)

                                        #OR#

# a = 10
# b = 12.05
# c ="rohit"
# print("the value of a is:",a)
# print("the value of b is:",b)
# print("the value of c is:",c)

# ---------------------------------------------------









