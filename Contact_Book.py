import json
import tkinter as tk
from tkinter import messagebox

class ContactBookGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")

        self.contacts = []

        self.load_contacts()

        self.create_widgets()

    def load_contacts(self):
        try:
            with open("contact_book.json", 'r') as f:
                self.contacts = json.load(f)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Invalid JSON format in the file.")

    def save_contacts(self):
        with open("contact_book.json", 'w') as f:
            json.dump(self.contacts, f, indent=4)

    def create_widgets(self):
        self.contact_listbox = tk.Listbox(self.master, width=50)
        self.contact_listbox.grid(row=0, column=0, padx=10, pady=10, rowspan=5)

        self.scrollbar = tk.Scrollbar(self.master, orient="vertical")
        self.scrollbar.config(command=self.contact_listbox.yview)
        self.scrollbar.grid(row=0, column=1, sticky="NSW", pady=10, rowspan=5)

        self.contact_listbox.config(yscrollcommand=self.scrollbar.set)

        self.refresh_contacts()

        self.add_button = tk.Button(self.master, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=0, column=2, padx=10, pady=10)

        self.edit_button = tk.Button(self.master, text="Edit Contact", command=self.edit_contact)
        self.edit_button.grid(row=1, column=2, padx=10, pady=10)

        self.delete_button = tk.Button(self.master, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=2, column=2, padx=10, pady=10)

    def refresh_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, contact['name'])

    def add_contact(self):
        add_window = tk.Toplevel(self.master)
        add_window.title("Add Contact")

        tk.Label(add_window, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(add_window, text="Phone Number:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(add_window, text="Email:").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(add_window, text="Address:").grid(row=3, column=0, padx=10, pady=5)

        name_entry = tk.Entry(add_window)
        phone_entry = tk.Entry(add_window)
        email_entry = tk.Entry(add_window)
        address_entry = tk.Entry(add_window)

        name_entry.grid(row=0, column=1, padx=10, pady=5)
        phone_entry.grid(row=1, column=1, padx=10, pady=5)
        email_entry.grid(row=2, column=1, padx=10, pady=5)
        address_entry.grid(row=3, column=1, padx=10, pady=5)

        add_button = tk.Button(add_window, text="Add", command=lambda: self.save_new_contact(name_entry.get(), phone_entry.get(), email_entry.get(), address_entry.get()))
        add_button.grid(row=4, column=1, padx=10, pady=10)

    def save_new_contact(self, name, phone, email, address):
        new_contact = {'name': name, 'phone_number': phone, 'email': email, 'address': address}
        self.contacts.append(new_contact)
        self.save_contacts()
        self.refresh_contacts()

    def edit_contact(self):
        selected_index = self.contact_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Warning", "Please select a contact to edit.")
            return
        selected_index = selected_index[0]

        edit_window = tk.Toplevel(self.master)
        edit_window.title("Edit Contact")

        tk.Label(edit_window, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(edit_window, text="Phone Number:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(edit_window, text="Email:").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(edit_window, text="Address:").grid(row=3, column=0, padx=10, pady=5)

        name_entry = tk.Entry(edit_window)
        phone_entry = tk.Entry(edit_window)
        email_entry = tk.Entry(edit_window)
        address_entry = tk.Entry(edit_window)

        name_entry.grid(row=0, column=1, padx=10, pady=5)
        phone_entry.grid(row=1, column=1, padx=10, pady=5)
        email_entry.grid(row=2, column=1, padx=10, pady=5)
        address_entry.grid(row=3, column=1, padx=10, pady=5)

        contact_to_edit = self.contacts[selected_index]
        name_entry.insert(0, contact_to_edit['name'])
        phone_entry.insert(0, contact_to_edit['phone_number'])
        email_entry.insert(0, contact_to_edit['email'])
        address_entry.insert(0, contact_to_edit['address'])

        update_button = tk.Button(edit_window, text="Update", command=lambda: self.update_contact(selected_index, name_entry.get(), phone_entry.get(), email_entry.get(), address_entry.get()))
        update_button.grid(row=4, column=1, padx=10, pady=10)

    def update_contact(self, index, name, phone, email, address):
        updated_contact = {'name': name, 'phone_number': phone, 'email': email, 'address': address}
        self.contacts[index] = updated_contact
        self.save_contacts()
        self.refresh_contacts()

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Warning", "Please select a contact to delete.")
            return
        selected_index = selected_index[0]

        confirm_delete = messagebox.askyesno("Delete Contact", "Are you sure you want to delete this contact?")
        if confirm_delete:
            del self.contacts[selected_index]
            self.save_contacts()
            self.refresh_contacts()

def main():
    root = tk.Tk()
    app = ContactBookGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
