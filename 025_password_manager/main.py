from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

# ---------------------------- GENERATE PASSWORD ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def random_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)

    return password


def generate_password():
    password = random_password()
    password_entry.insert(END, string=password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 and len(email) == 0 and len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            saved_output = f"{website} | {email} | {password}\n"
            with open(f"passwords.txt", "a") as passwords:
                passwords.write(saved_output)
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# image
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# website
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=49)
website_entry.grid(column=1, row=1, columnspan=2)

# email/username
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry(width=49)
email_entry.grid(column=1, row=2, columnspan=2)

# password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)
password_button = Button(text="Generate Password", width=14, font=("normal", 7), command=generate_password)
password_button.grid(column=2, row=3)

# add button
add_button = Button(text="Add", width=48, font=("normal", 7), command=add_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
