# function to calcalate simple interest


def calc_simple_interest(principal, rate, time):
    """
    Calculate simple interest.

    Parameters:
    principal (float): The principal amount.
    rate (float): The annual interest rate (in percentage).
    time (float): The time in years.

    Returns:
    float: The calculated simple interest.
    """
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# take user input for principal, rate, and time
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in percentage): "))
time = float(input("Enter the time in years: "))

# function call to calculate simple interest


simple_interest = calc_simple_interest(principal, rate, time)

# display the simple interest
print(f"The simple interest for principal amount {principal}, rate {rate}%, and time {time} years is: {simple_interest}")