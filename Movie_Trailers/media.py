"""Module for opening browser links."""
import webbrowser


class Movie():
    """Movie class to capture movie attributes."""

    def __init__(self, title, movie_storyline, poster_image, trailer_youtube):
        """Initialization method for movie object."""
        self.title = title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Show trailer in a browser for the given url."""
        webbrowser.open(self.trailer_youtube_url)
