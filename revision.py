# for i in range(1,20,3):
#     print(i,end=",")

# for i in range(4):
#     print(10**i,end=",")

# for i in range(10,0,-2):
#     print(i,end=",")

# for i in range(1, 6):
#     for j in range(i):
#         print(i, end="")
#     print()

# n = int(input("Enter the number of terms: "))
#
# a = 0
# b = 1
#
# print("Fibonacci Series:")
#
# for i in range(n):
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c
#
#
# word = "PYTHON"
#
# for i in range(1, len(word) + 1):
#     print(*word[:i])
#
#
#
# word = "PYTHON"
#
# for i in range(1, len(word) + 1):
#     for j in range(i):
#         print(word[j], end=" ")
#     print()

# L=[12,13,7,77,53]
#
# for num in L:
#     is_prime = True
#
#     if num < 2:
#         is_prime = False
#     else:
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break
#
#     if is_prime:
#         print(num)
#
# num = int(input("Enter a number: "))
#
# print("Factors of", num, "are:")
#
# for i in range(1, num + 1):
#     if num % i == 0:
#         print(i)

# 1
#
# employees = [
#     {"empid": 101, "name": "Arun", "email": "arun@gmail.com"},
#     {"empid": 102, "name": "Amal", "email": "amal@gmail.com"},
#     {"empid": 103, "name": "Anu", "email": "anu@gmail.com"}
# ]
#
# emails = list(map(lambda x: x["email"], employees))
#
# print(emails)


# 2
#
# class Mobile:
#
#
#     def display_details(mobile):
#         print("Brand:", mobile.brand)
#         print("Model:", mobile.model)
#         print("Price:", mobile.price)
#         print("Storage:", mobile.storage)
#         print("Battery:", mobile.battery)
#
#     
#     def apply_discount(mobile, amount):
#         mobile.price = mobile.price - amount
#         print("Price after discount:", mobile.price)
#
#
# # Create object
# m = Mobile()
#
# m.brand = "Samsung"
# m.model = "Galaxy A55"
# m.price = 30000
# m.storage = "128 GB"
# m.battery = "5000 mAh"
#
# Mobile.display_details(m)
#
# Mobile.apply_discount(m, 2000)

#
# 4
#
# class Company:
#
#
#     def display_company(emp):
#         print("Company Name:", emp.company_name)
#         print("Location:", emp.location)
#
#
# class Employee(Company):
#
#
#     def display_details(emp):
#         print("Employee Name:", emp.employee_name)
#         print("Salary:", emp.salary)
#         print("Experience:", emp.experience, "years")
#         Employee.display_company(emp)
#
#
#     def check_eligibility(emp):
#         if emp.experience >= 5:
#             print("Eligible for promotion")
#         else:
#             print("Not eligible for promotion")
#
#
#     def update_salary(emp, amount):
#         emp.salary = emp.salary + amount
#         print("Updated Salary:", emp.salary)
#
#
# # Create object
# e = Employee()
#
# e.company_name = "ABC Technologies"
# e.location = "Kochi"
# e.employee_name = "Arun"
# e.salary = 40000
# e.experience = 6
#
# # Call methods
# Employee.display_details(e)
# Employee.check_eligibility(e)
# Employee.update_salary(e, 5000)



# employees = [
#     {"empid": 101, "name": "Arun", "email": "arun@gmail.com"},
#     {"empid": 102, "name": "Amal", "email": "amal@gmail.com"},
#     {"empid": 103, "name": "Anu", "email": "anu@gmail.com"}
# ]
#
# emails = list(map(lambda x: x["email"], employees))
#
# print(emails)
#
#
# 2
#
# class Mobile:
#
#     @staticmethod
#     def display_details(mobile):
#         print("Brand:", mobile.brand)
#         print("Model:", mobile.model)
#         print("Price:", mobile.price)
#         print("Storage:", mobile.storage)
#         print("Battery:", mobile.battery)
#
#     @staticmethod
#     def apply_discount(mobile, amount):
#         mobile.price = mobile.price - amount
#         print("Price after discount:", mobile.price)
#
#
# # Create object
# m = Mobile()
#
# m.brand = "Samsung"
# m.model = "Galaxy A55"
# m.price = 30000
# m.storage = "128 GB"
# m.battery = "5000 mAh"
#
# Mobile.display_details(m)
#
# Mobile.apply_discount(m, 2000)
#
#
# 4
#
# class Company:
#
#     @staticmethod
#     def display_company(emp):
#         print("Company Name:", emp.company_name)
#         print("Location:", emp.location)
#
#
# class Employee(Company):
#
#     @staticmethod
#     def display_details(emp):
#         print("Employee Name:", emp.employee_name)
#         print("Salary:", emp.salary)
#         print("Experience:", emp.experience, "years")
#         Employee.display_company(emp)
#
#     @staticmethod
#     def check_eligibility(emp):
#         if emp.experience >= 5:
#             print("Eligible for promotion")
#         else:
#             print("Not eligible for promotion")
#
#     @staticmethod
#     def update_salary(emp, amount):
#         emp.salary = emp.salary + amount
#         print("Updated Salary:", emp.salary)
#
#
# # Create object
# e = Employee()
#
# e.company_name = "ABC Technologies"
# e.location = "Kochi"
# e.employee_name = "Arun"
# e.salary = 40000
# e.experience = 6
#
# # Call methods
# Employee.display_details(e)
# Employee.check_eligibility(e)
# Employee.update_salary(e, 5000)
#
#
# 1
#
# employees = [
#     {"empid": 101, "name": "Arun", "email": "arun@gmail.com"},
#     {"empid": 102, "name": "Amal", "email": "amal@gmail.com"},
#     {"empid": 103, "name": "Anu", "email": "anu@gmail.com"}
# ]
#
# emails = list(map(lambda x: x["email"], employees))
#
# print(emails)
# #
# #
# # 2
# #
# class Mobile:
#
#     @staticmethod
#     def display_details(mobile):
#         print("Brand:", mobile.brand)
#         print("Model:", mobile.model)
#         print("Price:", mobile.price)
#         print("Storage:", mobile.storage)
#         print("Battery:", mobile.battery)
#
#     @staticmethod
#     def apply_discount(mobile, amount):
#         mobile.price = mobile.price - amount
#         print("Price after discount:", mobile.price)
#
#
# # Create object
# m = Mobile()
#
# m.brand = "Samsung"
# m.model = "Galaxy A55"
# m.price = 30000
# m.storage = "128 GB"
# m.battery = "5000 mAh"
#
# Mobile.display_details(m)
#
# Mobile.apply_discount(m, 2000)
# #
# #
# # 4
# #
# class Company:
#
#     @staticmethod
#     def display_company(emp):
#         print("Company Name:", emp.company_name)
#         print("Location:", emp.location)
#
#
# class Employee(Company):
#
#     @staticmethod
#     def display_details(emp):
#         print("Employee Name:", emp.employee_name)
#         print("Salary:", emp.salary)
#         print("Experience:", emp.experience, "years")
#         Employee.display_company(emp)
#
#     @staticmethod
#     def check_eligibility(emp):
#         if emp.experience >= 5:
#             print("Eligible for promotion")
#         else:
#             print("Not eligible for promotion")
#
#     @staticmethod
#     def update_salary(emp, amount):
#         emp.salary = emp.salary + amount
#         print("Updated Salary:", emp.salary)
#
#
# # Create object
# e = Employee()
#
# e.company_name = "ABC Technologies"
# e.location = "Kochi"
# e.employee_name = "Arun"
# e.salary = 40000
# e.experience = 6
#
# # Call methods
# Employee.display_details(e)
# Employee.check_eligibility(e)
# Employee.update_salary(e, 5000)

num = 153
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** 3
    temp = temp // 10

if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")



n = 10
a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b




num = 17
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime number")
else:
    print("Not a prime number")
    