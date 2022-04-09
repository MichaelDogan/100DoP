# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

# Welcome user to the tip calculator
print("Welcome to the tip calculator.")

# Get total bill from user input *note it comes in as str* so we need to make it a float
total_bill = input("What was the total bill? $")
total_bill = float(total_bill)  # now a float

# Get the percentage tip you would like to give and again change the str input to a float and then change to a percent by dividing by 100
tip_percent = input(
    "What percentage tip would you like to give? 10, 12, or 15? ")
tip_percent = float(tip_percent) / 100

# Get the number of individuals splitting the bill, and once again change str to usable number, this time an int (just for kicks)
number_splitting_bill = input("How many people to split the bill? ")
number_splitting_bill = int(number_splitting_bill)

total_per_person = ((total_bill * tip_percent) +
                    total_bill) / number_splitting_bill

print(f"Each person should pay: ${total_per_person:.2f}")
