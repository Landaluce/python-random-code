#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def display_contact(self):
        print("name: " + self.name +
              "\nemail: " + self.email +
              "\nphone: " + self.phone + "\n")

    def to_string(self):
        return self.name + ", " + self.email + ", " + self.phone + "\n"


class ContactBook:
    file_name = "contacts.txt"

    def __init__(self):
        self.contact_book = []

    def add_contact(self, contact):
        self.contact_book.append(contact)

    def display_contacts(self):
        for contact in self.contact_book:
            contact.display_contact()

    def to_string(self):
        contacts = ""
        for contact in self.contact_book:
            contacts += contact.to_string()

    def save_contacts_to_file(self, file_name=None):
        if file_name is not None:
            self.file_name = file_name
        with open(self.file_name, 'w') as writer:
            for contact in self.contact_book:
                writer.write(contact.to_string())

    def load_contacts_from_file(self, file_name=None):
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
