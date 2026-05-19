import functools


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def contact_exists(name, contacts):
    return name in contacts


def is_valid_phone(phone_input):
    valid = ""
    for char in phone_input:
        if char.isdigit():
            valid += char

    if len(valid) == 10:
        return valid
    return None


def format_phone(phone):
    return f"+38({phone[0:3]}){phone[3:6]}-{phone[6:8]}-{phone[8:10]}"


def input_error(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Error: Enter name and phone please."
        except KeyError:
            return "Error: Contact hasnt been found."
        except IndexError:
            return "Error: Enter user name."

    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args
    clean_phone = is_valid_phone(phone)

    if not clean_phone:
        return "Error: Phone number must contain exactly 10 digits."

    if name in contacts:
        choice = (
            input(f"Contact {name} already exists. Overwrite? (y/n): ").strip().lower()
        )
        if choice not in ["y", "yes"]:
            return "Canceled."
    contacts[name] = clean_phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    clean_phone = is_valid_phone(phone)

    if not clean_phone:
        return "Error: Phone number must contain exactly 10 digits."

    if name in contacts:
        contacts[name] = clean_phone
        return f"Contact {name} updated."
    else:
        raise KeyError


@input_error
def show_phone(args, contacts):
    name = args[0]
    return format_phone(contacts[name])


@input_error
def show_all(contacts):
    if not contacts:
        return "Contact list is empty."

    contact_list = [
        f"{name}: {format_phone(phone)}" for name, phone in contacts.items()
    ]

    return "\n".join(contact_list)
