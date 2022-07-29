from flask import Flask, render_template, request, redirect, url_for


class Movie:
    next_id = 0

    def __init__(self, name, author):
        self.id = Movie.next_id
        Movie.next_id += 1
        self.name = name
        self.author = author

    def __repr__(self):
        return f"Movie '{self.name}' by {self.author}"


app = Flask(__name__)


movies = [
    Movie("Star Wars", "George Lucas"),
    Movie("Lord of the Rings", "Peter Jackson")
]


@app.route('/')
def home():
    return render_template('home.html', movies=movies)


@app.route('/movie/<int:movie_idx>')
def movie(movie_idx):
    try:
        return render_template('movie.html', movie=movies[movie_idx])
    except IndexError:
        return render_template('404Error.html')


@app.route('/movie/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        new_movie = Movie(request.form.get('name'), request.form.get('author'))
        movies.append(new_movie)
        return redirect(url_for('movie', movie_idx=new_movie.id))
    return render_template('create.html')


if __name__ == '__main__':
    app.run()
