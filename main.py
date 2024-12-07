from flask import Flask, render_template

from forms.answers_input import AnswersInput


app = Flask(__name__)
app.config['SECRET_KEY'] = 'uesyr67ibF$%!b87NICHINEOI'


@app.route('/')
def start_page():
    answer_input_form = AnswersInput()
    return render_template('index.html', answer_input_form=answer_input_form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
