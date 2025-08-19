# Program to removelines starting with any prefix
file1 = open('Codingal.txt', 'r')
file2 = open('CodingalUpdated.txt', 'w')

#reading each linefrom original
#text file
for line in file1.readlines():
    # reading all lines that do not
    # begin with "Coding"
    if not (line.startswith('Coding')):

        # printing those lines 
        print(line)
        
        # storing only those lines that
        # do not begin with "coding"
        file2.write(line)

#close and savethe files
file2.close()
file1.close()