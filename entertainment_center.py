import media
import fresh_tomatoes

pulp_fiction = media.Movie("Pulp Fiction",
                       "Pulp Fiction is a 1994 American black comedy neo-noir crime film written and directed by Quentin Tarantino, from a story by Tarantino and Roger Avary.",
                       "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
                       "https://www.youtube.com/watch?v=dZWPL9deY7I")
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")
it = media.Movie("IT",
                             "It can be anything. A fanged monster that won't stay on the movie screen. Something ominous lurking in the basement. No matter what your biggest fear is, no one knows It better than Stephen King. Based on the King Of Horror's 1986",
                             "https://upload.wikimedia.org/wikipedia/en/5/5a/It_%282017%29_poster.jpg",
                             "https://www.youtube.com/watch?v=xKJmEC5ieOk&t=61s")
matrix = media.Movie("The Matrix",
                          "Trinity, an infamous hacker, is cornered by police in an abandoned hotel. She overpowers them with superhuman abilities, but a group of sinister superhuman black-suited Agents lead the police in a rooftop pursuit. She answers a ringing public telephone and vanishes.",
                          "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                          "https://www.youtube.com/watch?v=m8e-FF8MsqU")
gladiator = media.Movie("Gladiator",
                                "Going back in time to meet authors",
                                "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
                                "https://www.youtube.com/watch?v=owK1qxDselE")
fight_club = media.Movie("Fight Club",
                           "A really reall reality show",
                           "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                           "https://www.youtube.com/watch?v=SUXWAEX2jlg")

movies = [pulp_fiction, avatar, it, matrix, gladiator, fight_club]
fresh_tomatoes.open_movies_page(movies)
