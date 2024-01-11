#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import string
import re


class PasswordGenerator:
    @staticmethod
    def generate_password(length=20, include_uppercase=True, include_lowercase=True,
                          include_numbers=True, include_special_chars=True):
        characters = ""
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_lowercase:
            characters += string.ascii_lowercase
        if include_numbers:
            characters += string.digits
        if include_special_chars:
            characters += string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))


class PasswordEvaluator:
    @staticmethod
    def evaluate_strength(password):
        length_error = len(password) < 8
        digit_error = not re.search(r"\d", password)
        uppercase_error = not re.search(r"[A-Z]", password)
        lowercase_error = not re.search(r"[a-z]", password)
        special_char_error = not re.search(r"\W", password)

        errors = []
        if length_error:
            errors.append("Password should be at least 8 characters long.")
        if digit_error:
            errors.append("Password should contain at least one digit.")
        if uppercase_error:
            errors.append("Password should contain at least one uppercase letter.")
        if lowercase_error:
            errors.append("Password should contain at least one lowercase letter.")
        if special_char_error:
            errors.append("Password should contain at least one special character.")

        if not errors:
            return "Password is strong and meets the complexity requirements."
        else:
            return "Password is weak. Please consider the following:\n" + "\n".join(errors)


class PasswordTool:
    def __init__(self, generator, evaluator):
        self.generator = generator
        self.evaluator = evaluator

    def generate_and_evaluate_password(self, length, include_upper, include_lower, include_digits, include_special):
        new_password = self.generator.generate_password(
            length, include_upper, include_lower, include_digits, include_special
        )
        return new_password, self.evaluator.evaluate_strength(new_password)

    def user_interface(self):
        print("Welcome to the Password Tool!")
        length = int(input("Enter the desired password length: "))
        include_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        include_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
        include_digits = input("Include digits? (y/n): ").lower() == 'y'
        include_special = input("Include special characters? (y/n): ").lower() == 'y'

        new_password, strength_evaluation = self.generate_and_evaluate_password(
            length, include_upper, include_lower, include_digits, include_special
        )

        print(f"Generated Password: {new_password}")
        print(strength_evaluation)


def main():
    password_tool = PasswordTool(PasswordGenerator(), PasswordEvaluator())
    password_tool.user_interface()


if __name__ == "__main__":
    main()
