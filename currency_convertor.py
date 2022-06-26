# CS361 Software Engineering 1
# John Kim
# Foreign Currency Convertor

def inst_print():
    print(" ---------------------------------------------------")
    print(" Name of Country  |  Currency Code  |  Currency Name")
    print(" ---------------------------------------------------")
    print("   Unite State    |       USD       |     Dollar")
    print("     Europe       |       EUR       |      Euro")
    print("  United Kingdom  |       GBP       |    Sterling")
    print("     Canada       |       CAD       |     Dollar")
    print("     Japan        |       JPY       |      Yen")
    print(" ---------------------------------------------------")

########### I need this from my partner ##############
conversion_ratio = [1.2, 1.8, 0.8, 20]
# conversion_ratio[0] = conversion ration from USD to EUR
# conversion_ratio[1] = conversion ration from USD to GBP
# conversion_ratio[2] = conversion ration from USD to CAD
# conversion_ratio[3] = conversion ration from USD to JPY
######################################################

cur_code_list = ['USD', 'EUR', 'GBP', 'CAD', 'JPY']
inst_print()
print("")
total_cur_from_amount = 0
while True:
    # currency from
    while True:
        error = 0
        cur_from = input("Please enter currency code that you like to convert from: ")
        for cur_code in cur_code_list:
            if cur_from == cur_code:
                error = 1
                break
        if error == 0:
            print("*** Warning: Wrong input, please select correct currency code in the table below")
            inst_print()
        else:
            break

    # USD dollar amount
    cur_from_amount = float(input("Please enter amount of currency which you like to convert from: "))

    # currency to
    while True:
        error = 0
        cur_to = input("Please enter currency code that you like to convert to: ")
        for cur_code in cur_code_list:
            if cur_to == cur_code:
                error = 1
                break
        if error == 0:
            print("*** Warning: Wrong input, please select correct currency code in the table below")
            inst_print()
        else:
            break

    if cur_from == 'USD':
        if cur_to == 'EUR':
            cur_to_amount = cur_from_amount * conversion_ratio[0]
        elif cur_to == 'GBP':
            cur_to_amount = cur_from_amount * conversion_ratio[1]
        elif cur_to == 'CAD':
            cur_to_amount = cur_from_amount * conversion_ratio[2]
        elif cur_to == 'JPY':
            cur_to_amount = cur_from_amount * conversion_ratio[3]

    total_cur_from_amount += cur_from_amount
    see_amount = input("Would you like to see the total USD you spent so far? (Y/N)")
    print("******* CONVERSION RESULT *********")
    print(cur_from_amount, " ", cur_from, " is converted to ", cur_to_amount, " ", cur_to)
    if see_amount == 'Y':
        print("Total USD you spent so far is ", total_cur_from_amount, "USD")
    print("")
    again = input("Would you like to conduct another currency transaction? (Y/N) ")
    if again == 'Y':
        continue
    elif again == 'N':
        print("Thank you. Good-bye!")
        break




