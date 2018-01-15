import media
import fresh_tomatoes

"""
This module contains the data for each movie and is the enterence to the
fresh tomatoes app
"""
# Create an instance of the Movie class for each movie to display
# Pulp Fiction movie
pulp_fiction = media.Movie(
    "Pulp Fiction",
    "Pulp Fiction is a 1994 American black comedy neo-noir crime film written "
    "and directed by Quentin Tarantino, from a story by Tarantino and Roger "
    "Avary.",
    "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=s7EdQ4FqbhY"
)
# Avatar movie
avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=d1_JBMrrYw8"
)
# IT movie
it = media.Movie(
    "IT",
    "It can be anything. A fanged monster that won't stay on the movie screen."
    " Something ominous lurking in the basement. No matter what your biggest "
    "fear is, no one knows It better than Stephen King. Based on the King Of "
    "Horror's 1986",
    "https://upload.wikimedia.org/wikipedia/en/5/5a/It_%282017%29_poster.jpg",
    "https://www.youtube.com/watch?v=xKJmEC5ieOk&t=61s"
)
# Matrix movie
matrix = media.Movie(
    "The Matrix",
    "Trinity, an infamous hacker, is cornered by police in an abandoned hotel."
    " She overpowers them with superhuman abilities, but a group of sinister "
    "superhuman black-suited Agents lead the police in a rooftop pursuit. She "
    "answers a ringing public telephone and vanishes.",
    "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
    "https://www.youtube.com/watch?v=m8e-FF8MsqU"
)
# Gladiator movie
gladiator = media.Movie(
    "Gladiator",
    "Going back in time to meet authors",
    "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
    "https://www.youtube.com/watch?v=owK1qxDselE"
)
# Fight Club movie
fight_club = media.Movie(
    "Fight Club",
    "A really reall reality show",
    "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
    "https://www.youtube.com/watch?v=SUXWAEX2jlg"
)
# movies array of each movie class instance
movies = [pulp_fiction, avatar, it, matrix, gladiator, fight_club]
# Pass each Movie instance to fresh tomatoes to build the app
fresh_tomatoes.open_movies_page(movies)
