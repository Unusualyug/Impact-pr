from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/contact")
db = client.phonebook
collection = db.contacts

def welcome():
    while True:
        try:
            entry = int(input("""welcome to py contact book.
                        >>> py contact book commands are: 1, 2, 3, 4, or 5 <<<
                        >>> what would you like to do? <<<
                        1. display your existing contacts
                        2. create a new contact
                        3. check an entry
                        4. delete an entry
                        5. exit
                        enter your entry here (1, 2, 3, 4, or 5): """))
            if entry in [1, 2, 3, 4, 5]:
                return entry
            else:
                print("invalid entry! please enter a number between 1 and 5.")
        except ValueError:
            print("invalid input! please enter a valid number.")

def phonebook():
    while True:
        entry = welcome()
        if entry == 1:
            contacts = collection.find()
            contact_list = list(contacts)
            if contact_list:
                for contact in contact_list:
                    print(f"{contact['name']} --> {contact['phone']}")
            else:
                print('you have an empty phonebook!')
        elif entry == 2:
            phone_number = input('please enter a number: ')
            contact_name = input('enter the contact name: ')
            if collection.find_one({"phone": phone_number}):
                print('this phone number is already saved in your phonebook.')
            elif collection.find_one({"name": contact_name}):
                print('this name is already saved. please choose a different name.')
            else:
                collection.insert_one({"name": contact_name, "phone": phone_number})
                print('contact successfully saved.')
        elif entry == 3:
            name = input('enter the name of the contact you wish to view: ')
            contact = collection.find_one({"name": name})
            if contact:
                print(f"the contact is {contact['name']} --> {contact['phone']}")
            else:
                print('that contact does not exist!')
        elif entry == 4:
            name = input('enter the name of the contact you wish to delete: ')
            result = collection.delete_one({"name": name})
            if result.deleted_count > 0:
                print(f"contact '{name}' deleted.")
            else:
                print('that contact does not exist!')
        elif entry == 5:
            print('thanks for using the py contact book.')
            break
        else:
            print('incorrect entry! please try again.')

phonebook()
