from python_mongoDB.base import Employee

print(list(Employee.find()))
Employee.delete_one({'Name': "Manoj Kumar 1"})

print(list(Employee.find()))
