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

# with open("student.csv") as file:
#     for line in file:
#         name,address = line.rstrip().split(",")
#         student = {"name":name, "address":address}
        
#         if name != 'Student_Name':
#             students.append(student)

# for info in sorted(students):  # here, sorting is not done properly so to sort them according name or house we need to implement different feature.
#     print(info)

# below methods can be defined using lamda also.
# def get_name(student):
#     return student["name"]

# def get_address(student):
#     return student["address"]

# for student in sorted(students,key= lambda student: student["name"]):
#     print(f"{student['name']} is in {student['address']}")


# Another way of reading a csv file is using reader method of csv

with open("student.csv") as file:
    # reader = csv.reader(file) # here reader method read the csv file, and it remaind the commas,and other things.
    # for row in reader:
    #     if row[0] != "Student_Name":
    #         students.append({"name":row[0],"address":row[1]})
    reader = csv.DictReader(file) # here using DictReader instead of reader is because suppose if someone interchange the name and address column then in above code row[0] gives address instead of name which cause our code to break down, so to get prevent from it we use it .
    for row in reader:
        students.append({"name":row["Student_Name"] , "address":row["Student_Address"]})
        
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['address']}")
    
    