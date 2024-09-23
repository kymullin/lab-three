import mido
from pathlib import Path

def midi_to_note_name(note):
    """Convert MIDI note number to note name."""
    note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    octave = (note // 12) - 1
    note_name = note_names[note % 12]
    return f"{note_name}{octave}"

# Load the MIDI file
midi_file = r'C:\Users\Trys\Downloads\twinkle-twinkle-little-star.mid'  # Replace with the path to your MIDI file
midi_data = mido.MidiFile(midi_file)

# Iterate over MIDI messages
for msg in midi_data:
    if msg.type == 'note_on' and msg.velocity > 0:
        note_name = midi_to_note_name(msg.note)
        print(f"Note: {note_name}, Time: {msg.time}")
