from typing import List

class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(balance)
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # Validate that both account numbers exist
        if not (1 <= account1 <= self.n and 1 <= account2 <= self.n):
            return False
        # Validate that the source account has enough money
        if self.balance[account1 - 1] < money:
            return False
        
        # Perform the transaction using 0-based indexing
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True
        

    def deposit(self, account: int, money: int) -> bool:
        # Validate that the account number exists
        if not (1 <= account <= self.n):
            return False
        
        # Perform the deposit
        self.balance[account - 1] += money
        return True
        

    def withdraw(self, account: int, money: int) -> bool:
        # Validate that the account exists and has enough money
        if not (1 <= account <= self.n) or self.balance[account - 1] < money:
            return False
        
        # Perform the withdrawal
        self.balance[account - 1] -= money
        return True
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)