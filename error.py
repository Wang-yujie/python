file1 = "cats.txt"
file2 = "dogs.txt"
try:
    with open(file1) as cats:
        ca = cats.read()
except FileNotFoundError:
    print("can not find file " + file1 + " !")
else:
    print(ca)
try:
    with open(file2) as dogs:
        do = dogs.read()
except FileNotFoundError:
    print("can not find file " + file2 + " !")
else:
    print(do)