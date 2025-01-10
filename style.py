import tkinter as tk

def create_ui(root, add_contact, delete_contact, display_contacts, search_contact, toggle_contacts, edit_contact, sort_contacts):
    # Create UI components
    
    # Name label and entry
    name_label = tk.Label(root, text="Contact Name:")
    name_label.pack(pady=5)
    entry_name = tk.Entry(root, width=30)
    entry_name.pack(pady=5)
    
    # Phone number label and entry
    phone_label = tk.Label(root, text="Phone Number:")
    phone_label.pack(pady=5)
    entry_phone = tk.Entry(root, width=30)
    entry_phone.pack(pady=5)
    
    # New name label and entry for editing
    new_name_label = tk.Label(root, text="New Name (for Edit):")
    new_name_label.pack(pady=5)
    entry_new_name = tk.Entry(root, width=30)
    entry_new_name.pack(pady=5)
    
    # New phone number label and entry for editing
    new_phone_label = tk.Label(root, text="New Phone Number (for Edit):")
    new_phone_label.pack(pady=5)
    entry_new_phone = tk.Entry(root, width=30)
    entry_new_phone.pack(pady=5)
    
    # Listbox to display contacts
    listbox = tk.Listbox(root, width=50, height=15)
    listbox.pack(pady=10)

    # Error message label
    error_label = tk.Label(root, text="", fg="red")
    error_label.pack(pady=10)

    # Add Contact Button
    add_button = tk.Button(
        root, text="Add Contact", width=20, 
        command=lambda: add_contact(entry_name.get(), entry_phone.get(), listbox, error_label)
    )
    add_button.pack(pady=5)

    # Delete Contact Button
    delete_button = tk.Button(
        root, text="Delete Contact", width=20, 
        command=lambda: delete_contact(entry_name.get(), listbox, error_label)
    )
    delete_button.pack(pady=5)

    # Search Bar and Button
    entry_search = tk.Entry(root, width=30)
    entry_search.pack(pady=10)

    search_button = tk.Button(
        root, text="Search Contact", width=20,
        command=lambda: search_contact(entry_search.get(), listbox, error_label)
    )
    search_button.pack(pady=5)

    # Edit Contact Button
    edit_button = tk.Button(
        root, text="Edit Contact", width=20,
        command=lambda: edit_contact(entry_name.get(), entry_new_name.get(), entry_new_phone.get(), listbox, error_label)
    )
    edit_button.pack(pady=5)

    # Sort Contacts Button
    sort_button = tk.Button(
        root, text="Sort by Name", width=20,
        command=lambda: sort_contacts(listbox, error_label, sort_by="name")
    )
    sort_button.pack(pady=5)

    # Show/Hide Contacts Button
    show_button = tk.Button(
        root, text="Show Contacts", width=20
    )
    show_button.pack(pady=5)

    return entry_name, entry_phone, listbox, error_label, entry_search, search_button, show_button, entry_new_name, entry_new_phone, edit_button
