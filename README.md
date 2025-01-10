# Phonebook Application

## Introduction

The Phonebook Application is a simple yet functional software that allows users to manage their contacts. It is built using Python's Tkinter for the graphical user interface (GUI) and MongoDB for storing contacts. This application supports basic operations such as adding, deleting, editing, searching, and sorting contacts, as well as toggling between showing all or no contacts.

## Problem

In many cases, people need to store and manage contacts digitally. It is common to have a collection of contacts with their names and phone numbers. A simple contact management application can make it easier for users to:

- Store contacts efficiently
- Retrieve contact details quickly
- Edit or delete contacts
- Search for specific contacts
- Sort contacts by name or phone number
- Display all contacts at once or hide them

A typical problem arises when managing contacts manually, where it is time-consuming and error-prone to organize and retrieve contact information.

## Solution

This Phonebook Application provides an intuitive interface that allows users to perform all the necessary actions required to manage their contacts in a digital format. The application connects to a MongoDB database to store and retrieve contacts and uses Tkinter to create an interactive GUI.

### Key Features:

- **Add Contact:** Allows users to add a new contact by entering the contact name and phone number.
- **Delete Contact:** Users can delete an existing contact by specifying the contact's name.
- **Edit Contact:** Users can update an existing contact's name and phone number.
- **Search Contact:** Users can search for contacts by name.
- **Sort Contacts:** Users can sort contacts either by name or phone number.
- **Show/Hide Contacts:** A toggle button allows users to either show or hide the list of contacts.

## Technologies Used

- **Python:** A high-level programming language used to build the application.
- **Tkinter:** A Python library for creating graphical user interfaces.
- **MongoDB:** A NoSQL database used for storing contact data.
- **pymongo:** A Python driver for MongoDB, used to interact with the database.

## Algorithm

1. **Add Contact:**
   - Input validation checks are performed to ensure the name and phone number are valid.
  
   - Example : ![image](https://github.com/user-attachments/assets/3d69abaa-0c97-4d2b-9e8b-a7a1ae7c6388)

   - The contact is inserted into the MongoDB database if the contact name or phone number does not already exist.
  
   - Example : ![image](https://github.com/user-attachments/assets/caee4440-9bed-4c2d-aae4-58f41b8cfcc6)
2. **Delete Contact:**

   - The user specifies a contact's name to delete.
  
   - Example : before delete the contact list
   - ![image](https://github.com/user-attachments/assets/8b07f2e8-7fbb-43d4-b736-313ca118672f)

      after perform the operation contact list
     ![image](https://github.com/user-attachments/assets/2379552e-fbc5-410c-96fb-6d75a7d50c50)

   - The application checks whether the contact exists in the database, and if found, it is removed.

3. **Edit Contact:**

   - Users provide the old contact name along with the new name and phone number.
  
   - Examplpe ==> before update the contact number
   - ![image](https://github.com/user-attachments/assets/56027ad2-87f2-416b-a02d-2713a2013084)

   after update the contact:
   ![image](https://github.com/user-attachments/assets/36f7407b-1418-4a7b-87bb-550dbe5bbad4)

   - The application checks if the contact exists and updates the information.
5. **Search Contact:**

   - Users can enter a search term, and the application uses a case-insensitive regular expression search in MongoDB to find matching contacts.
   Example :
![image](https://github.com/user-attachments/assets/ad8e9adf-24cc-4055-94c0-99da91b89ee1)
now click on search button

![image](https://github.com/user-attachments/assets/533498a1-c1b8-4e70-860d-53a64887fd57)

6. **Sort Contacts:**

   - The contacts are sorted based on either the name or the phone number field using MongoDB's built-in sorting functionality.
   Example :
   --click on sort by name button
     output : ![image](https://github.com/user-attachments/assets/040beb71-1964-43bc-bf3c-59e0b63dcfe2)

7. **Show All Contacts:**
   - The user can between showing all contacts and with all insertin or deletion operations...

The application displays a GUI with the following functionality:

- A listbox shows all the contacts in the database.
- Error messages or success messages are displayed in red to inform users of the current operation status.
- Buttons provide easy access to each functionality (Add, Delete, Edit, Search, Sort, Show/Hide).
- The contacts list is dynamically updated when any changes occur.

### Example GUI:

Phone Number: [_____________]
New Name (for Edit): [_________]
New Phone Number (for Edit): [__]

---

## [Add Contact] [Delete Contact]

## [Search Contact]

## [Show Contacts]

## Contacts:

[Contact 1 --> Phone Number]
[Contact 2 --> Phone Number]

---

finalUI ==> ![image](https://github.com/user-attachments/assets/8b2410b1-9488-4c88-945a-6cff855400a2)

## How to Run 

1. Clone the repository to your local machine.
2. Ensure that you have Python 3.x and MongoDB installed.
3. Install the necessary dependencies:

pip install pymongo pip install tkinter 

4. Start your MongoDB server.
5. 5. Run the `phonebook.py` file:


## Also run the code using html, css and javascript (frontend-backend)

output ==> 


