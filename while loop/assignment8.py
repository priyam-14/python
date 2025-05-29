numbers = [1, 2, 3, 4]
reversed_list = []
index = len(numbers) - 1  
while index >= 0:
    reversed_list.append(numbers[index])
    index = index - 1
print("Reversed list:", reversed_list)
