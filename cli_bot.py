"""
Console Assistant Bot

This is a simple console-based assistant bot that allows users to manage contacts. 
Users can add, change, and view contact details.

Usage:
- 'hello': Greet the bot.
- 'add [name] [phone]': Add a new contact with a name and phone number.
- 'change [name] [new_phone]': Change the phone number for an existing contact.
- 'phone [name]': View the phone number for a specific contact.
- 'all': View all contacts and their phone numbers.
- 'close' or 'exit': Exit the bot.

Instructions:
- Enter commands as described above to interact with the bot.
- The bot will provide feedback and instructions based on the commands.

"""


def parse_input(user_input: str):
    """
    Parses the user input to extract the command and arguments.

    Args:
    user_input (str): The user's input.

    Returns:
    tuple: A tuple containing the command (str) and a list of arguments (list of str).
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    """
    Adds a contact to the contacts dictionary.

    Args:
    args (list of str): A list containing the name (str) and phone number (str).
    contacts (dict): A dictionary containing contacts where keys are names and 
                     values are phone numbers.

    Returns:
    str: A message confirming the addition of the contact or an error message.
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    """
    Changes the phone number for an existing contact.

    Args:
    args (list of str): A list containing the name (str) and the new phone number (str).
    contacts (dict): A dictionary containing contacts where keys are names and
                     values are phone numbers.

    Returns:
    str: A message confirming the contact update or an error message.
    """
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."

    return f"Contact '{name}' not found."


def show_phone(args, contacts):
    """
    Shows the phone number for a specific contact.

    Args:
    args (list of str): A list containing the name (str) of the contact.
    contacts (dict): A dictionary containing contacts where keys are names and
                     values are phone numbers.

    Returns:
    str: The phone number of the contact or an error message.
    """
    name = args[0]
    if name in contacts:
        return contacts[name]

    return f"Contact '{name}' not found."


def show_all(contacts):
    """
    Shows all contacts and their phone numbers.

    Args:
    contacts (dict): A dictionary containing contacts where keys are names and
                     values are phone numbers.

    Returns:
    str: A formatted string containing all contacts and phone numbers or
         a message if no contacts are found.
    """
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

    return "No contacts found."


def main():
    """
    Main function for the console assistant bot.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
