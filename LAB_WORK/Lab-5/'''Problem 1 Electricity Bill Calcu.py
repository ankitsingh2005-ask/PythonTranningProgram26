'''Problem 1: Electricity Bill Calculator
Write a Python program that calculates the electricity bill based on the following conditions:
Units Rate per Unit
First 100 ₹5
Next 100 ₹7
Above 200 ₹10
Additional Charges:
• If the bill exceeds ₹2000, apply a 5% surcharge.
• If the total bill is below ₹500, the minimum bill should be ₹500.
Display:
• Total Units
• Bill Amount
• Final Payable Amount'''

#----------------------------------------------------------------------------

# Electricity Bill Calculator

# Input total units
units = int(input("Enter total electricity units: "))

bill = 0

# Calculate bill
if units <= 100:
    bill = units * 5

elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)

else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

# Apply surcharge
if bill > 2000:
    surcharge = bill * 0.05
    bill = bill + surcharge

# Minimum bill
if bill < 500:
    bill = 500

# Display result
print("\n------ Electricity Bill ------")
print("Total Units :", units)
print("Bill Amount : ₹", bill)
print("Final Payable Amount : ₹", bill)