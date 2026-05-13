# Q19. Information Extraction using Named Entity Recognition

text = "Apple Inc. was founded by Steve Jobs and Steve Wozniak in Cupertino, California in 1976. The company is headquartered in the United States and its CEO Tim Cook earns over $10 million annually. In January 2024, Apple released new products at an event in San Francisco."

# -------------------------------
# PART A: NER using spaCy
# -------------------------------

import spacy

# Load English model
nlp = spacy.load("en_core_web_sm")

# Process the text
doc = nlp(text)

print("=== NER using spaCy ===\n")

# Print entities found by spaCy
for ent in doc.ents:
    print(ent.text, "->", ent.label_)


# -------------------------------
# PART B: Manual / Hardcoded NER
# -------------------------------

entities = {
    "Apple Inc.": "ORG",
    "Apple": "ORG",
    "Steve Jobs": "PERSON",
    "Steve Wozniak": "PERSON",
    "Tim Cook": "PERSON",
    "Cupertino": "GPE",
    "California": "GPE",
    "United States": "GPE",
    "San Francisco": "GPE",
    "1976": "DATE",
    "January 2024": "DATE",
    "$10 million": "MONEY"
}

print("\n=== Manual NER ===\n")

# Check if each entity is present in text
for entity in entities:
    if entity in text:
        print(entity, "->", entities[entity])