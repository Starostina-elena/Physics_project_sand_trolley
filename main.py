import random
from flask import Flask, render_template, request
from forms.answers_input import AnswersInput
from utils.check_similar import check_similar
from utils.physics import calculate_graph_data

import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = 'uesyr67ibF$%!b87NICHINEOI'


@app.route('/', methods=['GET', 'POST'])
def start_page():
    global graph_data
    answer_input_form = AnswersInput()
    message = ''
    validation_error = False
    correct_answer = False

    if request.method == 'GET':
        # Генерация начальной массы тележки в диапазоне 50-200 кг
        m0 = random.uniform(50, 200)

        # Конечная масса 50-80% от начальной
        generated_weight_end = m0 * random.uniform(0.5, 0.8)

        # Коэффициент песка 2-5% от начальной массы
        mu = m0 * random.uniform(0.02, 0.05)

        F = m0 * random.uniform(0.5, 3)

        # Заполняем форму
        answer_input_form.generated_sand_speed.data = mu
        answer_input_form.generated_weight_beginning.data = m0
        answer_input_form.generated_weight_end.data = generated_weight_end
        answer_input_form.generated_strength.data = F

        # Вычисляем путь l до конечного времени t
        t_max = (m0 - generated_weight_end) / mu
        l = abs((F / mu) * (t_max - (m0 / mu) * np.log(m0 / generated_weight_end)))

        # Заполняем результат в форму
        answer_input_form.generated_distance.data = l

        # Генерируем данные для графиков
        graph_data = calculate_graph_data(m0, F, mu, generated_weight_end)

    if request.method == 'POST' and not answer_input_form.validate_on_submit():
        message = 'Физика любит числа :)'
        validation_error = True
    if answer_input_form.validate_on_submit():
        print(graph_data)
        if not check_similar(answer_input_form.sand_speed.data, answer_input_form.generated_sand_speed.data):
            message += 'Введен неверный \u03BC' + '<br>'
            validation_error = True
        if not check_similar(answer_input_form.weight_beginning.data,
                             answer_input_form.generated_weight_beginning.data):
            message += 'Введен неверный m\u2080' + '<br>'
            validation_error = True
        if not check_similar(answer_input_form.strength.data, answer_input_form.generated_strength.data):
            message += 'Введен неверный F' + '<br>'
            validation_error = True
        if not check_similar(answer_input_form.distance.data, answer_input_form.generated_distance.data):
            message += 'Введен неверный l' + '<br>'
            validation_error = True
        if not check_similar(answer_input_form.weight_end.data, answer_input_form.generated_weight_end.data):
            message += 'Введен неверный m' + '<br>'
            validation_error = True
        else:
            message = 'Правильный ответ!'
            correct_answer = True

    try:
        return render_template(
            'index.html',
            answer_input_form=answer_input_form,
            message=message,
            validation_error=validation_error,
            correct_answer=correct_answer,
            graph_data=graph_data  # Передаем данные для графиков
        )
    except NameError:
        return render_template(
            'index.html',
            answer_input_form=answer_input_form,
            message=message,
            validation_error=validation_error,
            correct_answer=correct_answer,
            graph_data=None  # Передаем данные для графиков
        )



if __name__ == '__main__':
    app.run()
