import random
accounts = {}

while True:

    print("\n--- Main Menu ---")
    print("1 I have a bank account")
    print("2 I want to create bank account")
    print("0 Exit")


    while True:
        try:
            choice = int(input("Enter your choice: "))
            break
        except ValueError:
            print("Enter a valid choice")


    if choice == 1:
        print("\n--- Existing Account ---")
        while True:
            try:
                bank_id = int(input("Enter your bank account number: "))
                break
            except ValueError:
                print("Enter a valid choice")
        found = False
        try:
            with open('bank accounts.txt', 'r', encoding='utf-8') as file:
                users = file.readlines()
            current_account = None
            for line in users:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if not parts[0]:
                    continue

                if bank_id == int(parts[0]):
                    current_account = {
                        "bank_id": parts[0],
                        "name": parts[1],
                        "card_number": parts[2],
                        "balance": float(parts[3])
                    }
                    found = True
            if not found:
                print("Enter a valid bank account number")
                continue
            print(f'\n---Welcome to my bank account {current_account["bank_id"]}--- ---')
            print(f"Your account number is {current_account['name']}")
            print(f"Your CARD number is {current_account['card_number']}")

        except FileNotFoundError:
            print("No accounts file found")
            continue


        while True:
            print("\n1. Check your current Balance")
            print("2. Withdrawal cash")
            print("3. Replenishment cash")
            print("4. Check your history transactions")
            print("0 Back")

            try:
                sub_choice = int(input("Enter your choice: "))
            except ValueError:
                print("Enter a valid choice")
                continue

            if sub_choice == 1:
                print(f"\n---Balance: {current_account['balance']} ---")


            elif sub_choice == 2:
                print(f"\n---Your Balance: {current_account['balance']} ---")

                name_withdrawal = input("Enter your name: ")
                if not name_withdrawal.isalpha():
                    print("Enter only letters")
                    continue

                try:
                    withdrawal = float(input("Enter your withdrawal amount: "))
                except ValueError:
                    print("Enter a valid amount")
                    continue

                if withdrawal <= 0:
                    print("Enter a valid amount")
                    continue

                if withdrawal > current_account['balance']:
                    print("Insufficient funds in the account")
                    continue

                current_account['balance'] -= withdrawal

                history_transaction = f"withdrawal {withdrawal}"

                history = f"{current_account["bank_id"]},{current_account["name"]},{current_account["card_number"]},{current_account["balance"]},{history_transaction},{name_withdrawal}"
                with open('bank accounts.txt', 'a', encoding='utf-8') as file:
                    file.write(history + '\n')

                    print(f"\n---Your Balance: {current_account['balance']} ---")

            elif sub_choice == 3:
                print(f"\n---Your Balance: {current_account['balance']} ---")

                name_replenishment = input("Enter your name: ")
                if not name_replenishment.isalpha():
                    print("Enter only letters")
                    continue

                try:
                    replenishment = float(input("Enter your replenishment amount: "))
                except ValueError:
                    print("Enter a valid amount")
                    continue
                if replenishment <= 0:
                    print("Enter a valid amount")
                    continue
                else:
                    print("Enter a valid amount")

                current_account['balance'] += replenishment

                history_transaction = f"replenishment {replenishment}"

                history = f"{current_account["bank_id"]},{current_account["name"]},{current_account["card_number"]},{current_account["balance"]},{history_transaction},{name_replenishment}"
                with open('bank accounts.txt', 'a', encoding='utf-8') as file:
                    file.write(history + '\n')

                    print(f"\n---Your Balance: {current_account['balance']} ---")





            elif sub_choice == 4:
                print("\n--- Transaction History ---")
                try:
                    with open('bank accounts.txt', 'r', encoding='utf-8') as file:
                        found_history = False
                        for line in file:
                            line = line.strip()
                            if not line:
                                continue
                            parts = line.split(',')
                            if not parts[0]:
                                continue
                            if int(parts[0]) == int(current_account["bank_id"]) and len(parts) > 4:
                                print(f"Type: {parts[4]}, Name: {parts[5]}, Balance: {parts[3]}")
                                found_history = True
                        if not found_history:
                            print("No transaction history")


                except FileNotFoundError:

                    print("No transaction history")



            elif sub_choice == 0:
                break
            else:
                print("Enter a valid choice")




    elif choice == 2:
        print("\n--- New Account ---")

        new_bank_id = int(random.randint(10000, 99999))
        print(f"\nYour new account number is {new_bank_id}")

        random_number_cards = int(random.randint(1000000000000000, 9999999999999999))

        number_cards = '-'.join(
            str(random_number_cards)[i:i + 4]
            for i in range(0, len(str(random_number_cards)), 4))


        while True:
            try:
                name = str(input("\nEnter your name: ")).title()
                break
            except ValueError:
                print("Enter a valid name")

        balance = 0

        accounts = {
            "bank_id": new_bank_id,
            "name": name,
            "number_cards": number_cards,
            "balance": balance
        }

        text = f"{accounts["bank_id"]},{accounts["name"]}, {accounts["number_cards"]}, {accounts["balance"]}"
        with open('bank accounts.txt', 'a', encoding='utf-8') as file:
            file.write(text + '\n')

        print(f"\nYour new card number is {number_cards}")
        print("\nYour account balance is " + str(balance))
        print("\n--- Account Created ---")


    elif choice == 0:
        break
