#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from typing import List, Optional


class Account:
    def __init__(self):
        """
        Initialize a new account with a unique account number and a zero balance.
        """
        import uuid
        self.account_number = str(uuid.uuid4())
        self.balance = 0.0

    def get_balance(self) -> float:
        """
        Get the current balance of the account.

        Returns:
            float: The account balance.
        """
        return self.balance

    def deposit(self, amount: float) -> None:
        """
        Deposit funds into the account.

        Args:
            amount (float): The amount to deposit.
        """
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount: float) -> None:
        """
        Withdraw funds from the account.

        Args:
            amount (float): The amount to withdraw.
        """
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
            else:
                raise ValueError("Insufficient funds.")
        else:
            raise ValueError("Withdrawal amount must be positive.")


class Bank:
    def __init__(self):
        """
        Initialize a bank with an empty list of accounts.
        """
        self.accounts: List[Account] = []

    def create_account(self) -> None:
        """
        Create a new account and add it to the bank's list of accounts.
        """
        account = Account()
        initial_deposit = random.uniform(1.00, 10000000000.00)
        account.deposit(initial_deposit)
        self.accounts.append(account)

    def get_account(self, account_number: str) -> Optional[Account]:
        """
        Find and return an account by its account number.

        Args:
            account_number (str): The account number to search for.

        Returns:
            Account or None: The account object if found, else None.
        """
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def close_account(self, account_number: str) -> None:
        """
        Close an account by removing it from the bank's list of accounts.

        Args:
            account_number (str): The account number of the account to close.
        """
        for i, account in enumerate(self.accounts):
            if account.account_number == account_number:
                self.accounts.pop(i)
                return
        raise ValueError("Account not found.")

    def display_accounts(self) -> None:
        """
        Display all accounts and their balances.
        """
        if not self.accounts:
            print("No accounts found.")
            return
        print("Accounts:")
        for i, account in enumerate(self.accounts):
            print(f"{i}: {account.account_number} - ${account.balance:.2f}")


def main():
    bank = Bank()
    bank.create_account()
    bank.display_accounts()


if __name__ == "__main__":
    main()
