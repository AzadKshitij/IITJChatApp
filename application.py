from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'anaiubaejgbfhjabfhkbawuifkjasfkjabkf'


@app.route('/')
def index():
    return render_template('auth/login.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
