import customtkinter as ctk
from PIL import Image, ImageTk, ImageDraw, ImageFilter
import random, string
from tkinter import messagebox

# ---------- Password Functions ----------
def generate_password():
    try:
        length = int(entry_length.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    entry_password.delete(0, "end")
    entry_password.insert(0, password)

def copy_password():
    password = entry_password.get()
    if password:
        app.clipboard_clear()
        app.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

# ---------- UI Setup ----------
ctk.set_appearance_mode("light")
app = ctk.CTk()
app.title("✨ Password Generator")
app.geometry("700x500")
app.resizable(False, False)

# Gradient background (instead of raw image)
gradient = Image.new("RGB", (700, 500), "#6a5acd")
draw = ImageDraw.Draw(gradient)
for i in range(500):
    color = (106, 90, 205 + i//5) if i < 250 else (46, 139, 87 + i//10)
    draw.line([(0, i), (700, i)], fill=color)
gradient = gradient.filter(ImageFilter.GaussianBlur(8))
bg_photo = ImageTk.PhotoImage(gradient)

bg_label = ctk.CTkLabel(master=app, image=bg_photo, text="")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Title
title = ctk.CTkLabel(master=app, text="🔑 Professional Password Generator",
                     font=("Poppins", 24, "bold"), text_color="green")
title.place(relx=0.5, y=50, anchor="center")

# Entry for length
entry_length = ctk.CTkEntry(master=app,
                            placeholder_text="Password length",
                            width=280, height=50,
                            corner_radius=25,
                            fg_color=("white", "white"),
                            text_color="black",
                            font=("Poppins", 14))
entry_length.place(relx=0.5, y=130, anchor="center")

# Generate Button
btn_generate = ctk.CTkButton(master=app, text="Generate",
                             command=generate_password,
                             corner_radius=30, height=50,
                             font=("Poppins", 15, "bold"),
                             fg_color="#6a5acd", hover_color="#5840a0")
btn_generate.place(relx=0.5, y=200, anchor="center")

# Password Output
entry_password = ctk.CTkEntry(master=app,
                              placeholder_text="Your password will appear here",
                              width=350, height=50, corner_radius=25,
                              fg_color=("white", "white"),
                              text_color="black",
                              font=("Poppins", 14))
entry_password.place(relx=0.5, y=270, anchor="center")

# Copy Button
btn_copy = ctk.CTkButton(master=app, text="Copy Password",
                         command=copy_password,
                         corner_radius=30, height=50,
                         font=("Poppins", 15, "bold"),
                         fg_color="#2e8b57", hover_color="#1e5d3b")
btn_copy.place(relx=0.5, y=340, anchor="center")

# Footer
footer = ctk.CTkLabel(master=app, text="Designed by Nimra",
                      font=("Calibri Light", 12), text_color="blue")
footer.place(relx=0.5, y=470, anchor="center")

app.mainloop()
