import os
import spacy

# Load the language model
nlp = spacy.load('en_core_web_md')

# Read the movie descriptions and titles
movie_descriptions = []
movie_titles = []
with open('movies.txt', 'r') as file:
    for line in file:
        title, description = line.strip().split(':')
        movie_titles.append(title)
        movie_descriptions.append(description)

# Process the descriptions
doc_descriptions = [nlp(description) for description in movie_descriptions]

# Process the description of the movie "Planet Hulk"
planet_hulk_description = nlp("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.")

# Compute similarity scores with all other movies
similarities = [planet_hulk_description.similarity(doc) for doc in doc_descriptions]

# Find the index of the most similar movie
most_similar_index = similarities.index(max(similarities))

# Print the title of the most similar movie
print(f"Watch next: {movie_titles[most_similar_index]}")