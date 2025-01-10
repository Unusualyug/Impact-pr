# Phonebook Web

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

# Phonebook Application

## Introduction
The Phonebook Application is a simple web-based application that allows users to manage their contacts. It is built using **Node.js** and **MongoDB** to provide a full CRUD (Create, Read, Update, Delete) functionality for contacts. Users can add new contacts, edit existing ones, delete contacts, and search or sort contacts by name.

## Problem
Managing contacts can be cumbersome without an easy-to-use interface for storing, retrieving, and updating contact information. Traditional methods, like paper-based systems or simple spreadsheets, can become inefficient and error-prone, especially as the number of contacts grows.

This application addresses the problem by providing an intuitive, web-based platform where users can easily store and manage their contacts.

## Solution
The Phonebook Application is built using **Express.js** to handle backend logic and **MongoDB** to store contact data. The application allows users to:

- View all contacts
- Add new contacts
- Edit existing contacts
- Delete contacts
- Search contacts by name
- Sort contacts alphabetically

The application has a simple, clean user interface powered by **EJS** templating engine, making it easy to display contact data dynamically.

## Technologies Used
- **Node.js**: JavaScript runtime used for building the server-side application.
- **Express.js**: Web application framework for Node.js that simplifies routing and middleware integration.
- **MongoDB**: NoSQL database used to store contact data.
- **Mongoose**: ODM (Object Data Modeling) library for MongoDB used to interact with the database.
- **EJS**: Templating engine used to render dynamic HTML pages.
- **Body-Parser**: Middleware used to parse incoming request bodies, especially for form submissions.
- **CORS**: Middleware to enable Cross-Origin Resource Sharing, allowing the frontend to make requests to the server from a different domain.

## Algorithm
1. **Create a Contact**: A user submits the contact form. The form data is captured and stored in the MongoDB database.
2. **Read Contacts**: On the homepage, all stored contacts are retrieved from the database and displayed in a list.
3. **Update a Contact**: A user can select a contact to edit. The contact details are retrieved from the database, displayed in an editable form, and then updated upon submission.
4. **Delete a Contact**: A user can delete a contact. The selected contact is removed from the MongoDB database.
5. **Search Contacts**: A user can search for contacts by name. The application filters contacts that match the search query.
6. **Sort Contacts**: A user can view contacts sorted by name in ascending order.

## Output

### Homepage:
Displays all contacts stored in the database. Users can view the list of contacts with options to edit or delete them.

### Add Contact Form:
A form where users can input a new contact's name and phone number.

### Edit Contact Form:
A form pre-filled with the contact's current details, allowing users to modify and save changes.


### Screenshots:

1. **Home Screen** – Displays a list of all contacts.
   - Contact name and phone number displayed with options to edit or delete.
![image](https://github.com/user-attachments/assets/7c768941-bc8b-40c3-8e0f-4b2c0b57828b)

2. **Add Contact Form** – Form to input a new contact's name and phone number.
![image](https://github.com/user-attachments/assets/50457e3c-db42-433f-a03b-7e95592853e2)

Output ==>
![image](https://github.com/user-attachments/assets/72ec7440-c018-4ef8-a5f3-8fd078bc8bde)


3. **Edit Contact Form** – Form that allows users to modify a contact's details.
![image](https://github.com/user-attachments/assets/829ca155-9dd9-4bec-8770-c7bfb756f141)

after update ++>
![image](https://github.com/user-attachments/assets/f5ddfc9e-8ab2-425e-8b74-0ff2c88ee4f5)

---

## Getting Started

### Prerequisites
To run this project, you will need:
- **Node.js** installed (https://nodejs.org/)
- **MongoDB** installed locally or use a cloud MongoDB service (https://www.mongodb.com/try/download/community)

https://github.com/Unusualyug/Impact-pr



