from tkinter import *
import tkinter as tk
from tkinter import messagebox


def submit():
    user_inputs = [entry1.get(), entry2.get(), entry3.get(), entry4.get()]
    # Hide the current window
    root.withdraw()

    # Create a new window
    new_window = tk.Toplevel()
    new_window.title("Shapes Screen")

    # Display user inputs in the new window
    tk.Label(new_window,
             text=f"You entered:\n1. {user_inputs[0]}\n2. {user_inputs[1]}\n3. {user_inputs[2]}\n4. {user_inputs[3]}").pack(
        pady=20)

    # Create BioBrick shapes
    canvas = tk.Canvas(new_window, width=500, height=300)
    canvas.pack()

    # Draw BioBrick shapes
    y_offset = 50
    box_width = 100
    box_height = 50

    # Promoter - Curved Arrow
    canvas.create_arc(50, y_offset - 30, 150, y_offset + 70, start=180, extent=180, style=tk.ARC, outline="lightblue",
                      width=5)
    canvas.create_text(100, y_offset + 50, text="Promoter", font=("Helvetica", 12))

    # RBS - Semi-circle
    canvas.create_arc(170, y_offset - 30, 270, y_offset + 30, start=0, extent=180, fill="lightgreen")
    canvas.create_text(220, y_offset + 50, text="RBS", font=("Helvetica", 12))

    # CDS - Thick Straight Arrow
    canvas.create_line(290, y_offset, 390, y_offset, arrow=tk.LAST, fill="lightcoral", width=10)
    canvas.create_text(340, y_offset + 50, text="CDS", font=("Helvetica", 12))

    # Terminator - Thick T Shape
    canvas.create_line(410, y_offset - 25, 410, y_offset + 25, fill="lightyellow", width=10)
    canvas.create_line(380, y_offset - 25, 440, y_offset - 25, fill="lightyellow", width=10)
    canvas.create_text(425, y_offset + 50, text="Terminator", font=("Helvetica", 12))

    # Button to close the new window
    close_button = tk.Button(new_window, text="Close", command=new_window.destroy)
    close_button.pack(pady=20)


# Create the main window
root = tk.Tk()
root.title("User Input Form")

# Create and place the labels and entry fields
label1 = tk.Label(root, text="Input 1:")
label1.grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(root, text="Input 2:")
label2.grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

label3 = tk.Label(root, text="Input 3:")
label3.grid(row=2, column=0, padx=10, pady=10)
entry3 = tk.Entry(root)
entry3.grid(row=2, column=1, padx=10, pady=10)

label4 = tk.Label(root, text="Input 4:")
label4.grid(row=3, column=0, padx=10, pady=10)
entry4 = tk.Entry(root)
entry4.grid(row=3, column=1, padx=10, pady=10)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=4, column=0, columnspan=2, pady=20)

# Run the main event loop
root.mainloop()



