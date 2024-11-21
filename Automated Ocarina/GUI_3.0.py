from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
from tkinter.ttk import Progressbar
import time
import threading
import subprocess

# Adjust asset paths
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets/frame0")  # Remove leading slash to make it relative

# Helper function to get relative paths for assets
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Function to run the progress bar
def run_progress(duration):
    for i in range(101):
        progress_bar['value'] = i
        time.sleep(duration / 100)  # Progress bar updates in steps proportional to the total duration
    progress_bar['value'] = 0  # Reset progress bar once done

# Function to handle button click: play MIDI and update progress bar
def on_button_click(duration, midi_file):
    # Start the progress bar in a separate thread to avoid freezing the GUI
    threading.Thread(target=run_progress, args=(duration,)).start()
    # Call the external Python file with the MIDI file as an argument
    midi_file_path = relative_to_assets(midi_file)  # Get the correct path to the MIDI file
    print(f"Playing MIDI file: {midi_file_path}")
    subprocess.Popen(["python3", "CaseStatements.py", str(midi_file_path)])  # Adjust the path as needed

# Create the main window
window = Tk()
window.geometry("700x550")
window.configure(bg="#FFFFFF")

# Create the canvas
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=550,
    width=700,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Button 1 (5 seconds)
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_button_click(5, "twinkle.mid"),  # Change this to your actual MIDI file
    relief="flat"
)
button_1.place(
    x=121.0,
    y=144.0,
    width=457.0,
    height=88.0
)

# Button 2 (10 seconds)
button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_button_click(10, "wheels_on_the_bus.mid"),  # Change this to your actual MIDI file
    relief="flat"
)
button_2.place(
    x=121.0,
    y=261.0,
    width=457.0,
    height=88.0
)

# Button 3 (15 seconds)
button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_button_click(15, "heart_and_soul.mid"),  # Change this to your actual MIDI file
    relief="flat"
)
button_3.place(
    x=122.0,
    y=395.0,
    width=457.0,
    height=88.0
)

# Create a red header rectangle
canvas.create_rectangle(
    0.0,
    0.0,
    700.0,
    110.0,
    fill="#B30000",
    outline=""
)

# Create the title text
canvas.create_text(
    110.0,
    29.0,
    anchor="nw",
    text="Song Selector",
    fill="#FFFFFF",
    font=("Inter Bold", 64 * -1)
)

# Create the progress bar
progress_bar = Progressbar(window, orient="horizontal", length=500, mode="determinate")
progress_bar.place(x=100, y=500)

# Make the window non-resizable
window.resizable(False, False)

# Run the Tkinter main loop
window.mainloop()
