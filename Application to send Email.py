import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import messagebox, colorchooser
import re  # Import the regular expressions module
from email.utils import formataddr
import hashlib  # Import the hashlib 

# validation of email Address
def is_valid_email(email):
    
    #  checking if the email address is in valid format
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

# ... Your other GUI code ...

def hash_password(password):
    salt = b'7a8f1d3e7b5c9a2e'  # Replace with a secure random salt
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return hashed

def send_email():
    sender_email = sender_entry.get()
    password = password_entry.get()
    rec_email = rec_email_entry.get()
    message = message_text.get("1.0", "end-1c")  # Get message from Text widget

    # Securely hash the password
    hashed_password = hash_password(password)

    # Convert the hashed password to a hex string
    hashed_password_str = hashed_password.hex()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender_email, hashed_password_str)  # Use the string representation of the hashed password
        print("Login success")

        server.sendmail(sender_email, rec_email, message)
        print("Email has been sent to", rec_email)
        messagebox.showinfo("Email Sent", "Email has been sent successfully.")
    except Exception as e:
        print("An error occurred:", e)
        messagebox.showerror("Error", "An error occurred while sending the email.")
    finally:
        server.quit()
        print("Server closed")

# ... Rest of your GUI code ...






    
    root.update_idletasks()  # Update the GUI
# Create the GUI window
root = tk.Tk()
root.title("Email Sender")

# Styling
root.geometry("400x550")

# Header Label
header_label = tk.Label(root, text="Email Sender", font=("Helvetica", 20), bg="#f0f0f0")
header_label.grid(row=0, column=0, columnspan=2, pady=10)

# Recipient Email Entry
rec_email_label = tk.Label(root, text="Recipient Email:", bg="#f0f0f0")
rec_email_label.grid(row=1, column=0, sticky="w", padx=10)
rec_email_entry = tk.Entry(root, font=("Helvetica", 12))
rec_email_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Sender Email Entry
sender_label = tk.Label(root, text="Sender Email:", bg="#f0f0f0")
sender_label.grid(row=2, column=0, sticky="w", padx=10)
sender_entry = tk.Entry(root, font=("Helvetica", 12))
sender_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Password Entry
password_label = tk.Label(root, text="Password:", bg="#f0f0f0")
password_label.grid(row=3, column=0, sticky="w", padx=10)
password_entry = tk.Entry(root, show="*", font=("Helvetica", 12))
password_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

# Compose Message Label
message_label = tk.Label(root, text="Compose Message", font=("Helvetica", 18), bg="#f0f0f0")
message_label.grid(row=4, column=0, columnspan=2, pady=10)

# Message Text Entry
message_text = tk.Text(root, font=("Helvetica", 12), wrap="word", height=10, width=40)
message_text.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Status Message Label
status_label = tk.Label(root, text="", bg="#f0f0f0")
status_label.grid(row=9, column=0, columnspan=2, pady=5)

# Send Email Button
send_button = tk.Button(root, text="Send Email", command=send_email, bg="#007acc", fg="white", font=("Helvetica", 12))
send_button.grid(row=10, column=0, columnspan=2, pady=20)

# Start the GUI event loop
root.mainloop()



