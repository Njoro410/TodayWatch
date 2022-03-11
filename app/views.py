from flask import Blueprint, render_template, request, redirect, url_for

from app.request import get_movie, get_movies, get_trailer

views = Blueprint('views', __name__)


@views.route('/')
def index():
    """
    view root page function that returns the index page and its data
    """
    # Getting popular movie
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    # print(popular_movies)
    title = 'Home - Welcome to The best Movie Review Website Online'
    search_movie = request.args.get('movie_query')
    # if search_movie:
    #     return redirect(url_for('.search', movie_name=search_movie))
    # else:
    return render_template('index.html', title=title, popular=popular_movies, upcoming=upcoming_movie, now_showing=now_showing_movie)


@views.route('/movie/<string:id>')
def movie(id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_movie(id)
    trailer = get_trailer(id)
    title = f'{movie.title}'
    time = movie.runtime
    hours = time // 60
    minutes = time % 60
    time_string = "{}hrs:{}mins".format(hours, minutes)
    


    return render_template('movie.html', title=title, movie=movie, time=time_string, trailers=trailer)


# @views.route('/search/<movie_name>')
# def search(movie_name):
#     '''
#     View function to display the search results
#     '''
#     movie_name_list = movie_name.split(" ")
#     movie_name_format = "+".join(movie_name_list)
#     searched_movies = search_movie(movie_name_format)
#     title = f'search results for {movie_name}'
#     return render_template('search.html', movies=searched_movies)
