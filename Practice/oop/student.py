def main():
    student = get_student()
        
    print(f"{student['Name']} has Roll_No--> {student['RollNo']}")

def get_student():
    # name = input("Name: ")
    # rollNo = input("Roll_No: ")
    # return name, rollNo  # basically here we are returning a tuple with name and rollNo.
    
    student = {}
    student["Name"] = input("Name: ")
    student["RollNo"] = input("RollNo: ")
    return student      # basically here we are returing a dict with key Name and RollNo.


if __name__ == "__main__":
    main()