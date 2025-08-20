#create a new file 
new_file = open('New_File.txt', 'x')
new_file.close()

#check if a file exists
import os
print("Checking if my_file exist or not....")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exist")

#creat a new if it doesn't
my_file = open("my_file.txt", "w")
my_file.write("Hi! I am penguin and I am 1 yr old.")
my_file.close()

#delete the folder
os.rmdir('Folder')