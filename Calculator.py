i=1
print("--------------------Welcome to calculator----------------------")
temp = int(input("\nEnter the number : "))
while i!=0:
    print("\n\t\t+ -> Addition\n\t\t- -> Subtraction\n\t\tx -> Multiplication\n\t\t/ -> Division\n\t\t= -> Output\n\t\te -> Exit")
    n = input("Enter the choice - ")
    if n=='+':
        number = int(input("Enter the number for addition : "))
        temp += number
        print('value',str(temp))
        print("===== ADDED =====")
    elif n=='-':
        number = int(input("Enter the number for subtraction : "))
        temp -= number
        print('value',str(temp))
        print("===== SUBTRACTED =====")
    elif n=='x':
        number = int(input("Enter the number for multiplication : "))
        temp *= number
        print('value',str(temp))
        print("===== MULTIPLICATED =====")
    elif n=='/':
        number = int(input("Enter the number for division : "))
        temp /= number
        print('value',str(temp))
        print("===== DIVIDED =====")
    elif n=='=':
        print("Calculation output => "+str(temp))
        print("\n=======================================================================")
        p=1
        while p!=0:
            print('\n\t\tr -> Restart the Calculator\n\t\te -> Exit the calculator\n')
            k = input("Enter your choice - ")
            if k=='r':
                temp = int(input("\nEnter the number : "))
                p=0
            elif k=='e':
                i=0
                p=0
                print("\n========== EXITED SUCCESSFULLY ==========")
            else:
                print("----- You entered a wrong choice !!! -----")
                continue
    elif n=='e':
        i=0
        print("\n========== EXITED SUCCESSFULLY ==========")
    else:
        print ("----- You entered a wrong choice -----")
        continue

