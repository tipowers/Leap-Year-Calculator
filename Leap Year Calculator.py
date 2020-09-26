# This program asks a user to input a year and then calculates whether the year was a leap year or not

# Get year user wishes to test
year = int(input('Enter a year: '))

# If year is divisible by 100 and 400
# Output leap year statement
if year % 100 == 0 and year % 400 == 0:
    print('\nIn the year', year, 'February has 29 days. It is a leap year!')

# If year is not divisible by 100, but is divisible by 4
# Output leap year statement
elif year % 100 != 0 and year % 4 == 0:
    print('\nIn the year', year, 'February has 29 days. It is a leap year!')

# Output no leap year statement
else:
    print('\nIn the year', year, 'Febuary has 28 days.', year, 'is not a leap year.')

print('\nAuthor: Tim Powers')
    
