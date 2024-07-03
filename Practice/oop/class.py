# Classes allow to create our own data type.   

class Student():
    def __init__(self,name,rollNo):
        
        self.name = name
        self.rollNo = rollNo
        
    def print_student(self):
        print(f"{self.name} is CSE Student,having rollNo {self.rollNo}.")

    @property
    def rollNo(self):
        return self._rollNo
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name
    
    @rollNo.setter
    def rollNo(self,rollNo):
        if rollNo not in [129,219]:
            raise ValueError("RollNo is out of scope")
        self._rollNo = rollNo
    
def main():
    student = get_student()
    student._rollNo = 120  # here anyone can change our instance's attributes,so avoid it we use property.
    student.print_student()
    
def get_student():
    name = input("Your's Name: ")
    rollNo = int(input("Your's RollNo: "))
    return Student(name,rollNo) # here class instance is created and returned
    
if __name__ == "__main__":
    main()