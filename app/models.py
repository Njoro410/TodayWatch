
import string


class Movie:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self, id, title, overview, poster, vote_average, vote_count, tagline, genres, date, language, prod, imdb_id, runtime):
        self.id = id
        self.title = title
        self.overview = overview
        self.poster = "https://image.tmdb.org/t/p/w500/" + poster
        self.vote_average = vote_average
        self.vote_count = vote_count
        self.tagline = tagline
        self.genres = genres
        self.date = date
        self.language = language
        self.prod = prod
        self.imdb_id = imdb_id
        self.runtime = runtime

class Trailer:
    def __init__(self,id,name,key,type):
        self.id = id
        self.name = name
        self.key = key
        self.type = type
