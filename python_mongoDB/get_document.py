from python_mongoDB.base import Employee


data = Employee.find_one({'Name': 'Manoj Kumar'})
print(data)
