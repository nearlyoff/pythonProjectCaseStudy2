# Case-study #2 "Progressive taxation"
# Developers:   Kremlin V. (40%),
#               Maslyukova P. (30%),
#               Soknyshev D. (50%)
print('Choose your category (1 - one subject, 2 - married couple, 3 - single parent). Type only 1 value: ')
C = int(input())
if C == 1 or C == 2 or C == 3:
    months_list = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    summ = 0
    print('Enter your income for each month:')
    for month in range(12):
        print(months_list[month])
        income = int(input())
        summ += income

    print('Your annual income:', summ)
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
            tax += 0.1 * summ

    elif C == 2:
        if summ - 18150 > 0:
            tax += 0.1 * 18150
            if summ - 73800 > 0:
                tax += 0.15 * (73800 - 18150)
                if summ - 148850 > 0:
                    tax += 0.25 * (148850 - 73800)
                    if summ - 226850 > 0:
                        tax += 0.28 * (226850 - 148850)
                        if summ - 405100 > 0:
                            tax += 0.33 * (405100 - 226850)
                            if summ - 457600 > 0:
                                tax += 0.35 * (457600 - 405100)
                                if summ - 457601 > 0:
                                    tax += 0.396 * (summ - 457601)
                            else:
                                tax += 0.35 * (summ - 405100)
                        else:
                            tax += 0.33 * (summ - 226850)
                    else:
                        tax += 0.28 * (summ - 148850)
                else:
                    tax += 0.25 * (summ - 73800)
            else:
                tax += 0.15 * (summ - 18150)
        else:
            tax += 0.1 * summ

    elif C == 3:
        if summ - 12950 > 0:
            tax += 0.1 * 12950
            if summ - 49400 > 0:
                tax += 0.15 * (49400 - 12950)
                if summ - 127550 > 0:
                    tax += 0.25 * (127550 - 49400)
                    if summ - 206600 > 0:
                        tax += 0.28 * (206600 - 127550)
                        if summ - 405100 > 0:
                            tax += 0.33 * (405100 - 206600)
                            if summ - 432200 > 0:
                                tax += 0.35 * (432200 - 405100)
                                if summ - 432201 > 0:
                                    tax += 0.396 * (summ - 432201)
                            else:
                                tax += 0.35 * (summ - 405100)
                        else:
                            tax += 0.33 * (summ - 206600)
                    else:
                        tax += 0.28 * (summ - 127550)
                else:
                    tax += 0.25 * (summ - 49400)
            else:
                tax += 0.15 * (summ - 12950)
        else:
            tax += 0.1 * summ

    print('Your annual tax:', round(tax, 2))
else:
    print('Invalid category value. Try again.')
