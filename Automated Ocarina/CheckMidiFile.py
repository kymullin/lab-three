def read_midi_file(file_path):
    with open(file_path, 'rb') as f:
        # Read the first 4 bytes to check if it's a valid MIDI file
        header = f.read(4)
        if header != b'MThd':
            print("Not a valid MIDI file.")
            return

        # Read header length (next 4 bytes)
        header_length = int.from_bytes(f.read(4), byteorder='big')
        print(f"Header Length: {header_length}")

        # Read format type (next 2 bytes)
        format_type = int.from_bytes(f.read(2), byteorder='big')
        print(f"Format Type: {format_type}")

        # Read number of tracks (next 2 bytes)
        num_tracks = int.from_bytes(f.read(2), byteorder='big')
        print(f"Number of Tracks: {num_tracks}")

        # Read timing division (next 2 bytes)
        division = int.from_bytes(f.read(2), byteorder='big')
        print(f"Timing Division: {division}")

        # Now read the tracks
        for track_num in range(num_tracks):
            # Each track should start with 'MTrk'
            track_header = f.read(4)
            if track_header != b'MTrk':
                print(f"Track {track_num} does not start with MTrk.")
                return

            # Read track length (next 4 bytes)
            track_length = int.from_bytes(f.read(4), byteorder='big')
            print(f"Track {track_num} Length: {track_length} bytes")

            # Read the track events
            track_data = f.read(track_length)
            print(f"Track {track_num} Data: {track_data[:50]}...")  # Print first 50 bytes for brevity
            # Further parsing would be needed to interpret the MIDI events.

# Example usage:
midi_file_path = r'C:\Users\Trys\Downloads\twinkle-twinkle-little-star.mid'
read_midi_file(midi_file_path)
