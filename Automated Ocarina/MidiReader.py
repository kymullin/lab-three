import mido
from pathlib import Path

# Define a class to represent a MIDI note with its attributes
class MidiNote:
    def __init__(self, note_name, time):
        self.note_name = note_name
        self.time = time

def midi_to_note_name(note):
    """Convert MIDI note number to note name."""
    note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    octave = (note // 12) - 1
    note_name = note_names[note % 12]
    return f"{note_name}{octave}"

# Define a function to handle actions for different notes
def handle_note_action(note_name):
    if note_name == "C4":
        print("Action: Play sound for C4")
    elif note_name == "C#4":
        print("Action: Play sound for C#4")
    elif note_name == "D4":
        print("Action: Play sound for D4")
    elif note_name == "D#4":
        print("Action: Play sound for D#4")
    elif note_name == "E4":
        print("Action: Play sound for E4")
    elif note_name == "F4":
        print("Action: Play sound for F4")
    elif note_name == "F#4":
        print("Action: Play sound for F#4")
    elif note_name == "G4":
        print("Action: Play sound for G4")
    elif note_name == "G#4":
        print("Action: Play sound for G#4")
    elif note_name == "A4":
        print("Action: Play sound for A4")
    elif note_name == "A#4":
        print("Action: Play sound for A#4")
    elif note_name == "B4":
        print("Action: Play sound for B4")
    else:
        print(f"No action defined for {note_name}")

# Load the MIDI file
midi_file = r'C:\Users\Trys\Downloads\twinkle-twinkle-little-star.mid'  # Replace with the path to your MIDI file
midi_data = mido.MidiFile(midi_file)

# List to store all the notes
note_list = []

# Iterate over MIDI messages and collect notes into the list
for msg in midi_data:
    if msg.type == 'note_on' and msg.velocity > 0:
        note_name = midi_to_note_name(msg.note)
        print(f"Note: {note_name}, Time: {msg.time}")
        
        # Add note to the list as a MidiNote object
        note_list.append(MidiNote(note_name, msg.time))

# Once all notes are collected, process them
print("\nHandling all collected notes:")
for note in note_list:
    handle_note_action(note.note_name)
