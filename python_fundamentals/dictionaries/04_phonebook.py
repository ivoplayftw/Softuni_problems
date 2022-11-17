phonebook = {}
while True:
    person_and_num = input()
    if "-" not in person_and_num:
        break
    name, num = person_and_num.split("-")
    phonebook[name] = num

for _ in range((int(person_and_num))):
    contact = input()
    if contact in phonebook.keys():
        print(f"{contact} -> {phonebook[contact]}")
    else:
        print(f"Contact {contact} does not exist.")