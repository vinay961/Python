import csv

# def get_user_input():
#     name = input("Enter your name: ")
#     address = input("Enter your address: ")
#     return name, address

# def write_to_csv(file_name, data):
#     with open(file_name, mode='a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(data)

# def main():
#     file_name = 'student.csv'
#     try:
#         with open(file_name, mode='x', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(['Student_Name', 'Student_Address'])
#     except FileExistsError:
#         pass  
    
#     while True:
#         name, address = get_user_input()
#         write_to_csv(file_name, [name, address])
#         another = input("Do you want to add another entry? (yes/no): ")
#         if another.lower() != 'yes':
#             break

# if __name__ == "__main__":
#     main()

students = []

with open("student.csv") as file:
    for line in file:
        name,address = line.rstrip().split(",")
        student = {"name":name, "address":address}
        
        if name != 'Student_Name':
            students.append(student)

# for info in sorted(students):  # here, sorting is not done properly so to sort them according name or house we need to implement different feature.
#     print(info)

def get_name(student):
    return student["name"]

def get_address(student):
    return student["address"]

for student in sorted(students,key=get_address):
    print(f"{student['name']} is in {student['address']}")