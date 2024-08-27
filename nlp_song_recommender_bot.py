import random
import spacy

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

# Real song data
songs_data = [
    {"song_id": 1, "song_name": "Blinding Lights", "artist": "The Weeknd", "genre": "Pop"},
    {"song_id": 2, "song_name": "Shape of You", "artist": "Ed Sheeran", "genre": "Pop"},
    {"song_id": 3, "song_name": "Rolling in the Deep", "artist": "Adele", "genre": "Pop"},
    {"song_id": 4, "song_name": "Uptown Funk", "artist": "Mark Ronson ft. Bruno Mars", "genre": "Funk"},
    {"song_id": 5, "song_name": "Hotel California", "artist": "Eagles", "genre": "Rock"},
    {"song_id": 6, "song_name": "Stairway to Heaven", "artist": "Led Zeppelin", "genre": "Rock"},
    {"song_id": 7, "song_name": "All of Me", "artist": "John Legend", "genre": "Ballad"},
    {"song_id": 8, "song_name": "Summertime Sadness", "artist": "Lana Del Rey", "genre": "Alternative"},
    {"song_id": 9, "song_name": "Take Five", "artist": "Dave Brubeck", "genre": "Jazz"},
    {"song_id": 10, "song_name": "So What", "artist": "Miles Davis", "genre": "Jazz"},
    {"song_id": 11, "song_name": "So", "artist": "Miles", "genre": "Classical"},
    {"song_id": 11, "song_name": "Love Dose", "artist": "Honey Singh", "genre": "Punjabi"},
    # Add more songs as needed
]

# Function to recommend songs based on genre
def recommend_songs(genre):
    # Filter songs based on genre
    recommended_songs = [song for song in songs_data if genre.lower() in song['genre'].lower()]
    return recommended_songs

# NLP-based genre extraction
def extract_genre(user_input):
    # Process user input with spaCy
    doc = nlp(user_input.lower())
    # Look for genre in the user's input
    genres = ["pop", "rock", "jazz", "funk", "ballad", "classical", "punjabi", "alternative"]
    for token in doc:
        if token.text in genres:
            return token.text.capitalize()
    return None

# Chatbot logic
def chatbot():
    print("Welcome to the Song Recommender Chatbot!")
    while True:
        user_input = input("What kind of music are you in the mood for? (Type 'exit' to quit): ")

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Extract genre from user input using NLP
        genre = extract_genre(user_input)
        
        if genre:
            recommendations = recommend_songs(genre)
            if recommendations:
                print(f"Here are some songs you might like in the {genre} genre:")
                for song in recommendations[:10]:  # Limit to top 10 recommendations
                    print(f"{song['song_name']} by {song['artist']}")
            else:
                print(f"Sorry, no recommendations found for the genre '{genre}'.")
        else:
            print("Sorry, I couldn't understand the genre you're looking for. Please try again.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()

