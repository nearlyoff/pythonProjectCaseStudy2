# Case-study #2
# Developers:   Kremlin V. (%),
#               Maslyukova P. (%),
#               Soknyshev D. (%)
print('Choose your category (1 - one subject, 2 - married couple, 3 - single parent). Type only 1 value: ')
C = int(input())
months_list = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
summ = 0
print('Enter your income for each month:')
for month in range(12):
    print(months_list[month])
    income = int(input())
    summ += income

print('Your annual income: ', summ)

tax = 0

if C == 1:
    if summ - 9075 > 0:
        tax += 0.1 * 9075
        if summ - 36900 > 0:
            tax += 0.15 * (36900 - 9075)
            if summ - 89350 > 0:
                tax += 0.25 * (89350 - 36900)
                if summ - 186350 > 0:
                    tax += 0.28 * (186350 - 89350)
                    if summ - 405100 > 0:
                        tax += 0.33 * (405100 - 186350)
                        if summ - 406750 > 0:
                            tax += 0.35 * (406750 - 405100)
                            if summ - 406751 > 0:
                                tax += 0.396 * (summ - 406751)
                        else:
                            tax += 0.35 * (summ - 405100)
                    else:
                        tax += 0.33 * (summ - 186350)
                else:
                    tax += 0.28 * (summ - 89350)
            else:
                tax += 0.25 * (summ - 36900)
        else:
            tax += 0.15 * (summ - 9075)
    else:
        tax += 0.1 * (summ)





elif C == 2:

    print("BALUISA")

elif C == 3:
    print("BALUISA")


else:
    print("NE BALUISA")

print(tax)
