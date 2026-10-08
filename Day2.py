# #OOPS
# class Employee :
#     def __init__(self,user,password) :
#         self.user=user
#         self.__password=password
#         self._salary=1000
#         # self.userDashboard()
        
#     def userDashboard(self) :
#         userInput=input(f"""Welcome {self.user} enter your input : 
#                             1.create your login id
#                             2.login
#                             3. Check Your Salary
#                             4. Check Your performance
#                             5. Exit """)
#         if userInput=='1' :
#             self.createLogin()
#         elif userInput=='2' :
#             self.login()
#         elif userInput=='3' :
#             self.Knowsalary()
#         elif userInput=='4' :
#             self.alldata()
#         elif userInput =="5":
#             print("BYE")
#     def createLogin(self):
#         self.user=input("Enter Your Name : ")
#         self.password=input("Enter Your password : ")

#     def login(self):
#         loginUser=input("Enter Your Name : ")
#         loginpassword=input("Enter Your password : ")

#         if self.checkUser(loginUser,loginpassword):
#              print(f"welcome {self.user} in our Company")
#         else:
#              print("invalid User")

#     def Knowsalary(self):
#         if self.user:
#             print(f"{self.user} salary is {self._salary}")
#         else:
#             print("Login first")
#     def alldata(self):
#         self._salary=300+self._salary
#         print(f"{self.user} salary is {self._salary}")

#     def checkUser(self,user,password):
#          if user==self.user and password==self.__password :
#               return True
#          else :
#               return False
              
# employees=[]
# emp1=Employee("Ram","1234")
# emp2=Employee("Rahul","3456")
# # emp1.Knowsalary()
# employees.append(emp1)
# employees.append(emp2)
# def findEmployee(username):
#     for person in employees:
#         if person.user==username:
#             return person
#     return None    
# e=findEmployee("Ram")
# e2=findEmployee("Rahul")
# e2.alldata()
# e.Knowsalary()
# emp2.Knowsalary()

# class Company:
#     counter=0
#     def __init__(self):
#         self.__id=None
#         self.role=""
#         self.field=""
#         self.employees=[]
#     def addEmployee(self,role,field,name,phone,address):
#         Company.counter+=1
#         self.__id=Company.counter
#         self.role=role
#         self.field=field
#         self.employees.append(Employee(name,phone,address))
#     def showEmployee(self):
#         for employee in self.employees :
#             print(f"ID : {self.__id}\nRole :{self.role}\nfield: {self.field}")
#             print(f"Name: {employee.name}")
# class Employee:
#     def __init__(self,name,phone,address):
#         self.name=name
#         self.__phone=phone
#         self.address=address

#     def editEmployee(self,name,phone,address):
#         self.name=name
#         self.__phone=phone
#         self.address=address

# com1=Company()
# com1.addEmployee("Tech Support","Technical","Anand","95233","Delhi")
# com1.addEmployee("Sale associate","BPO","Anvi","88078","Delhi")
# com1.showEmployee()

# class Car:
#     def __init__(self,color,engineType,price):
#         self.color=color
#         self.engineType=engineType
#         self.price=price
#     def specify(self):
#         print(f"Your {self.color}'s color car Looks Nice. as its price is {self.price} it will have {self.engineType}, i guess")
# class Suzuki(Car):
#     def specify(self):
#         print(f"Your {self.color}'s suzuki car Looks Nice. as its price is {self.price} it will have {self.engineType}, i guess")
    
# car1=Suzuki("red","4 stroke", "3mil")
# car1.specify()

# class A:
#     def m1(self):
#         return 20
# class B(A):
#     def m1(self):
#         val= super().m1()+30
#         return val
# class C(B):
#     def m1(self):
#         val= super().m1()+40
#         return val

# obj=C()
# print(obj.m1())

# def maximumnumber(*num):
#     return max(num)
# print(maximumnumber(20,30,40,50,30))

# def UserData(**users):
#     for key,value in users.items():
#         print(f"{key} is {value}")

# UserData(Name="Anand",Age=20,city="Delhi")
# l=[1,2,3,4,5,6,7,8,9,10]
# result=filter(lambda x:x%2==0,l)
# print(list(result))

# list=[x*x for x in range(1,6)]
# print(list)

# class Students:
#     def __init__(self,name,age,course):
#         self.name=name
#         self.age=age
#         self.course=course
#     def introduce(self):
#         print(f"Student Name : {self.name} \n age : {self.age} \n Course : {self.course}")

# student1=Students("Anand",20,"B.tech")
# student1.introduce()

# class Animal:
#     def sound(self):
#         print("Animal Sound ")
# class Dog(Animal):
#     def sound(self):
#         print("Bark")
# d1=Dog()
# d1.sound()

# def students():
#     for i in range(5):
#         yield i
# x=students()
# for student in x:
#     print(student)

# try:
#     inp=int(input("enter a number : "))
# except ValueError:
#     print("Enter a valid input")
# except ValueError:
#     print("Enter a valid input")
# else:
#     print("input is",inp)
# finally:
#     print("chalo aage padho!")


