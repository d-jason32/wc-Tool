import sys
import os

def byte(s):
    file_name = s
    file_stat = os.stat(file_name)
    return file_stat.st_size

def lines(s):
    file_name = open(s, "r")
    file_stat = len(file_name.readlines())
    return file_stat

def words(s):
    file = open(s, "r")
    data = file.read()
    lines = data.split()
    return len(lines)

def characters(s):
    file = open(s, "r")
    data = file.read()
    return len(data) 

if __name__ == "__main__":

    if sys.argv[1] == "-c":
        print(byte(sys.argv[2]))
    elif sys.argv[1] == "-l":
        print(lines(sys.argv[2]))
    elif sys.argv[1] == "-w":
        print(words(sys.argv[2]))
    elif sys.argv[1] == "-m":
        print(characters(sys.argv[2]))
    elif len(sys.argv) == 2:
        s1 = sys.argv[1]
        print(f"{byte(s1)} {lines(s1)} {words(s1)} {characters(s1)} {s1}")

