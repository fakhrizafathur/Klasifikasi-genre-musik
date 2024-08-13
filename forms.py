from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange, InputRequired

class AudioFeaturesForm(FlaskForm):
    duration_ms = IntegerField('Duration (ms)', validators=[InputRequired(message = 'Form harus di isi!!'), NumberRange(min=0)])
    danceability = FloatField('Danceability', validators=[InputRequired(message = 'Form harus di isi!!'), NumberRange(min=0.0, max=1.0)])
    energy = FloatField('Energy', validators=[InputRequired(message = 'Form harus di isi!!'), NumberRange(min=0.0, max=1.0)])
    loudness = FloatField('Loudness', validators=[InputRequired(message = 'Form harus di isi!!')])
    mode = IntegerField('Mode', validators=[InputRequired(message = 'Form harus di isi!!'), NumberRange(min=0, max=1)])
    speechiness = FloatField('Speechiness', validators=[InputRequired(message = 'Form harus di isi!!'), NumberRange(min=0.0, max=1.0)])
    acousticness = FloatField('Acousticness', validators=[InputRequired(message = 'Form harus di isi!!'), NumberRange(min=0.0, max=1.0)])
    instrumentalness = FloatField('Instrumentalness', validators=[InputRequired(message = 'Form harus di isi!!'), NumberRange(min=0.0, max=1.0)])
    valence = FloatField('Valence', validators=[InputRequired(message = 'Form harus di isi!!'), NumberRange(min=0.0, max=1.0)])
    time_signature = IntegerField('Time Signature', validators=[InputRequired(message = 'Form harus di isi!!'), NumberRange(min=3, max=7)])
    submit = SubmitField('Prediksi')
