import RPi.GPIO as GPIO
import time

# Define the GPIO pin numbers for the 12 holes (adjust according to your setup)
hole_pins = [11, 12, 13, 15, 16, 18, 22, 29, 31, 32, 33, 35]  # Pin numbers for the GPIOs

# Initialize GPIO
GPIO.setmode(GPIO.BCM)  # Using BCM numbering
for pin in hole_pins:
    GPIO.setup(pin, GPIO.OUT)

# Define the note-to-hole mapping for the 12-hole ocarina
# Each list represents the state of the holes: 1 for covered, 0 for uncovered
note_to_holes = {
    72: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # C5
    74: [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # D5
    76: [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],  # E5
    77: [0, 0, 0, 1, 1, 1, 1, 1, 1, 1],  # F5
    79: [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],  # G5
    81: [0, 0, 0, 0, 1, 0, 1, 1, 1, 1],  # A5
    83: [0, 0, 0, 0, 1, 0, 0, 1, 1, 1],  # B5
    84: [0, 0, 0, 0, 1, 0, 0, 0, 1, 1],  # C6
    86: [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],  # D6
    88: [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # E6
    89: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # F6
}

def set_holes(hole_states):
    """Control the GPIO pins to cover/uncover holes based on the hole_states."""
    for pin, state in zip(hole_pins, hole_states):
        GPIO.output(pin, GPIO.HIGH if state == 1 else GPIO.LOW)

def play_notes(note_array):
    """Play a series of notes with 1 second between each note."""
    for note in note_array:
        if note in note_to_holes:
            hole_states = note_to_holes[note]
            print(f"Playing note {note}")
            set_holes(hole_states)  # Control the holes to match the note
        else:
            print(f"Note {note} not mapped to any hole configuration")
        
        time.sleep(1)  # Pause for 1 second between notes

    # Reset holes to uncovered state when done
    set_holes([0] * 12)
    GPIO.cleanup()

# Example array of notes to play (MIDI note numbers)
note_array = [69, 71, 72, 74, 76, 79]  # Example sequence of notes

# Play the notes
play_notes(note_array)
