import os

def write_file():
    with open("test.txt", "w") as file:
        file.write("The service wrote text!")

if __name__ == '__main__':
    write_file() 
