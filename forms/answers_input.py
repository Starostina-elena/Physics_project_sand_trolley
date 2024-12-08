from flask_wtf import FlaskForm

from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired


class AnswersInput(FlaskForm):
    sand_speed = FloatField('\u03BC', validators=[DataRequired(message='Это поле обязательное')])
    weight_beginning = FloatField('m\u2080', validators=[DataRequired(message='Это поле обязательное')])
    strength = FloatField('F', validators=[DataRequired(message='Это поле обязательное')])
    distance = FloatField('l', validators=[DataRequired(message='Это поле обязательное')])
    weight_end = FloatField('m', validators=[DataRequired(message='Это поле обязательное')])
    submit = SubmitField('Проверить')
