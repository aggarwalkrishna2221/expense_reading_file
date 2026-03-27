try:
    file_handle = open("expenses.txt" , "r")
except:
    print("File name is incorrect or file does not exist")

count = dict()
total = 0

for lines in file_handle:
    words = lines.split(",")
    place = words[0]
    expense = words[1]
    total = total + int(expense)
    count[place] = count.get(place,0) + int(expense)

lst = list()

for key, value in count.items():
    newt = (value,key)
    lst.append(newt)

lst = sorted(lst, reverse=True)

print("-----Expense Report-----")
print("Total Spent:- ", total)

print("Category Breakdown (highest to lowest) \n")
i = 1
for val, key in lst:
    print(str(i) + "." + key + "-" + str(val))
    i = i+1


