from typing import List, Optional


class Contact:
    def __init__(self, name: str, email: str, phone: str):
        """
        Initialize a Contact object.

        Args:
            name (str): The name of the contact.
            email (str): The email address of the contact.
            phone (str): The phone number of the contact.
        """
        self.name = name
        self.email = email
        self.phone = phone

    def display_contact(self) -> None:
        """
        Display the contact information.
        """
        print(f"name: {self.name}\nemail: {self.email}\nphone: {self.phone}\n")

    def to_string(self) -> str:
        """
        Convert the contact information to a string.

        Returns:
            str: A string representation of the contact.
        """
        return f"{self.name}, {self.email}, {self.phone}\n"


class ContactBook:
    def __init__(self):
        """
        Initialize a ContactBook object.
        """
        self.contact_book: List[Contact] = []

    def add_contact(self, contact: Contact) -> None:
        """
        Add a contact to the contact book.

        Args:
            contact (Contact): The contact object to add.
        """
        self.contact_book.append(contact)

    def display_contacts(self) -> None:
        """
        Display all contacts in the contact book.
        """
        for contact in self.contact_book:
            contact.display_contact()

    def to_string(self) -> str:
        """
        Convert the contact book to a string representation.

        Returns:
            str: A string containing all contacts in the contact book.
        """
        contacts = ""
        for contact in self.contact_book:
            contacts += contact.to_string()
        return contacts

    def save_contacts_to_file(self, file_name: Optional[str] = None) -> None:
        """
        Save contacts to a file.

        Args:
            file_name (str, optional): The file name to save contacts to.
                If not provided, uses the default file name specified in the class.

        Raises:
            FileNotFoundError: If the specified file is not found.
            Exception: If an error occurs while saving contacts.
        """
        if file_name is not None:
            self.file_name = file_name
        try:
            with open(self.file_name, 'w') as writer:
                for contact in self.contact_book:
                    writer.write(contact.to_string())
        except FileNotFoundError:
            print(f"File not found: {self.file_name}")
        except Exception as e:
            print(f"An error occurred while saving contacts: {e}")

    def load_contacts_from_file(self, file_name: Optional[str] = None) -> None:
        """
        Load contacts from a file.

        Args:
            file_name (str, optional): The file name to load contacts from.
                If not provided, uses the default file name specified in the class.

        Raises:
            FileNotFoundError: If the specified file is not found.
            Exception: If an error occurs while loading contacts.
        """
        if file_name is not None and file_name != self.file_name:
            self.file_name = file_name
        try:
            with open(self.file_name, 'r') as reader:
                for line in reader:
                    name, email, phone = map(str.strip, line.split(','))
                    self.contact_book.append(Contact(name, email, phone))
        except FileNotFoundError:
            print(f"File not found: {self.file_name}")
        except Exception as e:
            print(f"An error occurred while loading contacts: {e}")
