In this project, we have to make todo which store the name and length of any particuler video and I also want to store that things in a text file.

file handling -->
file = open('youTube.txt','w')

try:
    file.write('chai aur code')
    
finally:
    file.close()


another way for writing in file is-->
with open('youTube.txt','w') as file:
    file.write('chai aur code')

    