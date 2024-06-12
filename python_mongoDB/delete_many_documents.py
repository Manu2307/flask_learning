from python_mongoDB.base import Employee

print(list(Employee.find()))

Employee.delete_many({'Name': {"$in": ['Abinash Panda', 'Hema Guduru']}})

print(list(Employee.find()))
