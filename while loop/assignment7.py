user = input('Enter 5 names: ').split() #.split() breaks this string into separate words based on spaces and makes a list:
print(user)
exist_name = input('Enter the name to search: ')
for i in user:
    if i == exist_name:
        print('Name exists')
        break
else:
    print("Name doesn't exist")
