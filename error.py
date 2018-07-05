# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0!")
#     else:
#         print(answer)
# print("Give me two numbers")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     try:
#         int(first_number)
#     except ValueError:
#         print("please enter numble, not word")
#     else:
#         answer1 = int(first_number)
#     second_number = input("Second number: ")
#     try:
#         int(second_number)
#     except ValueError:
#         print("please enter numble, not word")
#     else:
#         answer2 = int(second_number)
#         print(answer1 + answer2)fil
file1 = "cats.txt"
file2 = "dogs.txt"
try:
    with open(file1) as cats:
        ca = cats.read()
except FileExistsError:
    print("can not find file " + file1 + " !")
else:
    print(ca)

with open(file2) as dogs:
    do = dogs.read()
    print(do)
