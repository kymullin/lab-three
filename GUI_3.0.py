import tkinter as tk
import subprocess
from pathlib import Path

# Correct path handling
OUTPUT_PATH = Path(__file__).parent  # Path of the current script
ASSETS_PATH = OUTPUT_PATH / "home/admin/lab-three/Automated Ocarina"  # Fix path concatenation

# Function to handle button click
def on_button_click(song_name):
    print(f"{song_name} Button Clicked!")
    # Call the subprocess to run CaseStatements.py with the corresponding MIDI file
    play_midi(song_name)

# Function to run the external Python script with the MIDI file as an argument
def play_midi(song_name):
    # Dictionary of songs to their respective MIDI files
    midi_files = {
        "Twinkle Twinkle Little Star": "twinkle_twinkle.mid",
        "Wheels on the Bus": "wheels_on_the_bus.mid",
        "Heart and Soul": "heart_and_soul.mid",
        "Tetris": "tetris.mid",
        "Jingle Bells": "jingle_bells.mid"
    }
    
    # Get the corresponding MIDI file based on the song name
    midi_file = midi_files.get(song_name)
    
    if midi_file:
        print(f"Calling CaseStatements.py with {midi_file}")
        try:
            # Construct the full path to the MIDI file
            midi_file_path = ASSETS_PATH / midi_file
            print(f"MIDI file path: {midi_file_path}")
            
            # Call the external script with the MIDI file as an argument using subprocess
            subprocess.Popen(["python3", "CaseStatements.py", str(midi_file_path)])  # Adjust path if necessary
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"Song {song_name} not found in the list.")

# Create the main window
root = tk.Tk()
root.title("Song Selector")

# Set the window size
root.geometry("400x600")

# Set a vibrant background color for the window
root.configure(bg="#474747")

# Frame for the title to create a colored box effect
title_frame = tk.Frame(root, bg="#3F51B5", bd=5)
title_frame.pack(fill="x", pady=20)

# Add the title label inside the colored box
title_label = tk.Label(title_frame, text="Song Selector", font=("Helvetica", 20, "bold"), fg="white", bg="#3F51B5")
title_label.pack(pady=10)

# Style for the button
def create_button(text, bg_color, command):
    return tk.Button(
        root, 
        text=text, 
        command=command,
        font=("Helvetica", 14, "bold"),
        bg=bg_color, 
        fg="white", 
        bd=5, 
        relief="raised", 
        width=20, 
        height=2,
        activebackground="#4CAF50",  # Darker green when pressed
        activeforeground="yellow"  # Yellow text when pressed
    )

# Create the buttons with different colors and songs
button1 = create_button("Twinkle Twinkle Little Star", "#FF0000", lambda: on_button_click("Twinkle Twinkle Little Star"))
button2 = create_button("Wheels on the Bus", "#FF5733", lambda: on_button_click("Wheels on the Bus"))
button3 = create_button("Heart and Soul", "#FF9800", lambda: on_button_click("Heart and Soul"))
button4 = create_button("Tetris", "#3F51B5", lambda: on_button_click("Tetris"))
button5 = create_button("Jingle Bells", "#9C27B0", lambda: on_button_click("Jingle Bells"))

# Place the buttons on the window with some space in between
button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)
button4.pack(pady=10)
button5.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
