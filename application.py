from flask import Flask, render_template
from wtform_fields import RegistrationForm

app = Flask(__name__)
app.secret_key = 'anaiubaejgbfhjabfhkbawuifkjasfkjabkf'


@app.route('/', methods=['GET', 'POST'])
def index():
    registration_form = RegistrationForm()

    if registration_form.validate_on_submit():
        return 'Great Success'

    return render_template('auth/login.html',
                           props={'registration_form': registration_form})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
