import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('brew_that')

sales = SHEET.worksheet('sales')
data = sales.get_all_values()

# Welcome Message
def welcome_message():
    """
    Welcome the customer to BrewThat.
    Service offering.
    """
    print("Welcome to BrewThat!\n")
    print("A mobile pitstop that fuels cyclists on their socials.")

class Customer:
    """
    A class used to represent a Customer
    
    Attributes
    -----------
    name = str
        the customer's first name
    order = list
        nested list with customer's order [name, value, quantity]
   
    Methods
    --------
    user_info
        Return the customer full name
    coffee_choice
        Present user with a list of drink options
    repeat_order
        Provide the user with an opportunity to add a drink to their order
    order_successful
        Provide a user with a message to show order capture success
    customer_total
        Calculate and return the total from the order based on the order list
    """

    def __init__(self):
        """
        Instance attributes
        """
        self.order = []
        self.user = self.user_info()

    def user_info(self):
        """
        Ask the user for their name to start order process.
        """
        print("Let's start brewing!\n")
        print("First provide us with your name")
        while True:
            name = input("Enter your name here:\n").capitalize().strip()
                
            end_section()

            if validate_username(name):
                print(f"Hello {name}!\n")
                self.coffee_choice()
                break
            
            return name  
    
    def coffee_choice(self):
        """
        Display coffee menu and ask user for their choice.
        """
        print("Which coffee would you like to order?")
        print("1 - Cappuccino")
        print("2 - Latte")
        print("3 - Americano")
        print("4 - Vanilla Latte")
        print("5 - Caramel Macchiato")
        print("6 - Ceylon tea")
        drink_choice = input("Enter your answer here:\n").strip()

        print("\nYour order has been generated")
        end_section()

        # Validate customer order
        while drink_choice not in ("1", "2", "3"):
            print("1 - Cappuccino")
            print("2 - Latte")
            print("3 - Americano")
            print("4 - Vanilla Latte")
            print("5 - Caramel Macchiato")
            print("6 - Ceylon tea")
            drink_choice = input("Enter your answer here:\n").strip()

            end_section()

        self.order.append(drink_choice)

        self.repeat_order()

    def repeat_order(self):
        """
        Allow the customer to add to their order.
        """
        print("Would you like to add anything else?")
        print("1 - Yes")
        print("2 - No\n")
        repeat_order = input("Enter your answer here\n").strip()

        if repeat_order == "1":
            self.coffee_choice()

        elif repeat_order == "2":
            print("\nLet's start brewing!\n")
            self.order_successful()

    def order_successful(self):
        """
        Add sales count to the worksheet.
        Notifies user that their order is complete.
        """

        print("Your order is on its way!")
        # Same function as used on the love_sandwiches walk through project
        # by Code Institute
        worksheet_to_update = SHEET.worksheet("sales")
        worksheet_to_update.append_row(data)

        # 1. get counts of things order
        cappuccinos_ordered = self.order.count("1")
        latte_ordered = self.order.count("2")
     
        # 2. get total price
        worksheet_to_update = SHEET.worksheet("prices")
        cappuccino_price = worksheet_to_update.acell('B1').value
        # 3 write order to spread sheet
        # 4 print order to terminal
        

        print("Your order is successful!")


def validate_username(name):
    """
    Check customers name for length, numbers and characters.
    """
    try:
        if name.isnumeric():
            raise ValueError(
                "Enter your name with letters only please.")
        
        if not name.isalpha():
            raise ValueError(
                "Enter your name with letters only please.")

        if len(name) < 2:
            raise ValueError(
                "Please ensure that your name is more than two letters long.")
    
    except ValueError as e:
        print(f"{e} \nPlease enter your name again.")
        return False
    
    return True

# Formatting
def end_section():
    """
    Print ### to end each section.
    """
    print(" ")
    print("# "* 25)
    print(" ")

# Main
def main():
    """
    Run the main code functions
    """
    # Welcome Message
    welcome_message()
    end_section()
    coffee = Customer()
main()