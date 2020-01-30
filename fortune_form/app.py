from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/fortune')
def fortune_form():
    return render_template('fortune_form.html')


@app.route('/fortune_results')
def fortune_results():
    users_favorite_animal = request.args.get('animal')

    if users_favorite_animal == 'dog':
        fortune = "You will receive three minutes of good luck!"
    elif users_favorite_animal == 'cat':
        fortune = ("You will receive advice today that will only be applicable"
                   " for the next seven minutes and eighteen seconds!")
    elif users_favorite_animal == 'other':
        fortune = "You will have a great day tomorrow!"
    else:
        fortune = "You will have an average day today."

    return render_template("fortune_results.html", animal=users_favorite_animal,
                           fortune=fortune)
