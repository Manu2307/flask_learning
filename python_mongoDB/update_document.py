from python_mongoDB.base import Employee

data = Employee.find()
print(list(data))

Employee.update_one({"Name": "Manoj Kumar"}, {'$set': {"Address": "Hyderabad"}})

data = Employee.find()
print(list(data))
