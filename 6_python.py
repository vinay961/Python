# Here we try to write something in files.
file1 = open("sample.txt","w")   # types of modes: w ->write,w+ ->write and read,r,r+,
file1.write("Hello \n")

L = ["I am Vinay Rai \n", "I am CSE student \n","I am currently in 3rd year \n"]
file1.writelines(L)
file1.close()


# now lets us try to read this files
file2 = open("sample.txt","r+")
para = file2.read()
# print(file2.readline(9))
file2.close()

# append --> it always add to the last
file3 = open("sample.txt","a")
file3.write("Appended")


# Text preprocessing -- we use split() method.

#length of paragraph
# para = file2.read()
# txt = para.split("\n")
# print(len(txt))

#let us see how many lines present in text
txt = para.split(".")
print(len(txt))

