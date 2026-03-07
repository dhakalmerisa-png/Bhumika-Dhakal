with open ('file.txt', 'w') as file:
    file.write("Hello World\n")
with open ('file.txt', 'r') as file:
    content = file.read()
    print(content)
with open ('file.txt', 'a') as file:
    file.write("This\n")
#old method 
#file=open("hello.txt", 'w')
#file.write("Hello World\n")
#file.close()














