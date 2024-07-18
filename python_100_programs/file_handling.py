# writing to a file

with open("output.txt","w") as file:
    file.write("Hello, this is a simple text.")
    
# reading from a file

with open("output.txt","r") as file:
    data = file.read()
    print("Data from file: ", data)    