number = input('Enter 5 numbers: ').split()#.split() breaks this string into separate numbers based on spaces and makes a list:
print(number)
search_number = input('Enter the number to search:')
for i in number:
    if i == search_number:
        print('Found')
        break
else:
    print('Not Found')
