text = 'Welcome to Python loops' 
a = {'a', 'e', 'i', 'o', 'u'}     
count = 0                                 
for letter in text:                        
    if letter in a:      
        count += 1                        
print(count)