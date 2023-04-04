import spacy

# Load the spacy model
nlp = spacy.load("en_core_web_sm")

# Define a sample sentence
sentence = "Mark Zuckerberg founded Facebook in 2004 in Menlo Park, California."

# Process the sentence with the model
doc = nlp(sentence)

# Iterate over the named entities in the document
for ent in doc.ents:
    # Print the entity text and label
    print(ent.text," - ", ent.label_)
