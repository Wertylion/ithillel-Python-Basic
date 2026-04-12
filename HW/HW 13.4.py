# создать телефонную книгу с сохранением в файл txt
# добавление
# изменение контакта
# удаление
# поиск по имени

print("1. Add contact")
print("2. Change contact")
print("3. Delete contact")
print("4. Search contact")
print("5. Exit")

while True:
    try:
        choice = int(input("Enter your choice: "))
        break
    except ValueError:
        print("Invalid choice, try again")


if choice == 1:
    while True:
        name = input("Enter name: ").title()
        if name.isalpha():
            break
        else:
            print("Name must contain only letters")

    while True:
        surname = input("Enter surname: ").title()
        if surname.isalpha():
            break
        else:
            print("Surname must contain only letters")

    while True:
        try:
            age = int(input("Enter age: "))
            break
        except ValueError:
            print("Invalid age, enter a number")

    while True:
        phone = input("Enter phone: ")
        clean_phone = phone.replace("+", "").replace("-", "").replace(" ", "")
        if clean_phone.isdigit():
            break
        else:
            print("Phone must contain only digits, +, - or spaces")

    contact = {
        "name": name,
        "surname": surname,
        "age": age,
        "phone": phone
    }

    text = f"{contact['name']},{contact['surname']},{contact['age']},{contact['phone']}"
    with open('contact book.txt', 'a', encoding='utf-8') as file:
        file.write(text + '\n')

    print("Contact added successfully")


elif choice == 2:
    while True:
        name_contact_change = input("Enter name: ").title()
        if name_contact_change.isalpha():
            break
        else:
            print("Name must contain only letters")

    while True:
        surname_contact_change = input("Enter surname: ").title()
        if surname_contact_change.isalpha():
            break
        else:
            print("Surname must contain only letters")

    try:
        with open('contact book.txt', 'r', encoding='utf-8') as file:
            contacts = file.readlines()
    except FileNotFoundError:
        contacts = []

    updated_lines = []
    found = False

    for line in contacts:
        parts = line.strip().split(',')

        if len(parts) < 4:
            continue

        name = parts[0]
        surname = parts[1]
        age = parts[2]
        phone = parts[3]

        if name == name_contact_change and surname == surname_contact_change:
            found = True

            while True:
                new_phone = input("Enter new phone: ")
                clean_phone = new_phone.replace("+", "").replace("-", "").replace(" ", "")
                if clean_phone.isdigit():
                    break
                else:
                    print("Phone must contain only digits, +, - or spaces")

            new_line = f"{name},{surname},{age},{new_phone}\n"
            updated_lines.append(new_line)
        else:
            updated_lines.append(line)

    if not found:
        print("Contact does not exist")
    else:
        with open('contact book.txt', 'w', encoding='utf-8') as file:
            file.writelines(updated_lines)
        print("Contact changed")


elif choice == 3:
    while True:
        name_contact_delete = input("Enter name: ").title()
        if name_contact_delete.isalpha():
            break
        else:
            print("Name must contain only letters")

    while True:
        surname_contact_delete = input("Enter surname: ").title()
        if surname_contact_delete.isalpha():
            break
        else:
            print("Surname must contain only letters")

    try:
        with open('contact book.txt', 'r', encoding='utf-8') as file:
            contacts = file.readlines()
    except FileNotFoundError:
        contacts = []

    updated_lines = []
    found = False

    for line in contacts:
        parts = line.strip().split(',')

        if len(parts) < 4:
            continue

        name = parts[0]
        surname = parts[1]

        if name == name_contact_delete and surname == surname_contact_delete:
            found = True
            continue

        updated_lines.append(line)

    if not found:
        print("Contact does not exist")
    else:
        with open('contact book.txt', 'w', encoding='utf-8') as file:
            file.writelines(updated_lines)
        print("Contact deleted")


elif choice == 4:
    while True:
        name_contact_search = input("Enter name: ").title()
        if name_contact_search.isalpha():
            break
        else:
            print("Name must contain only letters")

    while True:
        surname_contact_search = input("Enter surname: ").title()
        if surname_contact_search.isalpha():
            break
        else:
            print("Surname must contain only letters")

    try:
        with open('contact book.txt', 'r', encoding='utf-8') as file:
            contacts = file.readlines()
    except FileNotFoundError:
        contacts = []

    found = False

    for line in contacts:
        parts = line.strip().split(',')

        if len(parts) < 4:
            continue

        name = parts[0]
        surname = parts[1]
        age = parts[2]
        phone = parts[3]

        if name == name_contact_search and surname == surname_contact_search:
            found = True
            parsed_line = f"{name},{surname},{age},{phone}"
            print(parsed_line)

    if not found:
        print("Contact does not exist")


elif choice == 5:
    print("Goodbye")

else:
    print("Wrong choice")