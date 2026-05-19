from handlers import (
    add_contact,
    change_contact,
    parse_input,
    contact_exists,
    show_phone,
    show_all,
)
from colorama import Fore


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        result = None
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            result = "How can I help you?"
        elif command == "add":
            result = add_contact(args, contacts)
        elif command == "change":
            result = change_contact(args, contacts)
        elif command == "phone":
            result = show_phone(args, contacts)
        elif command == "all":
            result = show_all(contacts)
        else:
            result = "Error: Invalid command."

        if result:
            if result.startswith("Error"):
                print(f"{Fore.RED}{result}{Fore.RESET}")
            else:
                print(result)


if __name__ == "__main__":
    main()
