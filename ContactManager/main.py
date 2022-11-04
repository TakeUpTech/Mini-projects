# The script allows to deal with list, file writing and reading and also function and parameter creation.

# Function that have for objective to search a contact name in a .csv file,
# return first name, last name and telephone number if it find the contact and display a message if the contact doesn't exist.

def find_contact(contact_sample, l_n_i, f_n_i):
    name = input('> Write contact first name: ').lower()
    found = False

    with open('contact_file.csv', 'r') as file: # allows to read in a file thanks to 'r'
        for line in file: # for each line of the file
            contact = line.split(',') # put allow information split by ',' in a list
            if contact[l_n_i].lower() == name or contact[f_n_i].lower() == name: # if the name write correspond to the name in the line, so find the contact
                for i in range(len(contact)):
                    print(f'{contact_sample[i]} : {contact[i]}')
                found = True
        
    if not found: 
        print("This contact doesn't exist.") # display a message if the contact is not found

def add_contact(contact_sample):
    contact = [input(f'> Write contact {info.lower()}: ') for info in contact_sample] # list of contact information entered by the user

    with open('contact_file.csv', 'r') as file: # save contacts already saved
        lines = list(file)

    with open('contact_file.csv', 'w') as file: # overwrite in the file all data about all contacts
        lines.append(''.join(f'{info},' for info in contact)[:-1] + '\n')
        for line in lines:
            file.write(line)


contact_sample = ['Last name', 'First name', 'Telephone number'] # list of information per contact (possibility to add many sections as you want)
last_name_index = 0
first_name_index = 1

exit = False
while not exit:
    find_contact(contact_sample, last_name_index, first_name_index)
    add_contact(contact_sample)
    if input("> Restart ? y/n ").lower() != 'y':
        exit = True
