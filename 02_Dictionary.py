# work with key and value (create entities)

person = {'name' : 'Lea', 'age' : 21, 'e-mail' : 'lea@email.com'}

print(person)
print(person['name'])
print(person['age'])
print(person['e-mail'])

person['course'] = 'programming'

print(person)

person['age'] = 25

print(person)

del person['course']

print(person)

languages = {
    'lea' : 'python',
    'sara' : 'c',
    'eddie' : 'java',
    'phil' : 'python'
}

print(languages)

print("The programming language used by Lea is: "  + languages['lea'].title())

      