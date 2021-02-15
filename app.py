from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Hello this is the homepage! </h1>'

# Other way to use routes: app.add_url_rule('/', 'index',index)

@app.route('/user/<name>')
def identifier(name):
    return f'<h1> Hello {name}!'