
#function to print customer information and appointment dates in a text file
def print_appt_txt(customer,customer_date):
    file = open('apptset1.txt','w')#open text file to write
    file.write('\t--------Puppy Groomers Pet Salon--------\n')
    file.write('\tHere is a reminder for your upcoming appointment(s).\n')
    file.write('Name: {}\n' .format(customer[0]))#call customer list for name
    file.write('Pet\'s name: {}\n' .format(customer[1]))#call customer list for pet name
    file.write('Phone: {}\n\n' .format(customer[2]))#call customer list for customer phone number
    file.write('Appointment(s):\n')
    for x in customer_date:#for loop to list all customer appointments
        file.write('{}\n' .format(x))
    file.write('\t\nThank you!\nWe will see you soon!\n')
        
    file.close()#close text file
    print('\nYour appointment information has been printed in appset1.txt file!')#text will print after customer sets appointments to let them know where to find it
