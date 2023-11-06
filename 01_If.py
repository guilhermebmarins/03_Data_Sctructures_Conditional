cars = ['audi', 'bmw', 'subaru', 'toyota']

for item in cars:
    if item == 'bmw': # == is comparison not a atribution
        print(item.upper())
    else:
        print(item.title())

age = 30

if age >= 18 and age <= 69:
    print('Mandatory voting')
else:
    print('Vote not mandatory')

note = 80
frequancy = 30

if note < 60 or frequancy < 25:
    print('Unapproved student')
else:
    print('Approved student')

listOfMaterials = ['pen', 'book', 'pencil', 'journal']

value = 'pen' in listOfMaterials
print(value)

value = 'E-book' not in listOfMaterials
print(value)

age = 30

if age < 14:
    print('Free entrance')
elif age < 21:
    print('Entrance costs $5.00')
else:
    print('Entrance costs $10.00')