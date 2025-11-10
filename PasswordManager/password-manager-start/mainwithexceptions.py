from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    password = password_letters + password_symbols + password_numbers
    shuffle(password)
    your_password = "".join(password)

    password_entry.insert(0, your_password)
    pyperclip.copy(your_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password,
        }
    }
    if website == "" or password == "":
        messagebox.showinfo(title="Error", message="Please fill all fields")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
        finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD  ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title= f"{website}", message=f"Email: {email} \n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message= f"No details for {website} found")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 100, pady =100, bg = "white")

canvas = Canvas(width = 200, height = 200, bg = "white", highlightthickness = 0)
image_file = PhotoImage(file = "logo.png")
canvas.create_image(100,100,image = image_file)
canvas.grid(row = 0, column = 1)

website_label= Label(text="Website:   ", bg = "white", fg = "black")
website_label.grid(row = 1, column = 0)
email_label= Label(text = "Email/Username:",bg = "white", fg = "black")
email_label.grid(column = 0,row = 2)
password_label= Label(text = "Password:",bg = "white", fg = "black")
password_label.grid(column = 0,row = 3)


website_entry = Entry(width = 21, bg = "white", fg = "black")
website_entry.focus()
website_entry.grid(column = 1,row = 1)

email_entry = Entry(width = 35, bg = "white", fg = "black")
email_entry.grid(column = 1,row = 2, columnspan = 2)
email_entry.insert(0, "ashita@gmail.com")
password_entry = Entry(width = 21, bg = "white", fg = "black")
password_entry.grid(column = 1,row = 3)

add_button = Button(text = "Add", width = 32, command = save_data)
add_button.grid(column = 1, row = 4, columnspan = 2)

search_button = Button(width = 10, text = "Search", command=find_password)
search_button.grid(column = 2, row = 1)

generate_button = Button(width = 10, text = "Generate Password", command=password_generator)
generate_button.grid(column = 2, row = 3)


window.mainloop()