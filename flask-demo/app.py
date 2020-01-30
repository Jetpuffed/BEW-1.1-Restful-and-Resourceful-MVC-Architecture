from flask import Flask, request

app = Flask(__name__)


@app.route('/hello')
def say_hello():
    return "Hello, world!"


@app.route('/user/<username>')
def say_hello_var(username):
    return 'Hi, ' + username

# Modified by Activity: Use a query string


@app.route('/double')
def double():
    the_number = request.args.get('the_number')
    return str(int(the_number) * int(2))


@app.route('/double_form')
def double_form():
    return """
    <form action='/double'>
        Type in the number you want to double: <input type='text' name='the_number'>
        <br>
        <input type='submit'>
    </form>
    """


@app.route('/square')
def square():
    root_number = request.args.get('root_number')
    return str(int(root_number) * int(root_number))


@app.route('/square_form')
def square_form():
    return """
    <form action='/square'>
        Type in the number you want to square root: <input type='text' name='root_number'>
        <br>
        <input type='submit'>
    </form>
    """


@app.route('/multiname')
def multiname():
    username = request.args.get('username')
    name_number = request.args.get('name_number')
    return str(username * int(name_number))


@app.route('/multiname_form')
def multiname_form():
    return """
    <form action='/multiname'>
        Type in your username: <input type='text' name='username'>
        <br>
        Type in a number: <input type='text' name='name_number'>
        <br>
        <input type='submit'>
    </form>
    """


@app.route('/backwards')
def backwards():
    username = request.args.get('username')
    return username[::-1]


@app.route('/backwards_form')
def backwards_form():
    return """
    <form action='/backwards'>
        Type in the name you want to convert backwards: <input type='text' name='username'>
        <br>
        <input type='submit'>
    </form>
    """

# End of modifcations


@app.route('/search')
def search_page():
    name = request.args.get('name')
    category = request.args.get('category')
    return 'You searched for ' + name + ' in the category ' + category


@app.route('/search_form')
def search_form():
    return """
    <form action='/search'>
        Type in the product name: <input type='text' name='name'>
        <br>
        Type in the category: <input type='text' name='category'>
        <br>
        <input type='submit'>
    </form>
    """


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    return 'Username is ' + username ', password is ' + password


@app.route('/login_form')
def login_form():
    return """
    <form action='/login'>
        Username: <input type='text' name='username'>
        <br>
        Password: <input type='text' name='password'>
        <br>
        <input type='submit'>
    </form>
    """
