from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/home_page')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

@app.route('/about', methods = ['GET', 'POST'])
def about_func():
    # TODO
    # DO SOMETHING WITH DB
    print('Im in about')
    return 'welcome to about'

@app.route('/catalog')
def catalog_func():
    return redirect(url_for('hello_world'))