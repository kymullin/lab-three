from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
from tkinter.ttk import Progressbar
import time
import threading
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("/home/admin/lab-three/Automated Ocarina/assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Function to update the progress bar
def run_progress(duration):
    for i in range(101):
        progress_bar['value'] = i
        window.after(10, update_progress)  # Schedule progress update every 10ms to keep UI responsive
        time.sleep(duration / 100)  # Simulate long task with time delay
    progress_bar['value'] = 0  # Reset progress bar once done

# Function that allows progress to update smoothly using window.after()
def update_progress():
    window.update_idletasks()  # Keep the UI responsive during progress updates

def on_button_click(duration, midi_file):
    # Start the progress bar in a separate thread to avoid UI freezing
    threading.Thread(target=run_progress, args=(duration,)).start()
    # Call the external Python file with the MIDI file as an argument
    subprocess.Popen(["python3", "CaseStatements.py", midi_file])  # Adjust the path as needed

# Create the main window
window = Tk()

# Get screen size and set window to fullscreen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")
window.attributes('-fullscreen', True)  # Set fullscreen mode
window.configure(bg="#FFFFFF")

# Create a canvas
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=screen_height,
    width=screen_width,
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
    command=lambda: on_button_click(5, "twinkle.mid"),  # Example MIDI file
    relief="flat"
)
button_1.place(
    x=121.0,
    y=144.0,
    width=457.0,
    height=120.0  # Increased button height for better touch usability
)

# Button 2 (10 seconds)
button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_button_click(10, "wheels_on_the_bus.mid"),  # Example MIDI file
    relief="flat"
)
button_2.place(
    x=121.0,
    y=274.0,  # Increased space between buttons
    width=457.0,
    height=120.0  # Increased button height
)

# Button 3 (15 seconds)
button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_button_click(15, "heart_and_soul.mid"),  # Example MIDI file
    relief="flat"
)
button_3.place(
    x=122.0,
    y=404.0,  # Increased space between buttons
    width=457.0,
    height=120.0  # Increased button height
)

# Create a red rectangle header
canvas.create_rectangle(
    0.0,
    0.0,
    screen_width,
    110.0,
    fill="#B30000",
    outline=""
)

# Create title text
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
progress_bar.place(x=100, y=screen_height - 50)  # Position the progress bar towards the bottom

# Run the Tkinter loop
window.resizable(False, False)
window.mainloop()
