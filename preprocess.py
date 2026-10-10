from music21 import converter, note, chord
import glob
import pickle

notes = []

midi_files = glob.glob("dataset/*.mid")

print(f"Found {len(midi_files)} MIDI files.")

for file in midi_files:
    print(f"Processing: {file}")

    midi = converter.parse(file)

    for element in midi.flatten().notes:
        if isinstance(element, note.Note):
            notes.append(str(element.pitch))
        elif isinstance(element, chord.Chord):
            notes.append(
                ".".join(str(n) for n in element.normalOrder)
            )

print(f"Total musical notes/chords extracted: {len(notes)}")

with open("notes.pkl", "wb") as file:
    pickle.dump(notes, file)

print("Preprocessing completed successfully!")
print("Saved processed data to notes.pkl")