import pickle
import numpy as np
from tensorflow.keras.models import load_model
from music21 import note, chord, stream

# Load trained model
model = load_model("model/music_model.keras")

# Load note mapping
with open("model/note_mapping.pkl", "rb") as file:
    mapping = pickle.load(file)

note_to_int = mapping["note_to_int"]
unique_notes = mapping["unique_notes"]

int_to_note = {
    number: note_name
    for note_name, number in note_to_int.items()
}

print("Model loaded successfully!")
print(f"Available notes/chords: {len(unique_notes)}")

# Load original notes
with open("notes.pkl", "rb") as file:
    notes = pickle.load(file)

# Starting sequence
sequence_length = 50

start = np.random.randint(0, len(notes) - sequence_length - 1)

pattern = [
    note_to_int[n]
    for n in notes[start:start + sequence_length]
]

generated_notes = []

# Generate 100 new musical notes
for _ in range(100):
    prediction_input = np.reshape(
        pattern,
        (1, len(pattern), 1)
    )

    prediction_input = prediction_input / float(
        len(unique_notes)
    )

    prediction = model.predict(
        prediction_input,
        verbose=0
    )

    index = np.argmax(prediction)

    result = int_to_note[index]

    generated_notes.append(result)

    pattern.append(index)
    pattern = pattern[1:]

print("New music sequence generated successfully!")

# Convert generated notes to music21 objects
output_notes = []

for pattern_note in generated_notes:

    if "." in pattern_note:
        chord_notes = [
            int(n)
            for n in pattern_note.split(".")
        ]

        new_chord = chord.Chord(chord_notes)
        output_notes.append(new_chord)

    else:
        new_note = note.Note(pattern_note)
        output_notes.append(new_note)

# Create music stream
music = stream.Stream(output_notes)

# Save generated MIDI file
music.write(
    "midi",
    fp="generated_music.mid"
)

print("Generated music saved successfully!")
print("File: generated_music.mid")