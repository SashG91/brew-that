import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime


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
    order_invoice
        Calculate and return the total from the order based on the order list
    """

    def __init__(self):
        """
        Instance attributes
        """
        self.order = []
        self.user = self.user_info()
        self.total_price = 0

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

        end_section()

        # Validate customer order
        while drink_choice not in ("1", "2", "3", "4", "5", "6"):
            print("Which coffee would you like to order?")
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

        return drink_choice

    def repeat_order(self):
        """
        Allow the customer to add to their order.
        """
        print("Would you like to add anything else?")
        print("1 - Yes")
        print("2 - No\n")
        repeat_order = input("Enter your answer here\n").strip()
        end_section()

        if repeat_order == "1":
            self.coffee_choice()

        if repeat_order == "2":
            print("\nLet's start brewing!\n")
            self.order_successful()

        if repeat_order not in ("1", "2"):
            print("Please enter number 1 or 2 to proceed")
            self.repeat_order()

    def order_successful(self):
        """
        Add sales count to the worksheet.
        Notifies user that their order is complete.
        """

        # 1. get counts of things order
        capps_no = self.order.count("1")
        lattes_no = self.order.count("2")
        americ_no = self.order.count("3")
        vanil_latte_no = self.order.count("4")
        car_macch_no = self.order.count("5")
        ceylon_tea_no = self.order.count("6")

        now = datetime.now() # current date and time
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")	
        worksheet_to_update = SHEET.worksheet("sales")
        worksheet_to_update.append_row([
            capps_no,
            lattes_no,
            americ_no,
            vanil_latte_no,
            car_macch_no,
            ceylon_tea_no,
            date_time
        ])

        print("Your order is successful!")
        self.order_invoice(capps_no, lattes_no, americ_no,
                           vanil_latte_no, car_macch_no, ceylon_tea_no)

    def order_invoice(
            self,
            capps_no,
            lattes_no,
            americ_no,
            vanil_latte_no,
            car_macch_no,
            ceylon_tea_no):
        """
        Calculate and return the total from the order based on the order list
        """

        if capps_no > 0:
            print(f"{capps_no} x cappucino = {format_currency(1.50 * capps_no)}")
        if lattes_no > 0:
            print(f"{lattes_no} x latte = ${2.75 * lattes_no}")
        if americ_no > 0:
            print(f"{americ_no} x latte = ${1.25 * americ_no}")
        if vanil_latte_no > 0:
            print(f"{vanil_latte_no} x latte = ${2.50 * vanil_latte_no}")
        if car_macch_no > 0:
            print(f"{car_macch_no} x latte = ${2.00 * car_macch_no}")
        if ceylon_tea_no > 0:
            print(f"{ceylon_tea_no} x latte = ${1.00 * ceylon_tea_no}")

        total_cost = (1.50 * capps_no) + (2.75 * lattes_no) + \
                     (1.25 * americ_no) + \
                     (2.50 * vanil_latte_no) + \
                     (2.00 * car_macch_no) + (1.00 * ceylon_tea_no)

        print(f"Total cost: {format_currency(total_cost)}")


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
    print("# " * 25)
    print(" ")

# Main


def format_currency(amount):
    return "${:,.2f}".format(amount)


def main():
    """
    Run the main code functions
    """
    # Welcome Message
    welcome_message()
    end_section()
    coffee = Customer()


main()
