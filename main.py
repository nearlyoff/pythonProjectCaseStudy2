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

tax = 0

if C == 1 :
    if summ - 9075 > 0 :
        tax = tax + 0,1*9075
    else:tax = tax + 0,1(summ)
        if summ - 36900 > 0:
            tax = tax + 0,15*36900
        else: tax = tax + 0,15(summ)
            if summ - 89350 > 0:
                tax = tax + 0,25 * 89350
            else: tax = tax + 0,25(summ)
                if summ - 186350 > 0:
                    tax = tax + 0,25 * 186350
                    if summ - 405100 > 0:
                        tax = tax + 0,33 * 405100
                        if summ - 406750  > 0:
                            tax = tax + 0,35 * 406750
                            if summ - 406751> 0:
                                tax = tax + 0,396 * (summ - 406751)




elif C == 2 :



elif C == 3 :




else:
    print("NE BALUISA")