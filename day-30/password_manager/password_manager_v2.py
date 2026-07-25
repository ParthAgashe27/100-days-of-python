from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [random.choice(letters) for i in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for i in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for i in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #

file_path = "data.json"

def save():
    website = website_input.get()
    email_username = email_username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email_username,
            "password": password,

        }
    }

    if len(website) < 1 or len(email_username) < 1 or len(password) < 1:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!!")
    else:                
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:{email_username}"
                                                              f"\nPassword:{password} \nIs it ok to save?")
            
        if is_ok:
            try:
                with open(file_path, "r") as file:
                    #Reading old data
                    data = json.load(file)
            except FileNotFoundError:
                with open(file_path, "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                #Updating old data with new data
                data.update(new_data)
                with open(file_path, "w") as file:
                    #Saving updated data
                    json.dump(data, file, indent=4)
            finally:
                website_input.delete(0, END)
                email_username_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_input.get()
    try:
        with open(file_path) as file:
            data = json.load(file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found")
    else:        
        if website in data :
            email =  data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=70, pady=70)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=1, column=2)

# ---------------------------- LABELS ------------------------------- #

website_label = Label(text="Website: ")
website_label.grid(row=2, column=1)

email_username_label = Label(text="Email/Username: ")
email_username_label.grid(row=3, column=1)

password_label = Label(text="Password: ")
password_label.grid(row=4, column=1)

# ---------------------------- INPUTS ------------------------------- #

website_input = Entry(width=32)
website_input.grid(row=2, column=2, )
website_input.focus()

email_username_input = Entry(width=52)
email_username_input.grid(row=3, column=2, columnspan=2)

password_input = Entry(width=32)
password_input.grid(row=4, column=2, sticky="")

# ---------------------------- BUTTONS ------------------------------- #

generate_password_button = Button(text="Generate Password", width=15, command=generate_password)
generate_password_button.grid(row=4, column=3)

search_button = Button(text="Search", width= 15, command=find_password)
search_button.grid(row=2, column=3)

add_button = Button(text="Add", width= 44, command=save)
add_button.grid(row=5, column=2, columnspan=2)


window.mainloop()
