#open file and read its contents
file = open('Codingal.txt','r')
print(file.read())
file.close()

#open file and read its beginnnig 8 characters
file = open('Codingal.txt','r')
print("\n Read in parts \n")
print(file.read(8))
file.close()