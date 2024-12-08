import random

from flask import Flask, render_template, request

from forms.answers_input import AnswersInput

from utils.check_similar import check_similar


app = Flask(__name__)
app.config['SECRET_KEY'] = 'uesyr67ibF$%!b87NICHINEOI'


@app.route('/', methods=['GET', 'POST'])
def start_page():
    answer_input_form = AnswersInput()
    message = ''

    if request.method == 'GET':
        answer_input_form.generated_sand_speed.data = random.random() * 10 + 0.1
        # TODO: установить адекватные границы для всех значений
        answer_input_form.generated_weight_beginning.data = random.random() * 10 + 0.1
        answer_input_form.generated_strength.data = random.random() * 10 + 0.1
        answer_input_form.generated_distance.data = random.random() * 10 + 0.1

    if answer_input_form.validate_on_submit():
        if check_similar(answer_input_form.sand_speed.data, answer_input_form.generated_sand_speed.data) and \
                check_similar(answer_input_form.weight_beginning.data, answer_input_form.generated_weight_beginning.data) and \
                check_similar(answer_input_form.strength.data, answer_input_form.generated_strength.data) and \
                check_similar(answer_input_form.distance.data, answer_input_form.generated_distance.data):
            message = 'OK'
            # TODO: тут еще должна быть проверка на то, что конечная масса посчитана правильно, я что-то туплю,
            # как это находить((
        else:
            message = 'Неправильный ответ'

    return render_template('index.html', answer_input_form=answer_input_form, message=message)


if __name__ == '__main__':
    app.run()
