# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

amount = 1000

interest_rate = .2

number_of_years = 20

for i in range(number_of_years):
    amount = (amount * interest_rate) + amount
    print(amount)
    print(f"You have so much money! You have {amount:.1f}.  It's been {i + 1} years!")