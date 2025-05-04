# Day 5 - ATM Menu Simulator
# Topic: Control Flow (if, loops, match-case), f-string and docstring.


# This Function to represent introduction of this assignment / Project. Starting with a little welcome message.
def show_intro():
    print("🔹 Welcome to Day 5 of Python 30-Day Challenge!")
    print("🔹 Topic: Control Flow, I/O - if, loops, match-case, f-strings and docstrings")
    print("🏧 Building an ATM Menu Simulator with interactive loop\n")

# This is a global-level declaration of account's initial balance of the user. 
balance = 1000.0


# This function displays the menu to user, represents what actions a user can perform on his / her account.
def display_menu():
    print("\n🏧 ATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

# This function displays current balance of user with two floating values.
def check_balance():
    """
    By choosing this option you are checking your account balance...
    """
    print(f"💰 Current Balance: ₹{balance:.2f}")

# This function deposits amount in users account by doing validation of amount.
def deposit():
    """
    By choosing this option you are depositing / adding amount into your account...
    """
    # This is users account initial  balance.
    global balance

    # Here this asks user for amount as input to deposit and converts it into float
    try:
        # asks user for amount to input
        amount_input = input("Enter amount to deposit: ₹")
        
        # converts the integer into float.
        deposit_amt = float(amount_input)

        # If the amount is greater than 0, then only it deposits the amount.
        if deposit_amt > 0:

            # It updates the balance by incrementing the balance with deposited amount.
            balance += deposit_amt
            # After updating the balance it displays the deposited amount.
            print(f"✅ ₹{deposit_amt:.2f} deposited. New Balance: ₹{balance:.2f}")

            # If user wants to deposit -ve amount it displays this msg.
        else:
            print("❌ Enter a positive amount.")

            # If user enters any value other than number this msg will be displayed.
    except ValueError:
        print("❌ Invalid input. Please enter a number.")

# This function withdraws amount from the user account by performing validation of amount.
def withdraw():
    """
    By choosing this option you are withdrawing / deducing amount from your account...
    """

    # This is users account initial  balance.
    global balance

    # Here this asks user for amount as input to withdraw and converts it into float.
    try:
        # asks user for amount to input
        raw_withdraw = input("Enter amount to withdraw: ₹")
        
        # converts the integer into float.
        withdraw_amount = float(raw_withdraw)

        # If the withdrawn amount is negative, it alerts the user to enter +ve amount.
        if withdraw_amount <= 0:
            print("❌ Enter a positive amount.")

        # If the withdrawn amount is greater than the balance it displays insufficient funds.
        elif withdraw_amount > balance:
            print("❌ Insufficient funds.")
        # Else it cuts down the amount from balance, then amount was withdrawn.
        else:
            balance -= withdraw_amount
            print(f"✅ ₹{withdraw_amount:.2f} withdrawn. Remaining Balance: ₹{balance:.2f}")
        # If user enters invalid option 
    except ValueError:
        print("❌ Invalid input. Please enter a number.")

# this is a main function
def main():

    # calls show_intro() to display the introduction and welcome msg.
    show_intro()
    
    # This loop runs until the user chooses the exit option
    while True:

        #  this calls display_menu() function and displays menu for user choice.
        display_menu()

        # Takes user's choice as an input and removes extra spaces by stripping.
        user_choice = input("🔢 Choose an option (1-4): ").strip()

        # Using match-case to choose options
        match user_choice:
            # If user chooses option-1 calls check_balance() to check balance in user's account
            case "1":
                print(check_balance.__doc__)
                check_balance()

                # If user chooses option-2 calls deposit() to deposit / add amount into user's account
            case "2":
                print(deposit.__doc__)
                deposit()

                # If user chooses option-3 calls withdraw() to withdraw / deduce amount from user's account
            case "3":
                print(withdraw.__doc__)
                withdraw()

                # If user chooses option-4 the while loop exits by breaking
            case "4":
                print("👋 Thank you for using the ATM Simulator!")
                break

                # this is default condn of match-case, if user enters invalid input this will execute
            case _:  
                print("❌ Invalid choice. Please select a valid option.")  

# calls main() to start execution of program
if __name__ == "__main__":
    main()
