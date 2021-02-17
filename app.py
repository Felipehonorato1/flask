from flask import Flask, request, g, make_response, redirect, abort, url_for

app = Flask(__name__)

@app.route('/homepage')
def index():
    return '<h1> Hello this is the homepage! </h1>'

# Other way to use routes: app.add_url_rule('/', 'index',index)

@app.route('/user/<name>')
def identifier(name):
    ip_address = request.remote_addr
    endpoint = request.endpoint
    return f'Hi {name}, your IP adress is {ip_address} and you\' re at {endpoint}'


@app.route('/target')
def target():
    return g.target +'\n'


# Request hooks: Useful for storing users and initializing database connections. 
@app.before_request
def before_r():
    g.target = request.args.get('target','default')
    g.user = request.remote_addr

# Response -> status code sent through invoked function.

@app.route('/ip_address')
def verifying_ip():
    if g.user == '127.0.0.2':
        return '02 adress', 200 # 200 Code is by default set as a positive sign for the function invoked
    if g.user == '127.0.0.1':
        # response = make_response(request.remote_addr)
        # response.set_cookie('Ip adress', 400)
        # return response
        return request.remote_addr, 400 # Bad request by default
    
    #Redirect response

@app.route('/redirection')
def redirection():
        return redirect(url_for('verifying_ip'),302 )