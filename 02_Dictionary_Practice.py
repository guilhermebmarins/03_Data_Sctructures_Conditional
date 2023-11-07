languages = {}

c = 0
java = 0
python = 0

for i in range(0, 3):
    name = input('Whats your name: ')
    print("What is yours favorite computer language?")
    print("(1): C++")
    print("(2): Java")
    print("(3): Python")
    language = int(input("Choose the number option: "))

    if language == 1:
        languages[name] = language
        c += 1
    elif language == 2:
        languages[name] = language
        java += 1
    elif language == 3:
        languages[name] = language
        python += 1

print(languages)
print(c)
print(java)
print(python)