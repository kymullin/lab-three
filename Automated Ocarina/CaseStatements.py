import RPi.GPIO as GPIO
import time
import mido

# Define the GPIO pin numbers for the 12 holes (adjust according to your setup)
hole_pins = [11, 12, 13, 15, 16, 18, 22, 29, 31, 32, 33, 35]  # Pin numbers for the GPIOs

# Initialize GPIO
GPIO.setmode(GPIO.BCM)  # Using BCM numbering
for pin in hole_pins:
    GPIO.setup(pin, GPIO.OUT)

# Define the note-to-hole mapping for the 12-hole ocarina
# Each list represents the state of the holes: 1 for covered, 0 for uncovered
note_to_holes = {
    69: [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],  # A4
    70: [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],  # A#4/Bb4
    71: [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # B4
    72: [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # C5
    73: [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # C#5/Db5
    74: [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # D5
    75: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # D#5/Eb5
    76: [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],  # E5
    77: [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],  # F5
    78: [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],  # F#5/Gb5
    79: [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # G5
    80: [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # G#5/Ab5
    81: [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # A5
    82: [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # A#5/Bb5
    83: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # B5
    84: [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],  # C6
    85: [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],  # C#6/Db6
    86: [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],  # D6
    87: [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # D#6/Eb6
    88: [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # E6
    89: [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # F6
}

def set_holes(hole_states):
    """Control the GPIO pins to cover/uncover holes based on the hole_states."""
    for pin, state in zip(hole_pins, hole_states):
        GPIO.output(pin, GPIO.HIGH if state == 1 else GPIO.LOW)

def play_midi_file(midi_file_path):
    """Interpret and play a MIDI file using the note-to-hole mappings."""
    # Load the MIDI file using mido
    midi_file = mido.MidiFile(midi_file_path)

    # Iterate through MIDI messages in the file
    for message in midi_file.play():
        if message.type == 'note_on' and message.velocity > 0:  # Only handle 'note_on' events
            note = message.note
            print(f"Playing note {note}")
            
            if note in note_to_holes:
                hole_states = note_to_holes[note]
                set_holes(hole_states)  # Control the holes to match the note
            else:
                print(f"Note {note} not mapped to any hole configuration")
        
        elif message.type == 'note_off':  # Optionally reset holes when the note is released
            print(f"Stopping note {message.note}")
            set_holes([0] * 12)  # Reset all holes to uncovered (if desired)

        time.sleep(message.time)  # Sleep to match the timing of the MIDI file

    # Cleanup GPIO after the file has finished playing
    GPIO.cleanup()

# Call the function with the path to your MIDI file
play_midi_file('your_midi_file.mid')
