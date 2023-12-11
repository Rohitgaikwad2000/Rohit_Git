# identifiers and rule:-

# 1.no numbers
# 2.can not start with numbers.
# 3.special characterstics are not allowed.
# 4.meanining full Name
# 5.can not use reserved keyword
# 6.no limitation.

# -----------------------------------------------------------

# data types:-  (there are 14 data types:-)

# numerical:- (integers, float, complex)

# integers:-

# a = 100
# print(a,type(a))

# float:-

# a = 14.26
# print(a,type(a))

# complex:-

# a = 262j
# print(a,type(a))


# sequence:- (list, tuple, set, range, string, bytes, bytearray, frozonset)

# list:-

# a = [10,20,30,40,50,60]
# print(a,type(a))


# tuple:-

# a = ("python","java","c++",2023)
# print(a,type(a))


# set:-

# a = {10,20,30,"rohit"}
# print(a,type(a))


# frozenset:--( homogenious & hetrogenious)
    #        (duplicates number are not allowed)

# a = frozenset({"black","white","yellow"})
# print(a,type(a))


# range:-

# a = range(1,10)
# print(a,type(a))


# string:-

# a = "what happened when if you use oil as compared to fuel"
# print(a,type(a))


# bytearray:--

# a = bytearray()
# print(a,type(a))



# bytes:-



# -----------------------------------------------------------------------------------


# mapping:- (duplicate key are not allowed)

# a = {"name":"rohit","age":23,"collage":"JNEC"}
# print(a,type(a))


# -----------------------------------------------------------------------------------------

# None:-

# a = None
# print(a,type(a))


# --------------------------------------------------------------------------

# bool:-

# a = (False)
# print(a,type(a))


# b = (True)
# print(a,type(a))


# --------------------------------------------------------------------


# built in methods:-

# 1.string feature:-

# allow duplicates
# immutable elemnts 
# support slicing
# no index based operation(+ve,-ve)
# homogenious and hetrogenious


# str strip:-

# a = "      Time is a finite resource, and in the realm of economics,it is directly equated with money    "
# print(a.strip())

# Rstrip:-

# a = "        Time also plays a pivotal role in technological advancements and societal progress."
# print(a.strip())

# Lstrip:-

# a = "Time, in this context, is not merely a concept but a quantifiable unit of production.              "
# print(a,type(a))


#  str split:-

# a = "Time is money"
# print(a.split())


# split with(",")

# a = "Once it is lost, it is lost forever and can never be regained."
# print(a.split(","))


# str find:-

# a = "The statement Time is money is an equating statement"
# print(a.find("Time"))


# count:-

# a = "Time is money means time is priceless and precious"
# print(a.count("is"))


# str join:-

# a = "mechanical engineering"
# a2 = a.split()
# print(" ".join(a2))


#  replace:-

# a = "python is simple and easy to learn"
# print(a.replace("python","java"))


# str upper:- 

# a = "java is simple and easy to learn".upper()
# print(a)

# str lower:-

# a = "PYTHON IS SIMPLE AND EASY TO LEARN".lower()
# print(a)

# str isalnum:-(alpha,numeric)

# a = "gaikwadrohit1428gmailcom"
# print(a.isalnum())


# str isalpha:-

# a = "Wealletimitedamountoftimeinurlives"
# print(a.isalpha())


# str title:-

# a = "We all get limited amount of time in our lives."
# print(a.title())

# str capatalize:-

# a = "we all get limited amount of time in our lives."
# print(a.capitalize())


#str endswith:- (end starts letter)

# a = "jawahar lal engineering collage aurangabad"
# print(a.endswith("d"))


#str isnumeric:-

# a = "7972671900"
# print(a.isnumeric())


#str isspace:-

# a = "      "
# print(a.isspace())

#str index:-

# a = "PYTHON IS SIMPLE AND EASY TO LEARN"
# print(a.index("AND"))


#str rindex:- (checking with the right side)

# a = "PYTHON IS SIMPLE AND EASY TO LEARN"
# print(a.rindex("TO"))




# 2. string:-


# str rindex:-

# a = "Your attitude is critical Yo success"
# print(a.rindex("Y"))

# str index:-

# a = "We all get limited amount of time in our lives."
# print(a.index("time"))

# str isspace:-

# a = "    "
# print(a.isspace())


# str isnumeric:-

# a = "7020754005"
# print(a.isnumeric())

# str enswith:-

# a = "We all get limited amount of time in our lives."
# print(a.endswith("."))


# str capatlize:-

# a = "we all get limited amount of time in our lives."
# print(a.capitalize())


# str title:-

# a = "Time is the most precious thing in the world."
# print(a.title())

# str isalpha:-

# a = "rohitgaikwad"
# print(a.isalpha())


# str strip:-

# a = "         jawahar lal nehru engineering collage aurangabad        "
# print(a.strip())

# Rside strip:-

# a = "    Time is the most precious thing in the world."
# print(a.rstrip())

# Lside strip:-

# a = "It is clear by now that time is more valuable than money      "
# print(a.lstrip())


# str find:-

# a = "It is clear by now that time is more valuable than money."
# print(a.find("more"))


# str count:-

# a = "To sum it up, time it definitely more important than money"
# print(a.count("it"))


# str join:-

# a = "To sum it up, time is definitely more important than money"
# a2 = a.split()
# print(" ".join(a2))


# str replace:-

# a = "Time is the most significant factor in life"
# print(a.replace("Time","money"))


# str upper:-

# a = "Time is the most significant factor in life".upper()
# print(a)

# str lower:-

# a = "TIME IS THE MOST SIGNIFICANT FACTOR IN LIFE"
# print(a.lower())


# str isalnum:-

# a = "rohitgaikwad2000"
# print(a.isalnum())





# 3. string:-

# str strip:-

# a = "       TIME IS THE MOST SIGNIFICANT FACTOR IN LIFE"
# print(a.strip())


# str isalnum:-

# a = "python2023"
# print(a.isalnum())


# str split:-

# a = "Time is very precious"
# print(a.split())


# str title:-


# a = "Your time is limited, so don't waste it living someone else's life"
# print(a.title())

# str find:-

# a = "Time is money, this saying is very true and important."
# print(a.find("money"))


# str capitalize:-


# a = "time is money, this saying is very true and important."
# print(a.capitalize())

# str count:-

# a = "Time is among the very few things that once lost can never be recovered."
# print(a.count("lost"))


# str endswith:-

# a = "Time is among the very few things that once lost can never be recovered."
# print(a.endswith("."))


# str join:-

# a = "Think of a positive thought to manage your stress instead of a negative one."
# a2 = a.split()
# print("".join(a2))


# str replace:-

# a = "today is a friday"
# print(a.replace("friday","saturday"))


# str isnumeric:-

# a = "64611666646"
# print(a.isnumeric())


# str upper:-

# a = "Think of a positive thought to manage your stress instead of a negative one.".upper()
# print(a)

# str lower:-

# a = "THINK OF A POSITIVE THOUGHT TO MANAGE YOUR STRESS INSTEAD OF A NEGATIVE ONE.".lower()
# print(a)


# str isspace:-

# a = "        "
# print(a.isspace())


# str index:-

# a = "mango, apple, banana, orange"
# print(a.index("orange"))


# str isalnum:-

# a = "python6461java"
# print(a.isalnum())


# str rindex:-

# a = "THINK OF A POSITIVE THOUGHT TO MANAGE YOUR STRESS INSTEAD OF A NEGATIVE ONE."
# print(a.rindex("NEGATIVE"))


# ----------------------------------------------------------------------------------------------------------------------


# 2.1 list:-

# list festure:-

# allow duplicates
# only  mutable and immutable elemnts 
# support slicing
# no index based operation(+ve,-ve)
# homogenious and hetrogenious


# list count:-

# a = ["time is money", 30, 10, 20, 30,[31564]]
# print(a.count(30))


# lst index:-

# a = [5,33,323,233,33,33,6,466,665,313]
# print(a.index(6))


# lst append:-

# a = ["math","science","history"]
# a.append("python")
# print(a)


# lst extend:-

# a = ["math","science","history"]
# a.extend("java,python,2000")
# print(a)


# lst remove:-

# a = ["black","white","orange",546,646,6161]
# a.remove("orange")
# print(a)


# lst pop:-

# a = [511,311,311,6461,33]
# print(a.pop())


# lst reverse:-

# a = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# a.reverse()
# print(a)

# lst sort:-

# a = [4646,46313,43131,6313,464,34643,4643]
# a.sort()
# print(a)

# for decnding sort:-

# a = [4646,46313,43131,6313,464,34643,4643]  
# a.sort(reverse=True)
# print(a)                    






# (decending order)

                                                      
# lst alising:-  (id is same)

# a = [10,20,30,40,50]
# a2 = a
# a2.append(2000)
# print(a,a2)


# lst clear:-

# a = ["saurabh","vinay",[10,20,30],"completed"]
# a.clear()
# print(a)


# lst insert:- (insert the value then lst is extend)

# a = ["rohit","vinay","saurbh"]
# a.insert(0,"pratik")
# print(a)


# lst cloning:-

# a = [10,20,30,40,50]
# a2 = a.copy()
# a2.append(2000)
# print(a,a2)
# print(id(a),id(a2))


# lst deepcopy:-

# import copy
# a = [10,20,30,40,50,[31,46,616]]
# a2 = copy.deepcopy(a)
# a2[5][2] = 6000
# print(a,a2)
# print(id(a),id(a2))




# 2.2 list:-


# list clear:-

# a = [10, 20, 30, 40, 50, "python"]
# a.clear()
# print(a)


# lst alising:-

# a = [1,2,3,6,5,4]
# a2 = a 
# a.append("rohit")
# print(a,a2)
# print(id(a),id(a2))



# list sort:-

# a = [566,16465,651515,111531,3153]
# a.sort()
# print(a)

# decending sort:-

# a = [566,16465,651515,111531,3153]
# a.sort(reverse=True)
# print(a)



# lst reverse:-

# a = ["mechanical","civil","electrical","csit"]
# a.reverse()
# print(a)


# lst pop:- (pop with index)


# a = [12,45,78,89,56,23]
# a.pop(3)
# print(a)


# lst remove:-

# a = ["aurangabad","pune","mumbai","nashik","jalna",[10,20,30]]
# a.remove("pune")
# print(a)


# lst extend:-

# a = ["aurangabad","pune","mumbai","nashik"]
# a.extend("jalna, 2000")
# print(a)


# lst append:-

# a = [100, 200, 300, 400, 500]
# a.append("131313,1511313,43131")
# print(a)


# lst index:-

# a = [100, 200, 300, 400, 500]
# print(a.index(300))


# lst count:-

# a = [1, 5, 4, 5, 1, 5, 1, 2, 3, 6, 5, 2, 2, 3, 2, 1, 5]
# print(a.count(5))


# lst insert:-

# a = ["aurangabad","pune","mumbai","nashik"]
# a.insert(2,"jalna")
# print(a)


# lst clonong:-

# a = [11,66,498,16,64,64,31]
# a2 = a.copy()
# a.append(7976)
# print(a,a2)
# print(id(a),id(a2))


# lst deepcopy:-

# import copy
# a = [11,66,498,16,64,64,31]
# a2 = copy.deepcopy(a)
# a2[5] = 2000
# print(a,a2)
# print(id(a),id(a2))



# 1.3 list:-


# lst count:-


# a = [10, 52, 41, 12, 510, 2, 64, 10]
# print(a.count(10))


# lst clear:-

# a = ["aurangabad","pune","mumbai","nashik"]
# a.clear()
# print(a)


# lst index:-


# a = ["aurangabad","pune","mumbai","nashik","jalna",[10,20,30]]
# print(a.index("mumbai"))



# lst alising:-


# a = [12,85,62,42,623]
# a2 = a
# a2.append(2000)
# print(a,a2)
# print(id(a),id(a2))


# lst append:-

# a = ["math","science","hindi","history"]
# a.append("marathi,2000")
# print(a)


# lst sort:-

# a = [12,94,6,56,849,313,546,132,646,899,313]
# a.sort()
# print(a)


# decending order:-

# a = [12,94,6,56,849,313,546,132,646,899,313]
# a.sort(reverse=True)
# print(a)


# lst extend:-

# a = ["mango","orange","apple"]
# a.extend("watermelon,python,2023")
# print(a)


# lst reverse:-

# a = ["math","science","hindi","history"]
# a.reverse()
# print(a)


# lst remove:-

# a = [12,94,6,56,849,313,546,132,646,899,313]
# a.remove(546)
# print(a)


# lst pop:-

# a = ["bollywood","hollywood","tollywood"]
# a.pop(0)
# print(a)


# lst insert:-

# a = [90, 80, 70, 60, 50, 40, 30, 20, 10]
# a.insert(4,2000)
# print(a)


# lst cloninig:-

# import copy
# a = [10,20,30,[60,50,40]]
# a2 = copy.deepcopy(a)
# a2[3][1] = 500
# print(a,a2)
# print(id(a),id(a2))


# -----------------------------------------------------------------------------------------------------------------------


# 3.1 tuple feature:-


# allow duplicates elements
# mutable and immutable elemnts 
# support slicing
# no index based operation(+ve,-ve)
# homogenious and hetrogenious


# tuple count:- 



# a = ("Python is an easy to learn, powerful programming language.")
# print(a.count("easy"))


# tuple index:-

# a = (589,655,"python","java","powerful programming language")
# print(a.index("java"))


# tuple max:-


# a = (46, 61, 98, 63, 12, 45, 74, 23)
# print(max(a))


# tuple min:-

# a = (125,896,745,852,123,654,789)
# print(min(a))



# 3.2 tuple:-

# tuple index:-

# a = ("Python is a simple, general purpose, high level, and object-oriented programming language.")
# print(a.index("high level"))


# tuple count:-

# a = (10, 20, 30, 40, 50, 20, 10, 30, 60, 50, 40, 20, 10)
# print(a.count(10))



# tuple max & min:-

# a = (852,654,789,321,459,687,125,968)

# print(max(a))
# print(min(a))



# 3.3 tuple:- 


# tuple index:- 

# a = ("python","java","c++",2023,2000,5896,[10,20,30])
# print(a.index(2000))


# tuple count:-


# a = ("This Python Tutorial helps you learn Python programming from scratch.")
# print(a.count("y"))


# tuple max and min:-

# a = (25645,87956,12365,87459,63254,12589)

# print(min(a))
# print(max(a))


# --------------------------------------------------------------------------------------------------------------------

# 4.1 set:-

# does not allow duplicates
# does not preserve insetion order
# only allow immutable elemnts (if mutable element is use then unhashable error)
# no slicing
# no index based operation
# mathmatical operstions
# homogenious and hetrogenious


# set:- 

# set add:-

# a = {"python","java","c++",(10,20,30)}
# a.add("mechanical, civil, (2000,2023)")
# print(a)


# set update:-

# a = {"bollywood","hollywood","tollywood"}
# a.update("salman, tom cruise, vijay thalaypati")
# print(a)

# set copy:-

# a = {"This Python tutorial is well-suited for beginners as well as professionals"}
# print(a.copy())


# set pop:- 

# a = {"mango","orange","banana","apple"}
# print(a.pop())


# set remove:-

# a = {"cricket","hockey","carrom","football"}
# a.remove("carrom")
# print(a)


# set clear:-

# a = {"Python tutorial will guide you to learn Python one step at a time with the help of examples."}
# a.clear()
# print(a)


# set discard:-  (if the elemt is not present then it gives key error )

# a = {"apple","mango","banana","pipe apple"}
# a.discard("mango")
# print(a)


# set union:- (add a + a2)


# a = {10, 20, 30, 40}
# a2 = {50, 60, 70, 80}
# a3 = a.union(a2)
# print(a3)


# set intersection:- (it gives common element)

# a = {15, 25, 35, 45}
# a2 = {25,18,26,45}
# a3 = a.intersection(a2)
# print(a3)


# set difference:- (delete same value)

# a = {10,20,30,40,50}
# a2 = {50,30,46,89,74}
# a3 = a - a2
# print(a3)


# set symetric_difference:- (same element is not prit in a and a2)


# a = {50,40,30,20,10}
# a2 = {20,40,84,65,66}
# a3 = a.symmetric_difference(a2)
# print(a3)


# 4.2 set:-


# set copy:-

# a = {"rohit","saurabh","vinay"}
# print(a.copy())


# set union:- (|)

# a = {51,45,66,23,51}
# a2 = {22,66,16,13,65}
# a3 = a | (a2)
# print(a3)


# set pop:-

# a = {"mango","orange","banana","apple"}

# a.pop()
# print(a)
# res = a.pop()
# print(res)


# set intersection:- ()

# a = {10,20,30,40,50}
# a2 = {"python","java",30,50,"c++"}
# a3 = a2.intersection(a)
# print(a3)


# set remove:-

# a = {"friends","bestfriends","collage"}
# a.remove("friends")
# print(a)


# set difference:-

# a = {100,200,300,400,500}
# a2 = {500,400,553,463,351}
# a3 = a - a2
# print(a3)


# set clear:-


# a = {"cricket","hockey","carrom","football"}
# a.clear()
# print(a)


# set symmetric_difference:-

# a = {12,24,36,48}
# a2 = {24,13,26,85}
# a3 = a.symmetric_difference(a2)
# print(a3)


# set add:-

# a = {"math","science","history"}
# a.add("marathi,hindi")
# print(a)


# set update:-


# a = {200,356,64,6651,161}
# a.update("python,java")
# print(a)



# 4.3 set:-


# symmetric_difference:-


# a = {0,20,30,0,50}
# a2 = {50,60,70,80,30}
# a3 = a.symmetric_difference(a2)
# print(a3)


# difference:-


# a = {"python","java","c++"}
# a2 = {"java","history","english"}
# a3 = a - a2
# print(a3)


# set intersection:-


# a = {"cricket","hockey","carrom","football"}
# a2 = {"cricket","football","python"}
# a3 = a.intersection(a2)
# print(a3)

# set union:-

# a = {31,61,161,1,33,31,654,646}
# a2 = {6,665,646,648,6,33,1}
# a3 = a | a2
# print(a3)


# set discard:-

# a = {"jeans","tshirt","shirt","jacket"}
# a.discard("jacket")
# print(a)


# set clear:-

# a = {2021,2022,2023,2024}
# a.clear()
# print(a)


# set remove:-

# a = {"yellow","red","white","black"}
# a.remove("black")
# print(a)


# set pop:-

# a = {12,85,96,32,14,77,8,52,69}
# a.pop()
# print(a)


# set copy:-

# a = {"Get the complete list of topics with proper Python notes"}
# a.copy()
# print(a)


# set update:-


# a = {"buffalo","teamspirit","leecooper"}
# a.update("being human, laser")
# print(a)


# set add:-


# a = {"school","collage","class"}
# a.add("byjuss , pwd")
# print(a)



# -----------------------------------------------------------------------------------------------------------------------/


# 5. dictionary features:-

# 1.key value pair.
# 2.key can not duplicates.
# 3.mutable. 
# 4.dict key - immutable.
# 5.dict values - mutable or immutable.
# 6.do not slicing


# dict update:-


# a = {"name":"rohit","PRN":2021321612042}
# a["collage"] = "JNEC"
# print(a)


# dict clear:-

# a = {"math":17, "science":18,"history":20}
# a.clear()
# print(a)


# dict get:-


# a = {"bollywood":"salman","hollywood":"tom cruise","tollywood":"vijay setupati"}
# print(a.get("tollywood"))


# dict pop:- 

# a = {"jeans":"blue","shirt":"black","shoes":"white"}
# print(a.pop("shoes"))


# dict keys:-

# a = {"math":17, "science":18,"history":20}
# print(a.keys())


# dict values:-

# a = {"rohit":"mechanical engineer","vinay":"civil engineer","saurabh":"elsectrical engineeer"}
# print(a.values())


# dict copy:-

# a = {"email":"rohit@gmail.com", "password":43112}
# print(a.copy())


# dict items:-

# a = {"mango":"yellow","apple":"red","gava":"green"}
# a2 = list(a.items())
# print(a2)


# dict fromkeys:-


# a = {}.fromkeys(["white","black","grey"],"color")
# print(a)



# dict pop items:-

# a = {"rohit":7972671,"suraj":702075,"mama":9923}
# a.popitem()
# print(a)

# res = a.popitem()
# print(res)


# dict key,value:-


# a = {"diploma":2020, "btech":2023,"status":"completed"}
# for key,value in a.items():
#     print(key,value)


# dict setdefault:-

# a = {"apple":"red","mango":"sweet","btech":"pass"}
# a.setdefault("rohit","mechanical")
# print(a)



# 5.2 dictionary:-


# dict items:-


# a = {"diploma":2020, "btech":2023,"status":"completed"}
# print(list(a.items()))


# dict fromkeys:- (same values for all key)

# a = {}.fromkeys(["math","science","history"],"subject")
# print(a)


# dict popitems:-

# a = {"name":"rohit","mobile no":79726719000}
# a.popitem()
# print(a)

# res = a.popitem()
# print(res)


# dict keys,value:-


# a = {"rohit":7972671900, "suraj":7020754005}
# for keys,value in a.items():
#     print(keys,value)


# dict setdefault:-

# a = {"police":100, "ambulance":108}
# a.setdefault("rohit",7972671900)
# print(a)


# dict update:-

# a = {}
# a["symbo"numbers":15664, "alphabate":"fscsd"l"]
# print(a)


# dict clear:-

# a = {"diploma":2020, "btech":2023,"status":"completed"}
# a.clear()
# print(a)


# dict get:-

# a = {"name":"rohit gaikwad", "collage":"JNEC", "state":"maharashtra"}
# print(a.get("state"))


# dict pop :- 

# a = {"rohit":7972671900, "suraj":7020754005}
# a.pop("rohit")
# print(a)


# dict keys:-

# a = {"diploma":2020, "btech":2023,"status":"completed"}
# print(a.keys())


# dict values:-

# a = {"diploma": 2020, "btech": 2023, "status": "completed"}
# print(a.values())


# dict copy:-

# a = {"day":"monday","date":14/5/2000}
# print(a.copy())




# 5.3 dict:-

# keys,value:-

# a = {"name":"rohit gaikwad","collage":"JNEC","PRN":2021321612042}
# for keys,values in a.items():
#     print(keys,values)


# dict pop items:-

# a = {"name":"rohit","PRN":2021321612042}
# a.popitem()
# print(a)

# res = a.popitem()
# print(res)


# dict fromkeys:-

# a = {}.fromkeys(["jeans","shirt","tshirt"],"blue")
# print(a)


# dict items:-

# a = {"numbers":15664, "alphabate":"fscsd"}
# print(list (a.items()))


# dict copy:-

# a = {"numbers": 15664, "alphabate": "fscsd", "symbol": "%$#@"}
# print(a.copy())


# dict values:-

# a = {"fruits":"mango","color":"red","city":"aurangabad"}
# print(a.values())


# dict keys:-


# a = {"city":"aurangabad","collage":"JNEC","PRN":2021321612042}
# print(a.keys())


# dict pop:-

# a = {"diploma":2020, "btech":2023,"status":"completed"}
# print(a.pop("status"))


# dict get:-

# a = {"diploma":2020, "btech":2023,"status":"completed"}
# print(a.get("diploma"))


# dict clear:-

# a = {"school":"bpv","diploma":"mgm","btech":"JNEC"}
# a.clear()
# print(a)


# dict update:-

# a = {"rohit":"boy","ishika":"girl"}
# a["scooter"] = "vehicle"
# print(a)


# dict setdefault:-

# a = {"name":"rohit","surname":"gaikwad"}
# a.setdefault("mobile no", 7972671900)
# print(a)

# ----------------------------------------------------------------------------------------------------------------------


# for loop:-


# 1. for loop with list:-


# a = ["python", "java", "c++"]
# for i in a:
#     print(i)


# 2. nested with star pattern:-

# for i in range(1,2):
#     for j in range(1,10):
#         print("*" * j)

        #   OR  #


# for i in range(1,5):
#     for j in range(1,5):
#         print("*",end=" ")
#     print()



# 3.for loop with continue with range:-

# for i in range(1,100):
#     if i == 25:
#         continue
#     print(i)


# 4.for loop continue statement:-

# a = "python devloper"
# for i in a:
#     if i == "d":
#         continue
#     print(i,end=" ")


# 5. python for loop with zip:-

# color = ["black","green","blue","white"]
# garments = ["jeans","shirt","tshirt","shoes"]
# for color,garments in zip(color,garments):
#     print(color, "is", garments)


# 6. for loop with else:
    
# for i in range(1,50):
#     print(i)
# else:
#     print("completed")


# 7. for loop with break statement:-

# a = "jawahar lal nehru engineering collage aurangabad"

# for i in a:
#     if i == "c":
#         break
#     print(i,end="")



# 8. for loop break in range:-

# for i in range(1,100):
#     if i == 55:
#         break
#     print(i,end=" ")


# 9.python for loop inside a for loop:-(nested_list)

# for i in range(1,10):
#     for j in range(1,10):
#         print(j,i)


# 10.python foor loop in dictionary:-


# a = dict()

# a["rohit"] = 7972671900
# a["suraj"] = 7020754005
# a["saurabh"] = 7972825358
# for i in a:
#     print("% s % d" % (i,a[i]))


# 11. sum of numbers in for loop:-

# sum = 0
# for i in range(1,20):
#     sum = sum + i
# print("the sum of numbers:-" ,sum)

# 12. for loop key & value:-

# i = 0
# a = {"math":18, "science":19, "history":17}
# for i in a:
#     print(f"key: {i} value: {(a[i])}")

# ---------------------------------------------------------------------------------------------------------------------


# while loop:-


# 1. while loop single statement block:-


# count = 0
# while(count < 10): count += 1; print("python")


# 2. whiloe loop with continue statement:-

# i = 0
# a = "python devloper"
# while i < len(a):
#     if a[i] == "v":
#         i += 1
#         continue
#     print(a[i],end=" ")
#     i += 1


# 3. python loop with break statement:-

# i = 0
# a = "being human"
# while i < len(a):
#     if a[i] == "h":
#         i += 1
#         break
#     print(a[i],end=" ")
#     i += 1


# 4. python sentinel control statement:- (2 to quit)

# a = int(input("enter the number:- "))
# while a != 2:
#     a = int(input("enter the number:- "))
# 


# 5. list print a perticular range:-

# i = 0
# a = (10,20,50,56,646,356,86,315,646)
# while i < 6:
#     print(a[i])
#     i += 1
# else:
#     print("the loop has completed")


# 6. while loop :-

# i = 0
# a = ("python","java","c++","mechanical","civil")
# while i < len(a):
#     print("course name: ", a[i])
#     i += 1



# 7. reversed full list print:-

# i = -1
# a = (65165,4646,1616,164,68486,646,3213)
# while i > (-len(a)-1):
#     print(a[i])
#     i -= 1
# print("completed")

                        #    OR


# i = -1
# a = ("Your attitude is critical to success")
# while i > (-len(a)-1):
#     print(a[i],end="")
#     i -= 1

# -------------------------------------------------------------------------------------------------------

# if-else-elif:-

1.

# name = "rohit, suraj, saurabh, vinay, ayush".lower()
# user_name = input("enter the user_name: ").lower()
# if user_name in name:
#     print(f"Hiiii {user_name} welccome back...!")

# else:
#     print("sry invalid name")


2. 

# while True:
#     email_id = input("enter the email_id: ")
#     if email_id == "rohitgaikwad55@gmail.com":
#         while True:
#             password = input("enter the password: ")
#             if password == "Rohit111":
#                 print("hiiiii Rohit....!")
#                 print("welcome back...! ")
#                 break
#             else:
#                 print("Wrong password")
#         break

#     else:
#         print("invalid email_id")



# 3.odd,even value:-

# i =0
# for i in range(1,20):
#     if i % 2 == 0:
#         print(f"even value {i}")
#     else:
#         print(f"odd value {i}")
#         i += 1


4. 

# score = 100
# score = int(input("enter the score: "))
# if score > 100 or score < 0:
#     print("invalid")

# elif score > 75:
#     print("1st class")

# elif score > 60:
#     print("2nd class")
# elif score > 50:
#     print("3rd class")
# else:
#     print("ATKT")

5. 

# i = 100
# if i == 80:
#     print("i is 80")
# elif i == 50:
#     print("i is 80")
# elif i == 100:
#     print(i is 100)
# else:
#     print("i is not present")


6.

# num = 10

# if num < 10:
#     print("wrong")
# elif num > 10:
#     print("")
# elif num == 10:
#     print("right")

# else:
#     print("num is not present")



7.

# name = "rohit, saurabh, vinay, suraj"
# user_name = input("enter the name: ")
# if name == ("Rohit, Saurabh, Vinay, Suraj").lower():
#     print(f"Hiii Welcome back {user_name}.....!")
# else:
#     print("sorrry")


8.

# fruits = ("mango, apple, pineapple, orange").lower()

# fruits_name = input("enter product:-").lower()

# if fruits_name in fruits:
#     print("available")

# else:
#     print("sry product is out of stock")

# print("thank you for shopping.....!")


9. 


# score = 100

# score = int(input("enter your score: "))
# if score > 75:
#     print("jnec allowted")
#     print("best of luck")

# elif score > 60:
#     print("mgm allowted")
#     print("best of luck")

# elif score < 50:
#     print("mit allowted")


10.

# a = 105
# b = 100

# if a == b:
#     print("both are same")
# elif a != b:
#     print("right")
# else:
#     print("both are different")


# ----------------------------------------------------------------------------------------------------------------------



# command line arguments:-


# 1. positional arguments:-


# def func(python, java, datascience, c):

#     print(python, java)

# func(100,200,300,400)




# def func(a, b, c, d):
#     add = a + b
#     mul = a * c
#     sub = d - b
#     print(mul, sub)

# func(65, 66, 161, 151)




# def marks(physics, math, history, english):
#     print(math, history,english)

# marks(18, 20, 17, 19)


# ----------------------------------------------------------------------------------------------------------------------


# 2. default arguments:-


# def cloths(jeans, shirt, tshirt = "white", jacket= None):
#     print(tshirt, shirt, jacket)

# cloths("black", "green")




# def func(name, msg = "hellooo"):
#     message = f"{msg} {name}!"
#     print (message)

# func(name = "Rohit")



# def func(a, b = "thon"):
#     print(a + b)

# func(a = "py")


# ------------------------------------------------------------------------------------------------------------------------


# 3. keyword arguments:-


# def func(a, b, c, d, e):
#     print(a, b, c, d, e)

# func(a = 100, b = 200, c = 400, d = 555, e = 0)



# def func(firstname, lastname):
#     print(firstname, lastname)

# func(firstname = "ROHIT", lastname = "GAIKWAD")



# def func(rohit,saurabh,vinay):
#     print(vinay)

# func(rohit = 7972671900, saurabh = 7972825358, vinay = 8485839091)

#  ------------------------------------------------------------------------------------------------------------------------


#  varible length arguments:- (it takes min 0th no of arguments and max N number of arguments)


# def func(*args):
#     return args

# res = func("python, java, (10,20,30), none")
# print(res)



# def total(*args):
#     return sum(args)

# res = total(6565,6466,6565165,616565,351651,651651)
# print(res)



# def func(*args):
#     total = 0
#     for i in args:
#         total += i
#         return total

# res = func(64654,646464,6464,86,64654,9879,5486,35468)
# print(res)  


# -------------------------------------------------------------------------------------------------------------------

# varible length of keyword arguments:- (min(0) max(N) (its gives a dictionary)


# def marks(**kwargs):
#     return kwargs

# res = marks(math = 19, physics = 18, english = "fail")
# print(res)



# def func(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key} : {value}")

# func(name = "rohit gaikwad", PRN = 2021321612042, email_id = "rohitgaikwad2000@gmailcom")



# def student(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key} : {value}")

# student(name = "rohit gaikwad", PRN = 2021321612042, collage = "JNEC")
# print()
# student(name = "vinay jojare", PRN = 2021321612041, collage = "JNEC")



# ----------------------------------------------------------------------------------------------------------------------


# function:-

# 1. default and keyword agruments:-

# def details(name,age=23):
#     return f"hello i am {name} i am {age} years old!"

# res = details(name = "Rohit gaikwad")
# print(res)


# 2. 

# def func(lst):
#     temp = lst[3]
#     del(lst[3])
#     print(lst)
#     return temp

# res = func([10,20,30,40,50])
# print(res)    


# 3. function inside nested function:-

# def outer():

#     def inner():
#         print("goood morning")

#     print("Hiii")
#     inner()

# outer()
# print("have a nice day")


# 4. define all type of arguments:- (pisitional,default,**kwargs,keyword)


# def func(a, b, v1, c = "rohit", **kwargs):
#     print(10, 20, v1, kwargs,c)

# func(616,11, v1 = 7972671900, name = "saurabh")



# 5. combination of *args and **kwargs:-


# def func(*args,**kwargs):
#     print(sum(args))

#     for key,value in kwargs.items():
#         print(f"{key} : {value}")

# func(1516, 5616, 113, name = "rohit", PRN = 2021321612042, collage = "pass")



# 6. pass function as an arguments:-


# def func1():
#     print("good morning")

# def func2(func1):
#     print("hiii")
#     func1()

# func2(func1)
# print("have a nice day")


# 7.

# def func1(func, msg = "goood morning"): 
#     return func() + msg

# def func2():
#     return "heyyy"

# res = func1(func2)
# print(res)


# 8.

# def student(**kwargs): 
#     for key,value in kwargs.items():
#             print(f"{key} : {value}")

# res = student(name = "rohit gaikwad", result = "pass")
# print()
# res = student(name = "sauabh", result = "pass")
# print()
# res = student(name = "vinay", result = "pass")



# 9. 


# def func(n):
#     def func1(x):
#         return n * x
#     return func1()

# res = func(10)
# print(func(10)(5))

# res = func(6)
# print(func(6)(8))

# res = func(9)
# print(func(9)(5))



# 10.

# msg = "good morning"

# def func():
#     print('local: ', msg)

# func()
# print('global: ',  "good evening")


# ---------------------------------------------------------------------------------------------------------------------
