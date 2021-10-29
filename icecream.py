def product_select():
    print('*********************************************************************************')
    learn = str(input( 'Welcome to the Ice Cream Shopee, can I help you find the perfect flavor? y/n: '))
    if learn == 'y':
        while learn != 'n':
            print(' Here is a list of our current flavors')
            print('1. Double Chocolate Crunch')
            print('2. Orange Creamsicle')
            print('3. Cookies and cream')
            print('4. The rockiest road')
            flavor_choice = int(input('please choose the flavor you would like to learn about by typing in number associated with flavor i.e "1": '))
            if flavor_choice == 1:
                print('***********************************************************************************')
                print('Chocolate ice cream with crunchy chocolate pieces')
                print('***********************************************************************************')
                learn = str(input('would you like to learn about more flavors? y/n: '))
            elif flavor_choice == 2:
                print('***********************************************************************************')
                print('A classic orange and vanilla swirl')
                print('***********************************************************************************')
                learn = str(input('would you like to learn about more flavors? y/n: '))
            elif flavor_choice == 3:
                print('***********************************************************************************')
                print('Vanilla ice cream with oreo cookies') 
                print('***********************************************************************************')
                learn = str(input('would you like to learn about more flavors? y/n: '))
            elif flavor_choice == 4:
                print('***********************************************************************************')
                print('Chocolate ice cream with marshmallows and nuts')
                print('***********************************************************************************')
                learn = str(input('would you like to learn about more flavors? y/n: '))
        print('***********************************************************************************')
        print('             Great! , lets get you some ice cream')
        print('***********************************************************************************')
def product_purchase():
    print('***********************************************************************************')
    print("                        Welcome Back to the Ice cream Shopee")
    print('***********************************************************************************')
    print('To choose a flavor type the number associated with the flavor')
    print("if done 'shopping' please type 'y' after entering scoop amount")
    print('If still calculating press the "enter" key after entering scoop amount')
    print('We can now accept scoop amounts as floating nubers. i.e 3.5')
    total_price = 0
    ready = 'n'
    product_list = { 'Double Chocolate Crunch' : 1.50,
                 'Orange Creamsicle' : 1.25,
                 'Cookies and cream' : 1.50,
                 'The rockiest road' : 1.75 }
    DC = product_list['Double Chocolate Crunch']
    OC = product_list['Orange Creamsicle']
    CC = product_list['Cookies and cream']
    RR = product_list['The rockiest road']
    print('***********************************************************************************')
    print(' Here is a list of our current flavors')
    print('1. Double Chocolate Crunch $1.50 per scoop')
    print('2. Orange Creamsicle $1.25 per scoop')
    print('3. Cookies and cream $1.50 per scoop')
    print('4. The rockiest road $1.75 per scoop \n')
    print('***********************************************************************************')
    flavor_choice = int(input('please choose the flavor you would like to purchase: '))
    scoops = float(input('Number of scoops: \n'))
    ready = str(input('are you ready to checkout? y/n: '))
    if ready == 'y' and flavor_choice == 1:
        print("Your total is",'$',round(DC * scoops,2))
        total_price = DC * scoops
    if ready == 'y' and flavor_choice == 2:
        print("Your total is",'$',round(OC * scoops,2))
        total_price = OC * scoops
    if ready == 'y' and flavor_choice == 3:
        print("Your total is",'$',round(CC * scoops,2))
        total_price = CC * scoops
    if ready == 'y' and flavor_choice == 4:
        print("Your total is",'$',round(RR * scoops,2))
        total_price = RR * scoops
    else:
      while (ready != 'y'):
        if ready != 'y' and flavor_choice == 1:
            total_price += DC * scoops
            print('current balance is $', round(float(total_price),2))
            flavor_choice = int(input('please choose the flavor you would like to purchase or type 5 to list flavors: '))
            if flavor_choice == 5:
                print('***********************************************************************************')
                print(' Here is a list of our current flavors')
                print('1. Double Chocolate Crunch $1.50 per scoop')
                print('2. Orange Creamsicle $1.25 per scoop')
                print('3. Cookies and cream $1.50 per scoop')
                print('4. The rockiest road $1.75 per scoop \n')
                print('***********************************************************************************')
                flavor_choice = int(input('please choose the flavor you would like to purchase or type 5 to list flavors: '))
            if flavor_choice == 5:
                print('please enter a flavor from the list')
            else:
                scoops = float(input('Number of scoops: \n'))
                ready = str(input('are you ready to checkout? y/n: '))
                total_price += DC * scoops
                scoops =0
        elif ready != 'y' and flavor_choice == 2:
            total_price += OC * scoops
            print('current balance is $', round(float(total_price),2))
            flavor_choice = int(input('please choose the flavor you would like to purchase or type 5 to list'))
            if flavor_choice == 5:
                print('***********************************************************************************')
                print(' Here is a list of our current flavors')
                print('1. Double Chocolate Crunch $1.50 per scoop')
                print('2. Orange Creamsicle $1.25 per scoop')
                print('3. Cookies and cream $1.50 per scoop')
                print('4. The rockiest road $1.75 per scoop \n')
                print('***********************************************************************************')
                flavor_choice = int(input('please choose the flavor you would like to purchase or type 5 to list flavors: '))
            if flavor_choice == 5:
                print('please enter a flavor from the list')
            else:
                scoops = float(input('Number of scoops: \n'))
                ready = str(input('are you ready to checkout? y/n: '))
                total_price += OC * scoops
                scoops = 0
        elif ready != 'y' and flavor_choice == 3:
            total_price += CC * scoops
            print('current balance is $', round(float(total_price),2))
            flavor_choice = int(input('please choose the flavor you would like to purchase or type 5 to list flavors: '))
            if flavor_choice == 5:
                print('***********************************************************************************')
                print(' Here is a list of our current flavors')
                print('1. Double Chocolate Crunch $1.50 per scoop')
                print('2. Orange Creamsicle $1.25 per scoop')
                print('3. Cookies and cream $1.50 per scoop')
                print('4. The rockiest road $1.75 per scoop \n')
                print('***********************************************************************************')
                flavor_choice = int(input('please choose the flavor you would like to purchase or type 5 to list flavors: '))
            if flavor_choice == 5:
                print('please enter a flavor from the list')
            else:
                scoops = float(input('Number of scoops: \n'))
                ready = str(input('are you ready to checkout? y/n: '))
                total_price += CC * scoops
                scoops = 0
        elif ready != 'y' and flavor_choice == 4:
            total_price += RR * scoops
            print('current balance is $', round(float(total_price),2))
            flavor_choice = int(input('please choose the flavor you would like to purchase or type 5 to list flavors: '))
            if flavor_choice == 5:
                print('***********************************************************************************')
                print(' Here is a list of our current flavors')
                print('1. Double Chocolate Crunch $1.50 per scoop')
                print('2. Orange Creamsicle $1.25 per scoop')
                print('3. Cookies and cream $1.50 per scoop')
                print('4. The rockiest road $1.75 per scoop \n')
                print('***********************************************************************************')
                flavor_choice = int(input('please choose the flavor you would like to purchase or type 5 to list flavors: '))
            if flavor_choice == 5:
                print('please enter a flavor from the list')
                flavor_choice = int(input('please choose the flavor you would like to purchase or type 5 to list flavors: '))
            elif flavor_choice != 5:
                scoops = float(input('Number of scoops: \n'))
                ready = str(input('are you ready to checkout? y/n: '))
                total_price += RR * scoops
                scoops = 0
      print('your total is', total_price)
      print('Please pay','$',round(float(total_price),2),'now')
    cash_used = float(input( 'Cash Used: \n'))
    if (cash_used < 0):
        print(' Must be a positive number!')
    elif cash_used < total_price:
        print('You too broke! come back with more money.')
    else:
        change_needed1 = (cash_used - total_price)
        change_needed = change_needed1
        num_hundreds = (change_needed // 100)
        change_needed -= num_hundreds * 100 # subtract 100 dollar bills amount from total change 
        num_fifties = change_needed  // 50
        change_needed -= num_fifties * 50 # subtract 50 dollar bills amount from change
        num_twenty =  change_needed  // 20
        change_needed -= num_twenty * 20# subtract 20 dollar bills amount from change 
        num_ten =  change_needed  // 10
        change_needed -= num_ten * 10 # subtract 10 dollar bills amount from change
        num_fives = change_needed // 5
        change_needed -= num_fives * 5
        num_ones = change_needed // 1
        change_needed -= num_ones * 1
        num_cents = round(change_needed  * 100)
        change = num_cents
        quarters = change // 25
        change -= quarters * 25
        dimes = change // 10
        change -= dimes * 10
        nickels = change // 5
        change -= nickels * 5
        pennies = change // 1
        print("your change is:", '$',round(change_needed1, 2))
        print('*******************************************')
        print (int(num_hundreds), ('hundred dollar bills'))
        print (int(num_fifties),('Fifty dollar bills'))
        print (int(num_twenty), ('tewnty dollar bills'))
        print (int(num_ten), ('ten dollar bills'))
        print (int(num_fives), ('five dollar bills'))
        print (int(num_ones), ('one dollar bills '))
        print ('*******************************************')
        print (int(quarters), ('quarters'))
        print (int(dimes), ('dimes'))
        print (int(nickels), ('nickels'))
        print (int(pennies), ('pennies \n'))
while True:
    product_select()
    product_purchase()