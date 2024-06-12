from python_mongoDB.base import Employee

emp1 = {
    "Name": "Manoj Kumar",
    "Role": "Software Engineer",
    "Address": "Amberpet"
}

Employee.insert_one(emp1)

