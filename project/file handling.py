def file_operations():
    # Create a sample text file for demonstration
    with open('sample.txt', 'w') as f:
        f.write("Hello, this is a sample file.\n")
        f.write("It contains multiple lines of text.\n")

    # 1. Read mode ('r')
    print("Reading from the file:")
    with open('sample.txt', 'r') as f:
        content = f.read()
        print(content)

    # 2. Write mode ('w') - This will overwrite the file
    print("Writing to the file:")
    with open('sample.txt', 'w') as f:
        f.write("This file has been overwritten.\n")
        f.write("New content added.\n")

    # 3. Read the file again to see the changes
    print("Reading after writing:")
    with open('sample.txt', 'r') as f:
        content = f.read()
        print(content)

    # 4. Append mode ('a') - This will add content to the end of the file
    print("Appending to the file:")
    with open('sample.txt', 'a') as f:
        f.write("This line is appended to the file.\n")

    # 5. Read the file again to see the appended content
    print("Reading after appending:")
    with open('sample.txt', 'r') as f:
        content = f.read()
        print(content)

    # 6. Read/Write mode ('r+')
    print("Using read/write mode:")
    with open('sample.txt', 'r+') as f:
        # Read the current content
        content = f.read()
        print("Current content:")
        print(content)

        # Move the cursor to the beginning of the file
        f.seek(0)
        # Write new content at the beginning
        f.write("This is new content at the start.\n")

    # 7. Read the file again to see the changes
    print("Reading after using read/write mode:")
    with open('sample.txt', 'r') as f:
        content = f.read()
        print(content)

if __name__ == "__main__":
    file_operations()
