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

# User Information
def user_info():
    """
    Ask the user for their name to start order process.
    """
    print("Let's start brewing!\n")
    print("First provide us with your name")


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
                "Please ensure that your name is more than two letters long")
    
    except ValueError as e:
        print(f"{e} \nPlease enter your name again")
        return False
    
    return True

# Formatting
def end_section():
    “”"
    Print ### to end each section.
    “”"
    print(” “)
    print(“# “* 25)
    print(” “)


# Main
def main():
    """
    Run the main code functions
    """
    # Welcome Message
    welcome_message()
    end_section()
    
main() 