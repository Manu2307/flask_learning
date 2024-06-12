from python_mongoDB.base import Employee
print(list(Employee.find()))

data_to_insert = [
    {
        'Name': 'Hema Guduru', 'Role': 'Senior Software Engineer', 'Address': 'Ameenpur'
    },
    {
        'Name': 'Abinash Panda', 'Role': 'Senior Software Engineer', 'Address': 'Kondapur'
    }
]

Employee.insert_many(data_to_insert)

print(list(Employee.find()))
