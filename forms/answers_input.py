from flask_wtf import FlaskForm

from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired


class AnswersInput(FlaskForm):
    my = FloatField('мю', validators=[DataRequired(message='Это поле обязательное')])  # TODO: потом нормально назову
    m0 = FloatField('m0', validators=[DataRequired(message='Это поле обязательное')])
    f = FloatField('F', validators=[DataRequired(message='Это поле обязательное')])
    l = FloatField('l', validators=[DataRequired(message='Это поле обязательное')])
    m = FloatField('m', validators=[DataRequired(message='Это поле обязательное')])
    submit = SubmitField('Проверить')
