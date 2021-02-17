from flask import Flask, request, g

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Hello this is the homepage! </h1>'

# Other way to use routes: app.add_url_rule('/', 'index',index)

@app.route('/user/<name>')
def identifier(name):
    ip_address = request.remote_addr
    endpoint = request.endpoint
    return f'Hi {name}, your IP adress is {ip_address} and you\' re at {endpoint}'


@app.route('target')
def target():
    return g.target +'\n'


# Request hooks 
@app.before_request
def before_r():
    g.target = request.args.get('target'.'default')