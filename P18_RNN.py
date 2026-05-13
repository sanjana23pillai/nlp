# Q18. RNN Sentiment Analysis using NLTK Movie Reviews

# Download movie reviews dataset
import nltk
nltk.download("movie_reviews")

from nltk.corpus import movie_reviews

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


# -------------------------------
# Step 1: Load reviews and labels
# -------------------------------

reviews = []
labels = []

# movie_reviews has two categories: pos and neg
for category in movie_reviews.categories():

    # Go through all review files in each category
    for fileid in movie_reviews.fileids(category):

        # Store review text
        reviews.append(movie_reviews.raw(fileid))

        # Store label
        # Positive = 1, Negative = 0
        if category == "pos":
            labels.append(1)
        else:
            labels.append(0)

labels = np.array(labels)


# -------------------------------
# Step 2: Convert text into numbers
# -------------------------------

MAX_WORDS = 5000
MAX_LEN = 200

# Tokenizer converts words into numbers
tokenizer = Tokenizer(num_words=MAX_WORDS, oov_token="<OOV>")

# Learn word index from reviews
tokenizer.fit_on_texts(reviews)

# Convert reviews into number sequences
sequences = tokenizer.texts_to_sequences(reviews)

# Make all reviews same length
X = pad_sequences(sequences, maxlen=MAX_LEN, padding="post")

# Labels
y = labels


# -------------------------------
# Step 3: Split data into train and test
# -------------------------------

split = int(0.8 * len(X))

X_train = X[:split]
X_test = X[split:]

y_train = y[:split]
y_test = y[split:]


# -------------------------------
# Step 4: Build RNN model
# -------------------------------

model = Sequential()

# Embedding layer converts word numbers into vector form
model.add(Embedding(input_dim=MAX_WORDS, output_dim=32, input_length=MAX_LEN))

# Simple RNN layer reads the sequence
model.add(SimpleRNN(32))

# Output layer
# sigmoid gives output between 0 and 1
model.add(Dense(1, activation="sigmoid"))


# -------------------------------
# Step 5: Compile model
# -------------------------------

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)


# -------------------------------
# Step 6: Train model
# -------------------------------

model.fit(
    X_train,
    y_train,
    epochs=3,
    batch_size=64,
    validation_split=0.1
)


# -------------------------------
# Step 7: Test model
# -------------------------------

loss, accuracy = model.evaluate(X_test, y_test)

print("Test Accuracy:", accuracy)


# -------------------------------
# Step 8: Predict new reviews
# -------------------------------

samples = [
    "This movie was very good and amazing",
    "This movie was boring and bad"
]

sample_seq = tokenizer.texts_to_sequences(samples)
sample_pad = pad_sequences(sample_seq, maxlen=MAX_LEN, padding="post")

predictions = model.predict(sample_pad)

for review, pred in zip(samples, predictions):

    if pred[0] >= 0.5:
        sentiment = "Positive"
    else:
        sentiment = "Negative"

    print(review, "->", sentiment)