#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import mido
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="filename")

parser.add_argument("filename", type=str, help="Name of the MIDI file")
args = parser.parse_args()

midi_file_path = args.filename

# Define the GPIO pin numbers for the 12 holes (adjust according to your setup)
hole_pins = [11, 12, 13, 15, 16, 18, 22, 7]#, 31, 32, 33, 35]  # Pin numbers for the GPIOs

# Set pin 33 for fan control
fan_pin = 33

# Initialize GPIO
GPIO.setmode(GPIO.BOARD)  # Using Board numbering
for pin in hole_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Setup fan control pin
GPIO.setup(fan_pin, GPIO.OUT)

# Define the note-to-hole mapping for the 12-hole ocarina
note_to_holes = {
    72: [0, 0, 0, 0, 0, 0, 0, 0],#, 0, 0],  # C5
    74: [1, 0, 0, 0, 0, 0, 0, 0],#, 0, 0],  # D5
    76: [1, 1, 0, 0, 0, 0, 0, 0],#, 0, 0],  # E5
    77: [1, 1, 1, 0, 0, 0, 0, 0],#, 0, 0],  # F5
    79: [1, 1, 1, 1, 0, 0, 0, 0],#, 0, 0],  # G5
    81: [1, 1, 1, 1, 0, 1, 0, 0],#, 0, 0],  # A5
    83: [1, 1, 1, 1, 0, 1, 1, 0],#, 0, 0],  # B5
    84: [1, 1, 1, 1, 0, 1, 1, 1],#, 0, 0],  # C6
    86: [1, 1, 1, 1, 0, 1, 1, 1],#, 1, 0],  # D6
    88: [1, 1, 1, 1, 0, 1, 1, 1],#, 1, 1],  # E6
    89: [1, 1, 1, 1, 1, 1, 1, 1]#, 1, 1]   # F6
    
    #72: [1, 0, 0, 0, 0, 0, 0, 0],#, 0, 0],  # C5
    #74: [0, 1, 0, 0, 0, 0, 0, 0],#, 0, 0],  # D5
    #76: [0, 0, 1, 0, 0, 0, 0, 0],#, 0, 0],  # E5
    #77: [0, 0, 0, 1, 0, 0, 0, 0],#, 0, 0],  # F5
    #79: [0, 0, 0, 0, 1, 0, 0, 0],#, 0, 0],  # G5
    #81: [0, 0, 0, 0, 0, 1, 0, 0],#, 0, 0],  # A5
    #83: [0, 0, 0, 0, 0, 0, 1, 0],#, 0, 0],  # B5
    #84: [0, 0, 0, 0, 0, 0, 0, 1],#, 0, 0],  # C6
    #86: [1, 1, 1, 1, 0, 1, 1, 1],#, 1, 0],  # D6
    #88: [1, 1, 1, 1, 0, 1, 1, 1],#, 1, 1],  # E6
    #89: [1, 1, 1, 1, 1, 1, 1, 1]#, 1, 1]   # F6
}

# Grab tempo
tempo = 0;
for track in mido.MidiFile(midi_file_path).tracks:
        for msg in track:
            if msg.type == 'set_tempo':
                tempo = msg.tempo

def set_holes(hole_states):
    """Control the GPIO pins to cover/uncover holes based on the hole_states."""
    for pin, state in zip(hole_pins, hole_states):
        GPIO.output(pin, GPIO.HIGH if state == 1 else GPIO.LOW)

def smooth_transition(current_holes, next_holes):
    """Smoothly transition from one note's hole configuration to the next."""
    for i in range(len(current_holes)):
        if current_holes[i] != next_holes[i]:
            GPIO.output(hole_pins[i], GPIO.HIGH if next_holes[i] == 1 else GPIO.LOW)
            time.sleep(0.05)  # Small delay to simulate a smooth transition

def control_fan(start):
    """Control the fan on pin 33: start or stop based on the 'start' flag."""
    if start:
        GPIO.output(fan_pin, GPIO.HIGH)  # Turn fan ON
    else:
        GPIO.output(fan_pin, GPIO.LOW)   # Turn fan OFF

def play_midi_file(midi_file_path):
    """Interpret and play a MIDI file using the note-to-hole mappings."""
    # Load the MIDI file using mido
    midi_file = mido.MidiFile(midi_file_path)

    # Store the current state of the holes
    current_holes = [0] * 8

    # Iterate through MIDI messages in the file
    for message in midi_file.play():
        if message.type == 'note_on' and message.velocity > 0:  # Only handle 'note_on' events
            note = message.note
            print(f"Playing note {note}")

            control_fan(True)  # Start the fan when a note is played
            
            if note in note_to_holes:
                next_holes = note_to_holes[note]
                smooth_transition(current_holes, next_holes)  # Smooth transition to the next note
                current_holes = next_holes  # Update the current holes state
            else:
                print(f"Note {note} not mapped to any hole configuration")

        elif message.type == 'note_off':  # Stop the fan when the note is released
            print(f"Stopping note {message.note}")
            control_fan(False)  # Stop the fan

        time.sleep(mido.tick2second(message.time, midi_file.ticks_per_beat, tempo))  # Sleep to match the timing of the MIDI file

    # Cleanup GPIO after the file has finished playing
    GPIO.cleanup()
    print(f"Complete")

# Call the function with the path to your MIDI file
play_midi_file(midi_file_path)
