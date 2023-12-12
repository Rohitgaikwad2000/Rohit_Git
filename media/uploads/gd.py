# a = ["python",10,20,3040]
# print(a,type(a))


# a = "python131165@%%3454"
# print(a,type(a))


# a = ("python",10,20,30,("kjsbjhbj"))
# print(a,type(a)).


# a = {"python",10,20,30,("kjkslks")}
# print(a,type(a))


# a = range(0,100)
# print(a,type(a))


# a = frozenset({"python",10,20,30,(10,20,33)})
# print(a,type(a))


# a = b"python,51661,sgdf"
# print(a,type(a))






# class employee():
#     def __init__(self,id,name,salary,age):
#         self.id = id
#         self.name = name
#         self.salary = salary
#         self.age = age


#     def __str__(self):
#         return f"{self.__dict__}"
    

#     def __repr__(self):
#         return f"\n{self.__dict__}"
    

# import random
# def creat_name():
#     name = ""
#     for i in range(0,random.randint(3,6)):
#         name += chr(65+random.randint(0,25))
#     return name.title()

 
# def creat_emp_details(no):
#     employee_list = []   
#     for i in range(1,no+1):
#         sal = random.randint(20000,80000)
#         age = random.randint(20,30)
#         em1 = employee(0+i,creat_name(),sal,age)
#         employee_list.append(em1)
#     return employee_list
# print(creat_emp_details(200))


# def get_emp_datails(id):     # reusable code 
#     all_employee = creat_emp_details(200)
#     for i in all_employee:
#         if i.id == id:
#             return i
# print(get_emp_datails(153))
        

# def get_emp_by_initial(letter):
#     all_employee = creat_emp_details(200)
#     for i in all_employee:
#         if i.name[0] == letter:
#             print(i) 

# print(get_emp_by_initial("P"))


# def get_employee_by_age(age):
#     all_employee = creat_emp_details(200)
#     for i in all_employee:
#         if i.age == age:
#             print(i)

# print(get_employee_by_age(30))