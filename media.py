import webbrowser

class Movie(object):
    """Holds data pertaining to a movie

    Stores movie information, as well as includes a function for opening the youtube trailer for a movie instance

    Attributes:
        title : A string containing the movie title
        storyline : A string containing a quick summary of the movie
        poster_image_url : A string containing a URL to the poster/box image for the movie
        trailer_youtube_url : A string containing a URL to the Youtube trailer for the movie
        movie_release_year : A string containing the movie release year
    """
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_release_year):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_year = movie_release_year
    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
