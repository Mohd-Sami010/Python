employees = [
    {"id": 1, "name": "Ram", "salary": 20000},
    {"id": 2, "name": "Shyam", "salary": 25000},
    {"id": 3, "name": "Mohan", "salary": 30000}
]
eid = int(input("Enter employee id: "))
for emp in employees:
    if emp["id"] == eid:
        print("Details:", emp)