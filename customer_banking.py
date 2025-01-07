# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    print("Savings Account")
    balance = float(input("Enter current balance for savings account: "))
    interest_rate = float(input("Enter annual interest rate (in %): "))
    periods = int(input("Enter number of periods (years): "))
# Call the create_savings_account function and pass the variables from the user.
    savings_updated_balance, savings_interest_earned = create_savings_account(balance, interest_rate, periods)
# Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Savings Account - Updated Balance: {savings_updated_balance:.2f}, Interest Earned: {savings_interest_earned:.2f}")
# Prompt the user to set the CD balance, interest rate, and months for the CD account.
    print("\nCertificate of Deposit (CD) Account")
    balance = float(input("Enter current balance for CD account: "))
    interest_rate = float(input("Enter annual interest rate (in %): "))
    periods = int(input("Enter number of periods (years): "))
# Call the create_cd_account function and pass the variables from the user.
    cd_updated_balance, cd_interest_earned = create_cd_account(balance, interest_rate, periods)
# Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"CD Account - Updated Balance: {cd_updated_balance:.2f}, Interest Earned: {cd_interest_earned:.2f}")

if __name__ == "__main__":
    # Call the main function.
    main()

    