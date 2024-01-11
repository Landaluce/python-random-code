#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    pass


if __name__ == "__main__":
    main()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


class Account:
    def __init__(self):
        import uuid
        self.account_number = str(uuid.uuid4())
        self.balance = 0.0

    def get_balance(self):
        return self.balance

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self):
        account = Account()
        account.deposit(random.uniform(1.00, 10000000000.00))
        self.accounts.append(account)

    def get_account(self, account_number: str):
        for account in self.accounts:
            if account.account_number == account_number:
                return account

    def close_account(self, account_number: str):
        for i in range(0, len(self.accounts)-1):
            if self.accounts[i].account_number == account_number:
                if i == len(self.accounts)-1:
                    self.accounts = self.accounts[0:-1]
                else:
                    while i < len(self.accounts)-2:
                        self.accounts[i] = self.accounts[i+1]

    def display_accounts(self):
        count = 0
        for account in self.accounts:
            print(str(count) + ": " + account.account_number, "$" + str(account.balance))
            count += 1


def main():
    bank = Bank()
    bank.create_account()
    bank.display_accounts()


if __name__ == "__main__":
    main()
