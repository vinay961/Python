# empty list for storing the student records.
student_record = [
    {"name":"Vinay Rai","roll_no":129,"marks":[90,90,90]},
    {"name":"samir","roll_no":91,"marks":[90,90,90]}
]

# Let's add some other entries
student_record.append({"name":"Shikhar","roll_no":104,"marks":[90,90,90]})
# print(student_record) #like this we can add other entries also.

# Now's let calculate the percentage and append it to the list
for student in student_record:
    total_marks = sum(student["marks"])
    percentage = total_marks/len(student["marks"])
    student["percentage"]=percentage
    
# printing the record 
for student in student_record:
    print("Name",student["name"])
    print("Roll_No",student["roll_no"])
    print("Marks",student["marks"])
    print("Percentage",student["percentage"])

