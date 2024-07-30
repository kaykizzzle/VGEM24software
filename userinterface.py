import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import BooleanVar, Checkbutton, StringVar, OptionMenu, Radiobutton


def toggle_key_molecule():
    if toggle_var.get():
        key_molecule_label.grid_remove()
        key_molecule_entry.grid_remove()
        regulation_label.grid_remove()
        positive_regulation.grid_remove()
        negative_regulation.grid_remove()
    else:
        key_molecule_label.grid()
        key_molecule_entry.grid()
        regulation_label.grid()
        positive_regulation.grid()
        negative_regulation.grid()


def submit():
    organism = organism_var.get()
    user_inputs = [organism, entry2.get(), entry3.get(), entry4.get()]
    constitutively_active = "Yes" if toggle_var.get() else "No"
    key_molecule = key_molecule_entry.get() if not toggle_var.get() else "N/A"
    regulation_type = regulation_var.get() if not toggle_var.get() else "N/A"

    # Hide the current window
    root.withdraw()

    # Create a new window
    new_window = tk.Toplevel()
    new_window.title("Shapes Screen")

    # Add title to the new window
    tk.Label(new_window, text="BioBricker", font=("Helvetica", 16, "bold")).pack(pady=10)

    # Display user inputs in the new window
    # tk.Label(new_window,
    # text=f"You entered:\n1. Organism: {user_inputs[0]}\n2. {user_inputs[1]}\n3. {user_inputs[2]}\n4. {user_inputs[3]}\nConstitutively active: {constitutively_active}\nKey molecule: {key_molecule}\nRegulation: {regulation_type}",
    # bg='white').pack(pady=20)

    # Create BioBrick shapes
    canvas = tk.Canvas(new_window, width=500, height=300)
    canvas.pack()

    # Draw BioBrick shapes
    y_offset = 50
    box_width = 100
    box_height = 50

    # Promoter - Arrow pointing up and to the right
    canvas.create_line(90, y_offset - 25, 90, y_offset + 25, fill="lightblue", width=15)
    canvas.create_line(82.45, y_offset - 25, 135, y_offset - 25, fill="lightblue", width=15)
    canvas.create_polygon(135, y_offset - 40, 135, y_offset - 10, 155, y_offset - 25, fill="lightblue")
    canvas.create_text(100, y_offset + 50, text="Promoter", font=("Helvetica", 12))

    # RBS - Semi-circle
    canvas.create_arc(160, y_offset + 50, 240, y_offset - 0, start=0, extent=180, fill="lightgreen")
    canvas.create_text(200, y_offset + 50, text="RBS", font=("Helvetica", 12))

    # CDS - Thick Straight Arrow
    canvas.create_line(260, y_offset + 15, 360, y_offset + 15, arrow=tk.LAST, fill="lightcoral", width=20)
    canvas.create_text(310, y_offset + 50, text="CDS", font=("Helvetica", 12))

    # Terminator - Thick T Shape
    canvas.create_line(400, y_offset - 25, 400, y_offset + 25, fill="yellow", width=15)
    canvas.create_line(370, y_offset - 25, 430, y_offset - 25, fill="yellow", width=15)
    canvas.create_text(400, y_offset + 50, text="Terminator", font=("Helvetica", 12))

    # Button to close the new window
    close_button = tk.Button(new_window, text="Close", command=new_window.destroy)
    close_button.pack(pady=20)


# Create the main window
root = tk.Tk()
root.title("User Input Form")

# Add title to the main window
tk.Label(root, text="BioBricker", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

# Create and place the dropdown for "Organism"
organism_var = StringVar()
organism_var.set("Select your organism")  # Default value

organisms = ["E. coli", "S. cerevisiae", "Lactobacillus spp.", "Bacillus subtilis"]
organism_label = tk.Label(root, text="Organism")
organism_label.grid(row=1, column=0, padx=10, pady=10)
organism_menu = OptionMenu(root, organism_var, *organisms)
organism_menu.config(width=20)  # Set fixed width for the dropdown
organism_menu.grid(row=1, column=1, padx=15, pady=15)

# Create and place the labels and entry fields
label2 = tk.Label(root, text="Coding Sequence")
label2.grid(row=2, column=0, padx=10, pady=10)
entry2 = tk.Entry(root)
entry2.grid(row=2, column=1, padx=10, pady=10)

label3 = tk.Label(root, text="Input 3")
label3.grid(row=3, column=0, padx=10, pady=10)
entry3 = tk.Entry(root)
entry3.grid(row=3, column=1, padx=10, pady=10)

label4 = tk.Label(root, text="Input 4")
label4.grid(row=4, column=0, padx=10, pady=10)
entry4 = tk.Entry(root)
entry4.grid(row=4, column=1, padx=10, pady=10)

# Create and place the toggle for "Constitutively active"
toggle_var = BooleanVar()
toggle_var.trace_add("write", lambda *args: toggle_key_molecule())
toggle = Checkbutton(root, text="Constitutively active", variable=toggle_var)
toggle.grid(row=5, column=0, columnspan=2, pady=10)

# Create and place the label and entry for "Key molecule"
key_molecule_label = tk.Label(root, text="Key molecule")
key_molecule_entry = tk.Entry(root)

key_molecule_label.grid(row=6, column=0, padx=10, pady=10)
key_molecule_entry.grid(row=6, column=1, padx=10, pady=10)

# Create and place the regulation type switch
regulation_var = StringVar()
regulation_var.set("Positive regulation")  # Default value

regulation_label = tk.Label(root, text="Regulation:", bg='white')
positive_regulation = Radiobutton(root, text="Positive", variable=regulation_var, value="Positive regulation",
                                  bg='white')
negative_regulation = Radiobutton(root, text="Negative", variable=regulation_var, value="Negative regulation",
                                  bg='white')

regulation_label.grid(row=7, column=0, padx=10, pady=10)
positive_regulation.grid(row=7, column=1, padx=(10, 5), pady=10, sticky='w')
negative_regulation.grid(row=7, column=1, padx=(95, 10), pady=10, sticky='w')

# Initially hide the "Key molecule" fields if constitutively active is toggled on
toggle_key_molecule()

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=9, column=0, columnspan=2, pady=20)

# Run the main event loop
root.mainloop()
