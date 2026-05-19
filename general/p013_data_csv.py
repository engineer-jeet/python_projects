import csv

# with open("emp.csv", 'a', newline="") as f:
#     w = csv.writer(f)
#     w.writerow(["E_NO", "E_Name", "E_SAL", "E_ADDR"])

#     while True:
#         E_NO = int(input("Enter employee number: "))
#         E_Name = input("Enter employee name: ")
#         E_Sal = int(input("Enter the salary: "))
#         E_Addr = input("Enter the address: ")
#         w.writerow([E_NO, E_Name, E_Sal, E_Addr])

#         option = input("Do you want to enter another row [Yes|No]? ")
#         if option.lower() == "no":
#             break
    
print()

with open("emp.csv") as f:
    r = csv.reader(f)
    data = list(r)

for row in data:
    for column in row:
        print(column,'\t',end="")
    
print()



