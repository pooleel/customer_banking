"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, periods):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        periods (int): The number of periods to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    savings = account(balance)
     # Calculate interest earned
    interest_earned = balance * (interest_rate / 100) * periods
    # Update the savings account balance by adding the interest earned
    updated_balance = balance + interest_earned
    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    savings.update_balance(updated_balance)
    # Return the updated balance and interest earned.
    return updated_balance, interest_earned

   
     