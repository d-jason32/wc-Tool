import sys
import os

def byte(s):
    file_name = s
    file_stat = os.stat(file_name)
    return file_stat.st_size

def lines(s):
    file_name = s
    file_stat = os.stat(file_name)
    return file_stat.st_size

if __name__ == "__main__":

    if sys.argv[1] == "-c":
        print(byte(sys.argv[2]))
    
    elif sys.argv[1] == "-l":
        print(lines(sys.argv[2]))

