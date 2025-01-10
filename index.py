import tkinter as tk
from pymongo import MongoClient
from style import create_ui

client = MongoClient("mongodb://localhost:27017/Contact")
db = client.phonebook  
collection = db.contacts  

def display_contacts(listbox, error_label):
    listbox.delete(0, tk.END)
    contacts = collection.find()  
    contact_list = list(contacts)  
    
    if len(contact_list) > 0:
        for contact in contact_list:
            listbox.insert(tk.END, f"{contact['name']} --> {contact['phone']}")
        error_label.config(text=f"Total contacts: {len(contact_list)}")
    else:
        listbox.insert(tk.END, "You have an empty phonebook!")
        error_label.config(text="No contacts found.")

def add_contact(contact_name, phone_number, listbox, error_label):
    if not contact_name or not phone_number:
        error_label.config(text="Name and phone number cannot be empty!")
        return
    
    if collection.find_one({"phone": phone_number}):
        error_label.config(text="Contact already exists with this phone number!")
    elif collection.find_one({"name": contact_name}):
        error_label.config(text="Contact name already exists! Use another name.")
    else:
        collection.insert_one({"name": contact_name, "phone": phone_number})
        error_label.config(text=f"Contact added: {contact_name} --> {phone_number}")
        display_contacts(listbox, error_label)
        clear_fields()

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

def delete_contact(contact_name, listbox, error_label):
    if not contact_name:
        error_label.config(text="Please enter a name to delete.")
        return
    
    contact = collection.find_one({"name": contact_name})
    if contact:
        collection.delete_one({"name": contact_name})
        error_label.config(text=f"Contact '{contact_name}' deleted.")
        display_contacts(listbox, error_label)
    else:
        error_label.config(text="Contact not found!")

def search_contact(search_term, listbox, error_label):
    listbox.delete(0, tk.END)
    contacts = collection.find({"name": {"$regex": search_term, "$options": "i"}})
    contact_list = list(contacts)
    
    if len(contact_list) > 0:
        for contact in contact_list:
            listbox.insert(tk.END, f"{contact['name']} --> {contact['phone']}")
        error_label.config(text=f"Total search results: {len(contact_list)}")
    else:
        error_label.config(text="No contacts found!")

def edit_contact(contact_name, new_name, new_phone, listbox, error_label):
    if not contact_name or not new_name or not new_phone:
        error_label.config(text="All fields must be filled!")
        return

    contact = collection.find_one({"name": contact_name})
    if contact:
        collection.update_one(
            {"name": contact_name},
            {"$set": {"name": new_name, "phone": new_phone}}
        )
        error_label.config(text=f"Contact '{contact_name}' updated to {new_name} --> {new_phone}")
        display_contacts(listbox, error_label)
        clear_fields()
    else:
        error_label.config(text="Contact not found!")

def sort_contacts(listbox, error_label, sort_by="name"):
    listbox.delete(0, tk.END)
    if sort_by == "name":
        contacts = collection.find().sort("name", 1)
    elif sort_by == "phone":
        contacts = collection.find().sort("phone", 1)

    contact_list = list(contacts)
    for contact in contact_list:
        listbox.insert(tk.END, f"{contact['name']} --> {contact['phone']}")
    
    error_label.config(text=f"Contacts sorted by {sort_by}.")

def toggle_contacts(listbox, error_label, contacts_shown):
    if contacts_shown:
        listbox.delete(0, tk.END)
    else:
        display_contacts(listbox, error_label)
    return not contacts_shown

root = tk.Tk()
root.title("Phonebook App")

entry_name, entry_phone, listbox, error_label, entry_search, search_button, show_button, entry_new_name, entry_new_phone, edit_button = create_ui(
    root, add_contact, delete_contact, display_contacts, search_contact, toggle_contacts, edit_contact, sort_contacts
)

contacts_shown = False

show_button.config(command=lambda: toggle_contacts(listbox, error_label, contacts_shown))

root.mainloop()
