"""Module to generate HTML with movie obejcts."""
import fresh_tomatoes
import media

lord_of_the_rings = media.Movie(
    "The Lord of the Rings",
    "A meek Hobbit and eight companions set out on a journey to destroy "
    "the One Ring and the Dark Lord Sauron",
    "https://upload.wikimedia.org/wikipedia/en/8/87/Ringstrilogyposter.jpg",
    "https://www.youtube.com/watch?v=V4mFjdJ5n2g")

everest = media.Movie(
    "Everest",
    "A climbing expedition on Mt Everest is devastated by a severe snow storm",
    "https://upload.wikimedia.org/wikipedia/en/2/28/Everest_poster.jpg",
    "https://www.youtube.com/watch?v=79Q2rrQlPW4")

fifty_fifty = media.Movie(
    "50/50",
    "A young guy who learns of his cancer diagnosis, and his subsequent "
    "struggle to beat the disease",
    "https://upload.wikimedia.org/wikipedia/en/5/51/50_50_Poster.jpg",
    "https://www.youtube.com/watch?v=oKD3qelGza8")

forrest_gump = media.Movie(
    "Forrest Gump",
    "Forrest Gump, while not intelligent, has accidentally been present "
    "at many historic moments",
    "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
    "https://www.youtube.com/watch?v=eYSnxZKTZzU")

taken = media.Movie(
    "Taken",
    "A retired CIA agent travels across Europe and relies on his old skills "
    "to save his estranged daughter",
    "https://upload.wikimedia.org/wikipedia/en/e/ed/Taken_film_poster.jpg",
    "https://www.youtube.com/watch?v=uPJVJBm9TPA")

finding_nemo = media.Movie(
    "Finding Nemo",
    "After his son is captured in the Great Barrier Reef and taken to Sydney,"
    " a timid clownfish sets out on a journey to bring him home.",
    "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
    "https://www.youtube.com/watch?v=AuCxjO2E9Co")

movies = [lord_of_the_rings, everest, fifty_fifty, forrest_gump,
          taken, finding_nemo]
fresh_tomatoes.open_movies_page(movies)
