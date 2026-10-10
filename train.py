import pickle
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.utils import to_categorical

# Load processed musical notes
with open("notes.pkl", "rb") as file:
    notes = pickle.load(file)

print(f"Loaded {len(notes)} musical notes/chords.")

# Get unique notes
unique_notes = sorted(set(notes))
note_to_int = {note: number for number, note in enumerate(unique_notes)}

print(f"Unique notes/chords: {len(unique_notes)}")

# Create input sequences
sequence_length = 50
network_input = []
network_output = []

for i in range(len(notes) - sequence_length):
    sequence_in = notes[i:i + sequence_length]
    sequence_out = notes[i + sequence_length]

    network_input.append(
        [note_to_int[char] for char in sequence_in]
    )
    network_output.append(note_to_int[sequence_out])

n_patterns = len(network_input)

print(f"Training sequences: {n_patterns}")

# Reshape input for LSTM
X = np.reshape(
    network_input,
    (n_patterns, sequence_length, 1)
)

# Normalize input
X = X / float(len(unique_notes))

# Convert output to categorical format
y = to_categorical(
    network_output,
    num_classes=len(unique_notes)
)

print("Input shape:", X.shape)
print("Output shape:", y.shape)

# Build LSTM model
model = Sequential()

model.add(
    LSTM(
        256,
        input_shape=(X.shape[1], X.shape[2]),
        return_sequences=True
    )
)

model.add(Dropout(0.3))

model.add(
    LSTM(256)
)

model.add(Dropout(0.3))

model.add(
    Dense(len(unique_notes), activation="softmax")
)

# Compile model
model.compile(
    loss="categorical_crossentropy",
    optimizer="adam"
)

model.summary()

# Train the model
print("\nStarting LSTM training...")

model.fit(
    X,
    y,
    epochs=30,
    batch_size=64
)

# Save the trained model
model.save("model/music_model.keras")

# Save note mappings
with open("model/note_mapping.pkl", "wb") as file:
    pickle.dump(
        {
            "note_to_int": note_to_int,
            "unique_notes": unique_notes
        },
        file
    )

print("\nTraining completed successfully!")
print("Model saved to: model/music_model.keras")
print("Note mapping saved to: model/note_mapping.pkl")