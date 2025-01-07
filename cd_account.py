"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account
def create_cd_account(balance, interest_rate, periods):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    cd = account(balance)
    # Calculate interest earned
    interest_earned = balance * (interest_rate / 100) * periods
    # Update the CD account balance by adding the interest earned
    updated_balance = balance + interest_earned
    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    cd.update_balance(updated_balance)
    # Return the updated balance and interest earned.
    return updated_balance, interest_earned
    
    