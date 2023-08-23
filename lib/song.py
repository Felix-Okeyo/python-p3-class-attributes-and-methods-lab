class Song:
    # We start with some variables to keep track of counts and lists.
    count = 0            # Total count of songs.
    artists = []         # List to store all artists.
    genres = []          # List to store all genres.
    genre_count = {}     # Dictionary to count each genre.
    artist_count = {}    # Dictionary to count each artist.
    
    # This special function runs when a new song is created.
    def __init__(self, name, artist, genre):
        # These variables store the song's details.
        self.name = name      # The name of the song.
        self.artist = artist  # The artist of the song.
        self.genre = genre    # The genre of the song.
        
        # We increase the count of songs and update lists and counts.
        Song.count += 1                      # Increase the total count.
        Song.artists.append(artist)          # Add the artist to the list.
        Song.genres.append(genre)            # Add the genre to the list.
        
        # Update the count of this genre in the genre_count dictionary.
        # If it doesn't exist, it starts at 0 and then increases by 1.
        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1
        
        # Update the count of this artist in the artist_count dictionary.
        # If it doesn't exist, it starts at 0 and then increases by 1.
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1
