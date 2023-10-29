from tkinter import *
import pyshorteners
from tkinter import messagebox

# Function to shorten the URL and display it
def shorten_url():
    user_input = url_entry.get()
    if user_input == "":
        # Show a message box if the URL field is empty
        messagebox.showinfo("Alert", "Text field is empty")
    else:
        # Shorten the URL and insert it in the result field
        result = pyshorteners.Shortener().tinyurl.short(user_input)
        shortened_url_entry.insert(END, result)

# Create the main Tkinter window
root = Tk()
root.title("URL Shortener")
root.geometry("900x300")

# Create and display a label
Label(root, text="Generate Short URL", font=("Georgia 25 bold"), fg="purple").pack(pady=10)

# Create a frame for the URL input field
input_frame = Frame(root)
Label(input_frame, text="Paste URL Here: ", font=("Georgia 25 bold")).pack(side=LEFT)
url_entry = Entry(input_frame, width=24, font=("Georgia 25 bold"))
url_entry.pack()  # Separate widget creation and packing
input_frame.pack(pady=10)

# Create a button to generate the short URL
generate_button = Button(root, text="Generate Link", font=("Georgia 25 bold"), command=shorten_url)
generate_button.pack(pady=10)

# Create a frame for displaying the shortened URL
output_frame = Frame(root)
Label(output_frame, text="Copy URL: ", font=("Georgia 25 bold")).pack(side=LEFT)
shortened_url_entry = Entry(output_frame, width=24, fg="blue", font=("Georgia 25 bold"))
shortened_url_entry.pack()  # Separate widget creation and packing
output_frame.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()