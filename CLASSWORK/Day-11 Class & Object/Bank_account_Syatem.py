# Create BankAccount class
class BankAccount:

    # Method to accept account details from the user
    def accept_details(self):
        self.account_number = int(input("Enter Account Number : "))
        self.customer_name = input("Enter Customer Name : ")
        self.balance = float(input("Enter Initial Balance : "))

    # Method to deposit money into the account
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposit Successful.")

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawal Successful.")
        else:
            print("Insufficient Balance.")

    # Method to display account details and current balance
    def display_balance(self):
        print("\n------ Account Details ------")
        print("Account Number :", self.account_number)
        print("Customer Name  :", self.customer_name)
        print("Current Balance:", self.balance)


# Create an object of the BankAccount class
account = BankAccount()

# Accept account details
account.accept_details()

# Accept deposit amount from the user
deposit_amount = float(input("Enter Deposit Amount : "))

# Deposit the amount
account.deposit(deposit_amount)

# Accept withdrawal amount from the user
withdraw_amount = float(input("Enter Withdrawal Amount : "))

# Withdraw the amount
account.withdraw(withdraw_amount)

# Display updated account details
account.display_balance()