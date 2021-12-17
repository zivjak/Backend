from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)


@app.route('/')
def cv():  # put application's code here
    return render_template('cv.html')

@app.route('/assignment8')
def assignment8():  # put application's code here
    return render_template('assignment8.html', years='8 years', hobbies=('climbing','cooking','art','runing', 'sql', 'jumping'))


if __name__ == '__main__':
    app.run()
