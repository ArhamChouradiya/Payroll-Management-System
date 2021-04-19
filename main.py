from os import remove, rename
from modify import *
from search import *
from display import *
from validate import *

# Addition of records for New Employees in Employee File
def addrec():
    p = []
    no = empcode()    
    fout = open('EMPLOYEE_FILE.txt', 'a')
    for no in range(n):
        no = no + 1
        while True:
            # Input Employee Name
            na = input('Employee Name? ')
            if not na.isalnum() or na.isdigit():
                print('Please enter proper Employee Name')
                na = input('Employee Name? ')
            elif na.isalpha() and len(na) <= 2 :
                print('Please enter proper Employee Name')
                na = input('Employee Name? ')
            else:
                break
        # Input Employee Gender
        gender = input('Gender [F/M]? ')
        while True:
            if not gender.isalpha():
                print('Please enter Gender as either F- Female or M- Male')
                gender = input('Gender [F/M]? ')
            elif gender.isalpha() and len(gender) != 1 :
                print('Please enter Gender as either F- Female or M- Male')
                gender = input('Gender [F/M]? ')
            elif gender.upper() != 'F' and gender.upper() != 'M' :
                print('Please enter Gender as either F- Female or M- Male')
                gender = input('Gender [F/M]? ')
            else:
                break
        # Input Date of Birth details
        print('Enter Employee Date of Birth details')
        dob = dateval()
        while len(dob) != 10:
            print(dob)
            print('Please enter Correct Date of Birth')
            dob = dateval()
        # Input Date of Joining details
        print('Enter Employee Date of Joining details')
        doj = dateval()
        while len(doj) != 10:
            print(doj)
            print('Please enter Correct Date of Joining')
            doj = dateval()
        # Input the Employee's Designation
        des = input('Employee Designation? ')
        # Input Basic Salary
        bs = input('Basic Salary? ')
        # Input the Employee's Phone number
        pn = input('Phone Number? ')
        validphone = phonevalidate(pn)
        if len(pn) == 10:
            while validphone == 1:
                print('Please enter New Phone Number as it already exists')
                pn = input('Phone Number? ')
                validphone = phonevalidate(pn)
            while True:
                if pn in p:
                    print('Please enter New Phone Number as it already exists')
                    pn = input('Phone Number? ')
                else:
                    p += [pn]
                    break
        else:
            print('Please enter New Phone Number with 10 digits')
            pn = input('Phone Number? ')
            validphone = phonevalidate(pn)
            while True:
                if pn in p:
                    print('Please enter New Phone Number as it already exists')
                    pn = input('Phone Number? ')
                else:
                    p += [pn]
                    break
        # Input the Employee's Mobile number                
        mob = input('Mobile Number? ')
        # Input the Employee's Address
        add = input('Address? ')
        
        data = str(no) +  ',' +  na.upper() +  ',' +  gender.upper() +  ',' +  dob +  ',' +  doj +  ',' +  des.upper() +  ',' +  bs +  ',' +  str(pn) +  ',' +  mob +  ',' +  add.upper() +  '\n'
        fout.write(data)
    print('\nEMPLOYEE RECORDS ADDED SUCCESSFULLY!\n')
    fout.close()
    
    
# Input Number of days worked and other deductions of each Employee in Monthly Pay File
def mpayfile():
    arr = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    m, y = 0, 1
    maxdays_work = 0
    while True:
        if m not in [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12] and y < 2015 :
            # Input Month
            m = int(input('Month? '))
            # Input Year
            y = int(input('Year? '))
        else:
            break
    if m in [1, 3, 5, 7, 8, 9, 10, 12]:
        maxdays_work = 27
    elif m in [4, 6, 9, 11]:
        maxdays_work = 26
    elif m == 2:
        if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
            maxdays_work = 25
        else:
            maxdays_work = 24
    file_name = 'Monthly_pay' + '_' + arr[m-1] + '_' + str(y) + '.txt'        
    fout = open(file_name, 'a')
    # Input Emplyee Number
    no = input('Employee Number? ')
    fin = open('EMPLOYEE_FILE.txt', 'r')
    for line in fin:
        line = line.strip()
        arr = line.split(',')
        if arr[0] == str(no):
            print('Employee Name  :', arr[1])
            act_basic = int(arr[6])
            print('Basic  :', act_basic)
            #Validation for Number of working days
            #Calculation of Basic Salary
            leaves = int(input('Number of leaves taken in the month? '))
            if leaves >= 0 and leaves <= maxdays_work:
                days = maxdays_work - leaves
                mon_sal = (act_basic // maxdays_work) * days
            else:
                while leaves >= 0 and leaves <= maxdays_work:
                    print('Please enter valid Number of leaves')
                    leaves = int(input('Number of leaves taken in the month? '))
                    days = maxdays_work - leaves
            if days >= 0 and leaves <= days:
                mon_sal = (act_basic // maxdays_work) * days
                da = round(0.55 * mon_sal)
                hra = round(0.35 * mon_sal)
                conv = round(0.15 * mon_sal)
                gross = round(mon_sal + da + hra + conv)
                itax = round(0.05 * mon_sal)
                loan = round(0.1 * mon_sal)
                ded = round(itax + loan)
                net = round(gross - ded)
                print('\nBasic\tDA\tHRA\tConveyance\tGross\tItax\tLoan\tDeductions\tNet')
                print('-' * 90)
                print(str(mon_sal) +  '\t' +  str(da) +  '\t' +  str(hra) +  '\t' +  str(conv) +  '\t\t' +  str(gross) +  '\t' +  str(itax) +  '\t' +  str(loan) +  '\t' +  str(ded) +  '\t\t' +  str(net), '\n\nAdded in Monthly Pay File!\n')
                data = str(no) +  ',' +  arr[1].upper() + ',' +  arr[5].upper() +  ',' +  str(days) +  ',' +  str(mon_sal) +  ',' +  str(da) +  ',' +  str(hra) +  ',' +  str(conv) +  ',' +  str(gross) +  ',' +  str(itax) +  ',' +  str(loan) +  ',' +  str(net) +  '\n'
                fout.write(data)
    fout.close()


# Menu
while True:
    print('''Main Menu:
1. Addition of New Employee records in Employee File
2. Addition of Employee Pay File records in Monthly Pay File
3. Modification in existing records
4. Search for Employee records
5. Delete existing Employee records
6. Display files
7. Print Salary Statement
8. Print Salary Slip
0. Exit Main Menu\n''')
    ch = int(input('Choice[0-8]? '))
    if ch == 1:
        n = int(input('Number of Employees to be added? '))
        addrec()
    elif ch == 2:
        mpayfile()
    elif ch == 3:
        print('''\nModification in Employee details Menu:
1. Modify Basic Salary
2. Modify Designation
3. Modify Gender
4. Modify Date of Birth
5. Modify Date of Joining
6. Modify Phone Number
7. Modify Mobile Number
8. Modify Address
0. Exit Modification Menu\n''')
        a = int(input('Choice[0-8]? '))
        while True:
            if a == 1:
                modif1()
            elif a == 2:
                modif2()
            elif a == 3:
                modif3()
            elif a == 4:
                modif4()
            elif a == 5:
                modif5()
            elif a == 6:
                modif6()
            elif a == 7:
                modif7()
            elif a == 8:
                modif8()
            elif a == 0:
                break 
    elif ch == 4:
        print('''\nSearching for Employee details Menu:
1. Searching by Employee Number
2. Searching by Employee Name
0. Exit Search Menu\n''')
        a = int(input('Choice[0-2]? '))
        while True:
            if a == 1:
                search1()
                break
            elif a == 2:
                search2()
                break
            elif a == 0:
                break
    elif ch == 5:
        delete()
    elif ch == 6:
        print('''\nDisplay File Menu:
1. Display Employee File
2. Display Monthly Pay File
0. Exit Display Menu\n''')
        a = int(input('Choice[0-2]? '))
        if a == 1:
            display_emp()
        elif a == 2:
            display_mon()
        elif ch == 0:
            break
    elif ch == 7:
        sal_statement()
    elif ch == 8:
        sal_slip()
    elif ch == 0:
        print('\n', 'Thank You for Visiting!!', '\n')
        break
