from flask import Flask, request, make_response, render_template, session, flash, redirect, url_for

app = Flask(__name__, template_folder='templates/video6', static_folder='static', static_url_path='/')
app.secret_key = 'some_key'

@app.route('/')
def index():
    return render_template('index.html', message= 'Home page!')

@app.route('/set_session_data')
def set_session_data():
    session['name'] = 'Kumaravel Rajan'
    session['other'] = 'Other data in cookie'

    return render_template('index.html', message= 'Session data set')

@app.route('/get_session_data')
def get_session_data():
    if session:
        name = session.get('name')
        other = session.get('other')
        return render_template('index.html', message= f'name = {name};; other = {other}')
    
    return render_template('index.html', message='No session exists yet. Create a new session instead and try again.')

@app.route('/clear_session')
def clear_session():
    session.clear()
    return render_template('index.html', message='Session cleared.')


@app.route('/set_custom_cookie')
def set_custom_cookie():
    response = make_response(render_template('index.html', message='Custom cookie set'))
    response.set_cookie('cookie_key', 'cookie_value')
    return response

@app.route('/get_custom_cookie')
def get_custom_cookie():
    if 'cookie_key' in request.cookies:
        key = 'cookie_key'
        value = request.cookies.get(key)
        return render_template('index.html', message= f'custom cookie key: {key};; custom cookie value: {value}')
    
    return render_template('index.html', message='No custom cookie set. First set the cookie and then try to read it.')

@app.route('/clear_custom_cookie')
def clear_custom_cookie():
    response = make_response(render_template('index.html', message='Cleared custom cookie'))
    response.set_cookie('cookie_key', 'cookie_value', expires=0)
    return response

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        if request.form.get('username') == 'kumar' and request.form.get('password') == 'kumar':
            flash('Successful login (sent via flash)!')
            return redirect(url_for('index'))
            # return render_template('index.html', message = 'Successful login (sent via index.html message)')
        else:
            flash('Login failed! (sent via flash)')
            return redirect(url_for('index'))
            # return render_template('index.html', message= 'Login failed (sent via index.html message)')
            
            

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)

