info = {
    'name': 'Alice',
    'city': 'New York', 
    'hobby': 'coding'
}
for key, value in info.items():
    if len(value) > 5:
        print(value.upper())
    else:
        print(value.lower())

