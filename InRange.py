"""
10/10/2023
InRange
"""

"""asks user to enter the following numbers for lists"""
first_num= int(input("type a number from where you want your first list to begin: "))
second_num= int(input("type a number at which  you want your first list to end: "))
third_num= int(input("type a number from where you want your second list to begin: "))
fourth_num= int(input("type a number at which you want your second list to end: "))
fifth_num= int(input("type a number that you want to find:"))
first_list = list(range(first_num, second_num))   #declares the list
second_list = list(range(third_num, fourth_num))

if fifth_num in first_list and second_list: #finds if the last number exists in both list
    print("True")
else:
    print("False")  #prints the final answer