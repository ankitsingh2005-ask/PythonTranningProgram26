# function to calculate the compound interest 

def calc_compound_interest(P, R, T):
    # calculate the interest 

    amount = P * (1 + R/100)**T 

    # calculate the coumpound intrest 

    compound_interest = amount - P

    # return the values 

    return compound_interest

# ---------main Program------------------

P = float(input("Enter the Principal: "))

R = float(input("Enter the annual interest in (%): "))

T = float(input("Enter the time (in Year): "))

compound_interest = calc_compound_interest(P, R, T)

print(f"Compound Interest of the amount is: {compound_interest:.2f}")