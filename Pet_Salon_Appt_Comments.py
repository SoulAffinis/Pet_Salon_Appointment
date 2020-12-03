import calendar
import datetime
from print_appt import print_appt_txt

customer = [] # empty list to append customer information (used to print in text file)
customer_date = [] #empty list to append customer appointment date (used to print in text file)

# function to clear empty lists (used after the information is printed in the text file)
def clear():
    customer.clear()
    customer_date.clear()

# function to return to main menu selection
def main_menu():
    while True:
        back = input('To go back to main menu press B and enter: ').upper()
        if back == 'B': #user must type 'B' to return to the main menu
            main() #function returns user to the main menu selection(main function)
        else:
            print('Thank you!')
            break
        return
    
# function to list services included with each visit plus additional services offered
def services():
    print('\n\t\tOur services:\n')
    print('\tRegular Grooming includes:')
    print('-Brushing')
    print('-Clipping')
    print('-Teeth cleaning')
    print('-Relaxing bath')
    print('-Blow drying')
    print('-Tailored haircut')
    print('\n\tExtras\nAdditional charge for the following services:\n')
    print('-Flea Cleanse')
    print('-Shedd Release')
    print('-Hydrate and Restore\n\n')
    main_menu()#calls fucntion to ask user if they wish to return to the main menu selection

#function used to give customer a subtotal price based on pet weigth and services requested
def prices():
    #dictionry for prices based on pet size
    price = {'Miniature': 39.99, 'Small': 44.99, 'Medium': 49.99, 'Large': 54.99, 'Extra Large': 59.99}
    #dictonary for prices of extra services offered
    extras = {1: ('Flea Cleanse', 9.99), 2: ('Shedd Release', 14.99), 3: ('Hydrate and Restore', 14.99)}
    cust_total = [] #empty list to append the customers subtotal price
    
    print('\n\nTo give an accurate estimate please answer the following question.\n')
    while True:
        weight = int(input('What is the weight of your dog in pounds?: ')) #ask user for weight of pet
        print('Your subtotal price for regular grooming would be: \n')
        if weight <= 12:
            cust_total.append(price['Miniature']) #if pet weight is <=12 append price for miniature to subtotal list
            print('$',price['Miniature'])#if pet weight is <=12 print the price for miniature from price dictionary
            break
        elif 13 <= weight <= 22:
            cust_total.append(price['Small'])#if pet weight is between 13 & 22 append price for small to subtotal list
            print('$',price['Small'])#if pet weight is between 13 & 22 print the price for small from price dictionary
            break
        elif 23 <= weight <= 57:
            cust_total.append(price['Medium'])#if pet weight is between 23 &57 append price for medium to subtotal list
            print('$',price['Medium'])#if pet weight is between 23 & 57 print the price for medium from price dictionary
            break
        elif 58 <= weight <= 99:
            cust_total.append(price['Large'])#if pet weight is between 58 & 99 append price for large to subtotal list
            print('$',price['Large'])#if pet weight is between 58 & 99 print the price for large from price dictionary
            break
        elif 100<= weight <= 200:
            cust_total.append(price['Extra Large'])#if pet weight is between 100 & 200 append price for extra large to subtotal list
            print('$',price['Extra Large'])#if pet weight is between 100 & 200 print the price for extra large from price dictionary
            break
        else:
            print('Invalid, please try again.\n')#if user input is not 0 through 200 'invalid' will print and user may try again
            continue
    
    ask_extras = input('\nWould you like to add any extras? Y/N: ').upper()#ask customer if they would like additonal services
    if ask_extras == 'Y':#if user selects 'Y' then additonal services are displayed
        print('Prices for extras are:\n')
        for x,y in extras.items():
            print('{}. {}.....${}'.format(x,y[0],y[1]))#for loop to print the addtional services with their prices
        extra_add = int(input('\nWhich extra care treatment would you like to add? '))
        if extra_add in extras.keys():#user will select either 1, 2 or 3 
            cust_total.append(extras[extra_add][1])#append price of additonal service to subtotal list 
            sub = 0
            for x in cust_total:#add the price for regular groom plus any additonal service selected
                sub += float(x)
            print('Subtotal price with extra care treatment is ${:.2f}'.format(sub))#print the subtotal price
            cust_total.clear()#clear the list so it is ready for next customer
        else:
            print('Sorry, invalid option')#invalid option will be displayed if customer doesn't select 1, 2 or 3 from additional services
    else:
        print('Thank you!')

    main_menu()#calls fucntion to ask user if they wish to return to the main menu selection

#fucntion to dispaly pet salon general information
def info():
    print('\n\tHello! We are Puppy Groomers Pet Salon\n')
    print('\tWe are located at 12345 Main Street')
    print('\tOur office phone is 123-456-7891')
    print('\tWe are open 7 days a week from 8:00am to 4:00pm')
    print('\tPlease give us a call if you have any questions!\n')
    main_menu()#calls fucntion to ask user if they wish to return to the main menu selection
    
#class for each customer    
class customers():
    global customer #global empty list for customer information
    global customer_date #gloabl empty list for customer appointment information
    def cust_info(self):
        while True:
            try:
                self.owner_name = input('Enter your first name: ')#ask user for name
                assert self.owner_name.isalpha()#assert to assure user inputs a valid name
            except AssertionError:
                print('Error, please type a valid name.')#if input is not alpha then print error and user wil try again
                continue
            else:
                customer.append(self.owner_name)#append user name to empty customer list if alpha
                break
        while True:
            try:
                self.pet_name = input('Enter your pet\'s name: ')#ask user for pet name
                assert self.pet_name.isalpha()#assert to assure user input is a valid name
            except AssertionError:
                print('Error, please type a valid name.')#if input is not alpha then print error and user will try again
                continue
            else:
                customer.append(self.pet_name)#append pet name to empty customer list of alpha
                break
        while True:
            try:
                self.phone = int(input('Enter your 10 digit phone number(without spaces or special symbols): '))#ask user for phone number
                self.phone = str(self.phone)#convert phone to string
                assert len(self.phone) == 10 #assert to assure user input is valid phone number of 10 digits
            except ValueError:
                print('Error, please use numbers only.')#if input is not a number print error, user tries again
                continue
            except AssertionError:
                print('Error, phone number must be a total of 10 digits.')#if input is not total of 10 digits print error, user tries again
                continue
            else:
                customer.append(self.phone)#append phone to empty customer list if proper
                break
                  
    def appointment_time(self):
        print('We are open 7 days a week from 8:00am to 4:00pm')
        print('(We close an hour for lunch)\n')
        self.avl_times = ['8:00am', '9:00am', '10:00am', '11:00am', '1:00pm', '2:00pm', '3:00pm']#list for salon hours of opertation
        for x in self.avl_times:#for loop to print the salon hours of operation
            print('{}'.format(x))
        while True:
            self.check_time =  int(input('\nEnter the time you prefer from above(as single or double digit): '))
            times = [8,9,10,11,1,2,3]#list to validate user input
            if self.check_time not in times:#if user input is not found in times list print invalid, user tries again
                print('Invalid time')
                continue
            else:
                print('Now let\'s reserve a date for you!\n')
                break
            
        while True:
            self.yy = 21#set the year to 2021
            self.mm = int(input('\nEnter the number of the month you would like to schedule your appointment: '))#set the month to based on user selection
            if self.mm in range (1,13):#checks to assure user input for month is valid
                print('---------------------')
                print(calendar.month(self.yy, self.mm))#print mini calendar with user selected month and year 2021
                break
            else:
                print('Invalid month, please try again.')#if the month number is invalid print error, user tries again
                continue
        self.day = int(input('Enter the date you would like to schedule your appointment: '))
        self.appt_date = datetime. datetime(2021,self.mm,self.day,self.check_time)#create variable for user input date, month, year and time 
        print('Thank you! You have successfully scheduled an appointment for: ', self.appt_date)#print the selected appointment date and time
        print('\nIt is recommended to have your dog groomed atleast every 3 months.\n')
        self.next_yes = input('Would you like to schedule your next appointments?\nY/N:').upper()
        customer_date.append(self.appt_date)#append to user selected date and time to empty list
        if self.next_yes == 'Y':
            self.next_appt1 = self.appt_date + datetime.timedelta(30*3)#variable for 90 days added to first appointment
            self.next_appt2 = self.next_appt1 + datetime.timedelta(30*3)#variable for 90 days added to second appointment
            self.next_appt3 = self.next_appt2 + datetime.timedelta(30*3)#variable for 90 days added to third appointment
            self.next_appt4 = self.next_appt3 + datetime.timedelta(30*3)#variable for 90 days added to fourth appointment
            customer_date.append(self.next_appt1)#append the second appoinment to customer date list
            customer_date.append(self.next_appt2)#append the third appointment to customer date list
            customer_date.append(self.next_appt3)#append the fourth appoinment to customer date list
            customer_date.append(self.next_appt4)#append the fifth appointment to customer date list
            print('Your next appointments will be on the following dates: ')
            print(self.next_appt1)
            print(self.next_appt2)
            print(self.next_appt3)
            print(self.next_appt4)#print the next four appointments
            print_appt_txt(customer,customer_date)#call on function to print customer information and appoinemtns into text file
            clear()#call clear fucntionto clear lists for next customer
            main_menu()#calls fucntion to ask user if they wish to return to the main menu selection
        else:
            print_appt_txt(customer,customer_date)
            clear()
            main_menu()#calls fucntion to ask user if they wish to return to the main menu selection
        return
    
customer1 = customers()
customer2 = customers()
customer3 = customers()
customer4 = customers()
#function for main menu   
def main():
    print('\t\t\tHello and welcome to Puppy Groomers pet salon!\n\n')
    print('1. Schedule Appointment')
    print('2. Check Services')
    print('3. Prices')
    print('4. View Salon Information\n')
    
    while True: 
        choice = int(input('Which would you like to view?\nInput the number of your selection here: '))#ask user what they wish to view based on above choices
        if choice == 1:
            customer1.cust_info()
            customer1.appointment_time()
            customer2.cust_info()
            customer2.appointment_time()
            customer3.cust_info()
            customer3.appointment_time()
            customer4.cust_info()
            customer4.appointment_time()
            break
        elif choice == 2:
            services()
            break
        elif choice == 3:
            prices()
            break
        elif choice == 4:
            info()
            break
        else:
            print('\nInvalid choice.\n')
            continue
        return
main()#call fucntion for main menu

