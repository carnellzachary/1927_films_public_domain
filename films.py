from flask import Flask, render_template, redirect, url_for, request
from modules import convert_to_dict

app = Flask(__name__)

films_list = convert_to_dict("1927_films.csv")

@app.route('/')
def index():
    ids_list = []
    title_list = []
    image_list = []

    for film in films_list:
        ids_list.append(film['id'])
        title_list.append(film['title'])
        image_list.append(film['image_name'])

    pairs_list = zip(ids_list, title_list, image_list)

    return render_template('index.html', pairs=pairs_list, the_title="1927 Films in Public Domain")

@app.route('/film/<num>')
def detail(num):
    for film in films_list:
        if film['id'] == num:
            film_dict = film
            break
    return render_template('detail.html', film=film_dict, the_title=film_dict['title'])

# keep this as is
if __name__ == '__main__':
    app.run(debug=True)
