# Case-study #2
# Developers:   Kremlin V. (%),
#               Maslyukova P. (%),
#               Soknyshev D. (%)
print('Choose your category (1 - one subject, 2 - married couple, 3 - single parent). Type only 1 value: ')
C = input()
months_list = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
summ = 0
print('Enter your income for each month:')
for month in range(12):
    print(months_list[month])
    income = int(input())
    summ += income

print('Your annual income: ', summ)

if C == 1:



elif C == 2:



elif C == 3:




else:
    print("Invalid category value. Please try again.")