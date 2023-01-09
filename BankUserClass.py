class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0.0

    def show_balance(self):
        """This function displays the account balance of the instance user"""
        print(f"{self.name} has and account balance of: {self.balance}")

    def withdraw(self, amount):
        """This function will decrease the balance by given amount

        Args:
            amount (float): The amount to be deducted from the balance
        """
        self.balance -= amount

    def deposit(self, amount):
        """This function will decrease the balance by given amount
        Args:
            amount (float): The amount to be deducted from the balance
        """
        self.balance += amount

    def transfer_money(self, otheruser, amount):
        """ This function transfers money to another User if correct PIN is given for the transferring User. Also return a Boolean value of True. 
            If an incorrect PIN is given, return a Boolean value of False. It will also adjust the balance for both users 
        Args:
            otheruser (BankUser): The BankUser object to transfer the money to 
            amount (float): The amount to add to otheruser.balance and deduct from self.balance

        Returns:
            Boolean: True if successful False otherwise 
        """
        print(f"\nYou are transfering ${amount} to {otheruser.name}")
        pin = input("Authentication required\nEnter your PIN: ")
        if self.pin == pin:
            print(
                f"Transfer Authorized\nTransfering ${amount} to {otheruser.name}")
            otheruser.deposit(amount)
            self.withdraw(amount)
            return True
        else:
            print(
                f"Invalid PIN. Transaction canceled.")
            return False

    def request_money(self, otheruser, amount):
        print(
            f"\nYou are requesting ${amount} from {otheruser.name}\nUser authentication is required...")
        pin = input(f"Enter {otheruser.name}'s PIN: ")
        if pin == otheruser.pin:
            password = input("Enter your password: ")
            if password == self.password:
                print(f"Request authorized\n{otheruser.name} sent ${amount}")
                self.deposit(amount)
                otheruser.withdraw(amount)
            else:
                print(f"Invalid PIN. Transaction canceled.")
        else:
            print(
                f"Invalid PIN. Transaction canceled.")


""" Driver Code for Task 1 """
# user1 = User()
# user1.name = "Bob"
# user1.pin = '1234'
# user1.password = 'password'

# print(f"{user1.name} {user1.pin} {user1.password}")


""" Driver Code for Task 2 """

# def change_name(user, name):
#     """This function changes the user's name

#     Args:
#         user (object): instance of an object of User class
#         name (string): the name you want to change for user
#     """
#     user.name = name


# def change_pin(user, pin):
#     """This function changes the user's name

#     Args:
#         user (object): instance of an object of User class
#         pin (string): the pin you want to change for the user
#     """
#     user.pin = pin


# def change_password(user, password):
#     """This function changes the user's password

#     Args:
#         user (object): instance of an object of User class
#         password (string): the password you want to change for the user
#     """
#     user.password = password


# user1 = User()
# user1.name = "Bob"
# user1.pin = '1234'
# user1.password = 'password'

# print(f"{user1.name} {user1.pin} {user1.password}")

# change_name(user1, 'Bobby')
# change_pin(user1, '4321')
# change_password(user1, 'newpassword')

# print(f"{user1.name} {user1.pin} {user1.password}")

""" Driver Code for Task 3"""
# bnkuser1 = BankUser('Bob', '123', 'password')
# print(f"{bnkuser1.name} {bnkuser1.pin} {bnkuser1.password} {bnkuser1.balance}")

""" Driver Code for Task 4"""
# bnkuser1 = BankUser('Bob', '123', 'password')
# bnkuser1.show_balance()

# bnkuser1.deposit(1000)
# bnkuser1.show_balance()

# bnkuser1.withdraw(500)
# bnkuser1.show_balance()


""" Driver Code for Task 5"""
# Instantiate an object of the BankUser class, providing arguments for the name, pin, and password.
bankuser1 = BankUser('Bob', '1234', 'bob')

# Instantiate a second object of the BankUser class, providing different arguments.
bankuser2 = BankUser('Alice', '4321', 'alice')

# Deposit $5000 into the account of this second user using the deposit() method.
bankuser2.deposit(5000)

# Show the balance of the second user.
bankuser2.show_balance()

# Show the balance of the first user.
bankuser1.show_balance()

# Have the second user transfer $500 to the first user, using its transfer_money() method.
successful_transfer = bankuser2.transfer_money(bankuser1, 500)

# Again, show the balance of each user.
bankuser2.show_balance()
bankuser1.show_balance()

# If the money transfer was successful, now have the second user request some money from the first user, using its request_money() method.
if successful_transfer:
    bankuser2.request_money(bankuser1, 250)
    # Again, show the balance of each user.
    bankuser2.show_balance()
    bankuser1.show_balance()
else:
    pass
