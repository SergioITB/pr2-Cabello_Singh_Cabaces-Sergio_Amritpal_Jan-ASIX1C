"""
Amritpal Singh
10/10/2023
InRange
"""
first_num= int(input("type a number:"))
second_num= int(input("type a number:"))
third_num= int(input("type a number:"))
fourth_num= int(input("type a number:"))
fifth_num= int(input("type a number:"))
first_list = list(range(first_num, second_num))
second_list = list(range(third_num, fourth_num))

if fifth_num in first_list and second_list:
    print("True")
else:
    print("False")