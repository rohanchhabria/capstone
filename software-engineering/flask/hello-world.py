from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # html can be rendered along with normal strings.
    return '<h2>This is an `Hello World` rendered from an flask app.</h2>'

@app.route('/user/<name>')
def user(name):
    return f'<h2>Greetings {name}! This was rendered from the user route.</h2>'

if __name__ == '__main__':
    app.run(port=5000)
    