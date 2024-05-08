import os

# student = [
#       {"Name":"Vinay Rai","Dept":"CSE","Marks":123},
#       {"Name":"Akash","Dept":"Bsc","Marks":120}
#     ]

# def Insert(name,dept,marks):
#     record = {"Name":name,"Dept":dept,"Marks":marks}
#     student.append(record)
    
# def Delete(name):
#     for x in student:
#         if name == x["Name"]:
#             student.remove(x)
#             print("Record found and deleted successfully.")
#             break
            
# def Search(name):
#     for x in student:
#         if x["Name"] == name:
#             print("Record found successfully ---> ")
#             print(x)
#             break
        
    
# def Display():
#     print(student)

# File Handling

# 1st way to write in file 
with open("text.txt","w",encoding="Utf-8") as fs:
    fs.write("I am Vinay Rai , a cse student.\n")
    fs.write("I am going to do intern this summer.")

# 2nd way to write in file
# try:
#     fs = open("text.txt","w",encoding="Utf-8")
#     fs.write("Hii!! I am VJR.")
        
# finally:
#     fs.close()

# with open("text.txt","r",encoding="Utf-8") as fs:
#     # print(fs.read(10))
#     # print(fs.read())
#     for line in fs:
#         print(fs.readline())
        
# os.remove("text.txt")

# with open("text.txt","r",encoding="Utf-8") as fs:
#     print(fs.read(10))
#     print(fs.tell())
#     print(fs.read(15))
#     print(fs.tell())
#     fs.seek(0,0)   
#     print(fs.read(10))


path = os.getcwd()
# print(os.listdir())
os.rmdir('C:\Users\Desktop\Python\\newg.py')
print(os.listdir())


    

    
