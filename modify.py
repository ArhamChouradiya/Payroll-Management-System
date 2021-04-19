from os import remove, rename

# Modification of existing records in Employee File except Employee Number and Employee Name

# Modification in Basic Salary
def modif1():
    fin = open('EMPLOYEE_FILE.txt', 'r')
    fout = open('TEMPORARY.txt', 'w')
    # Input Employee's Designation
    desig = input('Designation to change Basic Salary? ')
    # Input amount by which Basic Salary has to be increased
    inc = int(input('Amount by which Basic Salary to be increased? '))
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if arr[5] == desig.upper():
            found = 1
            arr[6] = str(int(arr[6]) + inc)
        print('Are you sure you want to change:\n\tY/y for Yes or N/n for No')
        ch = input('Enter your Choice [Y/y or N/n] ')
        if ch == 'Y' or ch == 'y':            
            print('BASIC SALARY UPDATED SUCCESSFULLY!\n')
        else:
            print('BASIC SALARY NOT UPDATED!\n')
        rec = (',').join(arr)
        fout.write(rec + '\n')
    if found == 0:
        print('\nERROR: DESIGNATION NOT FOUND!\n')
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.txt')
    rename('TEMPORARY.txt', 'EMPLOYEE_FILE.txt')

# Modification in Designation
def modif2():
    fin = open('EMPLOYEE_FILE.txt', 'r')
    fout = open('TEMPORARY.txt', 'w')
    # Input Employee Number
    no = input('Employee Number to change Designation? ')
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if int(arr[0]) == no:
            found = 1
            print('Name :', arr[1])
            print('Designation:', arr[5], '\t\t', 'Basic Salary :', arr[6])
            newdes = input('New Designation? ')
            newbs = input('New Basic Salary? ')
            if not newdes.isalnum() or newdes.isdigit():
                print('Please enter proper Designation')
                newdes = input('New Designation? ')
            elif newdes.isalpha():
                print('Please enter proper Designation')
                newdes = input('New Designation? ')
            else:
                break
            print('Are you sure you want to change:\n\tY/y for Yes or N/n for No')
            ch = input('Enter your Choice [Y/y or N/n]? ')
            if ch == 'Y' or ch == 'y':
                arr[5] = newdes.upper()
                arr[6] = newbs
                print('DESIGNATION UPDATED SUCCESSFULLY!\n')
            else:
                print('DESIGNATION NOT UPDATED!\n')
        rec = (',').join(arr)
        fout.write(rec + '\n')
    if found == 0:
        print('\nERROR: EMPLOYEE NUMBER NOT FOUND!\n')
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.txt')
    rename('TEMPORARY.txt', 'EMPLOYEE_FILE.txt')
    

# Modification in Gender
def modif3():
    fin = open('EMPLOYEE_FILE.txt', 'r')
    fout = open('TEMPORARY.txt', 'w')
    found = 0
    # Input Employee Number
    no = input('Employee Number to change Gender? ')
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if int(arr[0]) == no:
            found = 1
            print('Name :', arr[1])
            print('Gender:', arr[2])
            gender = input('Gender [F/M]? ')
            while True:
                if not gender.isalpha():
                    print('Please enter Gender as either F- Female or M- Male')
                    gender = input('Gender [F/M]? ')  
                elif gender.isalpha() and len(gender) != 1:
                    print('Please enter Gender as either F- Female or M- Male')
                    gender = input('Gender [F/M]? ')
                elif gender.upper() != 'F' and gender.upper() != 'M':
                    print('Please enter Gender as either F- Female or M- Male')
                    gender = input('Gender [F/M]? ')
                else:
                    print('Are you sure you want to change?\n\tY/y for Yes or N/n for No')
                    ch = input('Enter your Choice [Y/y or N/n]? ')
                    if ch == 'Y' or ch == 'y':
                        arr[2] = gender
                        print('GENDER UPDATED!\n')
                    else:
                        print('GENDER NOT UPDATED!\n')
                        break    
        rec = (',').join(arr)
        fout.write(rec  + '\n')
    if found == 0:
        print('\nERROR: EMPLOYEE NUMBER NOT FOUND!\n')
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.txt')
    rename('TEMPORARY.txt', 'EMPLOYEE_FILE.txt')

# Modification in Date of Birth
def modif4():
    fin = open('EMPLOYEE_FILE.txt', 'r')
    fout = open('TEMPORARY.txt', 'w')
    # Input Employee Number
    no = input('Employee Number to change Date of Birth? ')
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if int(arr[0]) == no:
            found = 1
            print('Name :', arr[1])
            print('Date of Birth:', arr[3])
            print('Enter a Correct Data of Birth')
            newdob = dateval()
            while len(newdob) != 10:
                print(newdob)
                print('Please enter Correct Date of Birth')
                newdob = dateval()
            print('Are you sure you want to change?\n\tY/y for Yes or N/n for No')
            ch = input('Enter your Choice [Y/y or N/n]? ')
            if ch == 'Y' or ch == 'y':
                arr[4] = newdob
                print('DATE OF BIRTH UPDATED SUCCESSFULLY!\n')
            else:
                print('DATE OF BIRTH NOT UPDATED!\n')
        rec = (',').join(arr)
        fout.write(rec + '\n')
    if found == 0:
        print('\nERROR: EMPLOYEE NUMBER NOT FOUND!\n')
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.txt')
    rename('TEMPORARY.txt', 'EMPLOYEE_FILE.txt')

# Modification in Date of Joining
def modif5():
    fin = open('EMPLOYEE_FILE.txt', 'r')
    fout = open('TEMPORARY.txt', 'w')
    # Input Employee Number
    no = int(input('Employee Number to change Date of Joining? '))
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if int(arr[0]) == no:
            found = 1
            print('Name:', arr[1])
            print('Date of Joining:', arr[4])
            print('Enter a Correct Data of Joining')
            newdoj = dateval()
            while len(newdoj) != 10:
                print(newdoj)
                print('Please enter Correct Data of Joining')
                newdoj = dateval()
            print('Are you sure you want to change?\n\tY/y for Yes or N/n for No')
            ch = input('Enter your Choice [Y/y or N/n]? ')
            if ch == 'Y' or ch == 'y':
                arr[5] = newdoj
                print('DATE OF JOINING UPDATED SUCCESSFULLY!\n')
            else:
                print('DATE OF JOINING NOT UPDATED!\n')
        rec = (',').join(arr)
        fout.write(rec  + '\n')
    if found == 0:
        print('\nERROR: EMPLOYEE NUMBER NOT FOUND!\n')
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.txt')
    rename('TEMPORARY.txt','EMPLOYEE_FILE.txt')

# Modification in Phone Number
def modif6():
    fin = open('EMPLOYEE_FILE.txt', 'r')
    fout = open('TEMPORARY.txt', 'w')
    # Input Employee Number
    no = int(input('Employee Number to change Phone Number? '))
    # Input New Phone Number
    newpn = input('New Phone Number? ')
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if int(arr[0]) == no:
            found = 1
            print('Name :', arr[1])
            print('Phone Number:', arr[7])
            print('Are you sure you want to change?\n\tY/y for Yes or N/n for No')
            ch = input('Enter your Choice [Y/y or N/n]? ')
            if ch == 'Y' or ch == 'y':
                arr[7] = newpn
                print('Phone Number updated!\n')
            else:
                print('Phone Number not updated!\n')
        rec = (',').join(arr)
        fout.write(rec + '\n')
    if found == 0:
        print('\nERROR: EMPLOYEE NUMBER NOT FOUND!\n')
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.txt')
    rename('TEMPORARY.txt', 'EMPLOYEE_FILE.txt')

# Modification in Mobile Number
def modif7():
    fin = open('EMPLOYEE_FILE.txt')
    fout = open('TEMPORARY.txt', 'w')
    # Input Employee Number
    no = int(input('Employee Number to change Mobile Number? '))
    # Input New Mobile Number
    newmob = input('New Mobile Number? ')
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if int(arr[0]) == no:
            found = 1
            print('Name :', arr[1])
            print('Mobile Number:', arr[8])
            print('Are you sure you want to change?\n\tY/y for Yes or N/n for No')
            ch = input('Enter your Choice [Y/y or N/n]? ')
            if ch == 'Y' or ch == 'y':
                arr[8] = newmob
                print('MOBILE NUMBER UPDATED SUCCESSFULLY!\n')
            else:
                print('MOBILE NUMBER NOT UPDATED!\n')
        rec = (',').join(arr)
        fout.write(rec + '\n')
    if found == 0:
        print('\nERROR: EMPLOYEE NUMBER NOT FOUND!\n')
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.txt')
    rename('TEMPORARY.txt', 'EMPLOYEE_FILE.txt')

# Modification in Address
def modif8():
    fin = open('EMPLOYEE_FILE.txt')
    fout = open('TEMPORARY.txt', 'w')
    # Input Employee Number
    no = int(input('Enter the Number for changing the Address- '))
    # Input New Address
    newadd = input('New address? ')
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if int(arr[0]) == no:
            found = 1
            print('Name :', arr[1])
            print('Address :', arr[9])
        print('Are you sure you want to change?\n\tY/y for Yes or N/n for No')
        ch = input('Enter your Choice [Y/y or N/n]? ')
        if ch == 'Y' or ch == 'y':
            arr[9] = newadd.upper()
            print('ADDRESS UPDATED SUCCESSFULLY!\n')
        else:
            print('ADDRESS NOT UPDATED!\n')
        rec = (',').join(arr)
        fout.write(rec  + '\n')
    if found == 0:
        print('\nERROR: EMPLOYEE NUMBER NOT FOUND!\n')
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.txt')
    rename('TEMPORARY.txt', 'EMPLOYEE_FILE.txt')
 
