count = 1

while count <= 5:
    print(count)
    count +=1

messange = ""
while messange != 'exit':
    print("'exit' to end")
    messange = input("Type a messange: ")
    print("(1). Your messagange is: " + messange)

flag = True
while flag:
    messange = input("(2). Type your messange: ")

    if messange == 'exit':
        flag = False

    else:
        print(messange)


flag = True
while flag:
    messange = input("(3). Type your messange: ")

    if messange == 'exit':
        break

    else:
        print(messange)


count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    else:
        print(count)

listOfMaterials = ['pen', 'book', 'pencil', 'journal']
objects = []

while listOfMaterials:
    newListOfMaterials = listOfMaterials.pop()
    objects.append(newListOfMaterials)

for teste in objects:
    print(teste.title())

print(listOfMaterials)