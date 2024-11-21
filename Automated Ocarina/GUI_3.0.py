from pathlib import Path
from tkinter import Tk, Canvas, Button
from tkinter.ttk import Progressbar
import time
import threading
import subprocess

# Correct path handling for assets
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("/home/admin/lab-three/Automated Ocarina/assets/frame0")  # Adjust path

# Helper function to get relative paths for assets
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Function to update the progress bar
def run_progress(duration):
    for i in range(101):
        progress_bar['value'] = i
        time.sleep(duration / 100)  # Progress bar updates in steps proportional to the total duration
    progress_bar['value'] = 0  # Reset progress bar once done

# Function to handle button click: play MIDI and update progress bar
def on_button_click(duration, midi_file):
    # Start the progress bar in a separate thread
    threading.Thread(target=run_progress, args=(duration,)).start()
    # Call the external Python file with the MIDI file as an argument
    midi_file_path = relative_to_assets(midi_file)  # Get the correct path to the MIDI file
    print(f"Playing MIDI file: {midi_file_path}")
    subprocess.Popen(["python3", "CaseStatements.py", str(midi_file_path)])  # Adjust path if necessary

# Create the main window
window = Tk()
window.geometry("700x550")
window.configure(bg="#FFFFFF")

# Create the canvas (background)
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

# Button 1 (for example, Twinkle Twinkle with 5 seconds of progress bar duration)
button_1 = Button(
    window,
    text="Twinkle Twinkle Little Star",  # Button text
    command=lambda: on_button_click(5, "twinkle.mid"),  # Call function with 5 seconds and MIDI file
    font=("Helvetica", 14),
    bg="#FF0000",  # Red background color
    fg="white",
    bd=5,
    relief="raised",
    width=20,
    height=2
)
button_1.place(x=121, y=144, width=457, height=88)

# Button 2 (for example, Wheels on the Bus with 10 seconds of progress bar duration)
button_2 = Button(
    window,
    text="Wheels on the Bus",
    command=lambda: on_button_click(10, "wheels_on_the_bus.mid"),
    font=("Helvetica", 14),
    bg="#FF5733",  # Orange background color
    fg="white",
    bd=5,
    relief="raised",
    width=20,
    height=2
)
button_2.place(x=121, y=261, width=457, height=88)

# Button 3 (for example, Heart and Soul with 15 seconds of progress bar duration)
button_3 = Button(
    window,
    text="Heart and Soul",
    command=lambda: on_button_click(15, "heart_and_soul.mid"),
    font=("Helvetica", 14),
    bg="#FF9800",  # Yellow background color
    fg="white",
    bd=5,
    relief="raised",
    width=20,
    height=2
)
button_3.place(x=122, y=395, width=457, height=88)

# Create a rectangle for the header section
canvas.create_rectangle(
    0.0,
    0.0,
    700.0,
    110.0,
    fill="#B30000",  # Red color for the header
    outline=""
)

# Create the title text
canvas.create_text(
    110.0,
    29.0,
    anchor="nw",
    text="Song Selector",  # Title text
    fill="#FFFFFF",  # White text color
    font=("Helvetica", 32, "bold")
)

# Create the progress bar
progress_bar = Progressbar(window, orient="horizontal", length=500, mode="determinate")
progress_bar.place(x=100, y=500)

# Make the window non-resizable
window.resizable(False, False)

# Start the Tkinter event loop
window.mainloop()
