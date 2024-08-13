from flask import Flask, render_template, request, jsonify
from forms import AudioFeaturesForm
from flask_bootstrap import Bootstrap
import os
import pickle
import pandas as pd
import numpy as np
from sklearn.feature_extraction import DictVectorizer

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
Bootstrap(app)

#memuat model
with open('model_rf.pkl', 'rb') as file:
    model = pickle.load(file)

dv = DictVectorizer(sparse=False)
cols = ['duration_ms', 'danceability','energy','loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'valence', 'time_signature']

@app.route('/')
def home():
    form = AudioFeaturesForm()
    return render_template('index.html', form=form)

@app.route('/predict', methods=['POST'])
def predict():
    form = AudioFeaturesForm()
    if form.validate_on_submit():
        # Ambil data dari form
        features = {
            'duration_ms': form.duration_ms.data,
            'danceability': form.danceability.data,
            'energy': form.energy.data,
            'loudness': form.loudness.data,
            'mode': form.mode.data,
            'speechiness': form.speechiness.data,
            'acousticness': form.acousticness.data,
            'instrumentalness': form.instrumentalness.data,
            'valence': form.valence.data,
            'time_signature': form.time_signature.data
        }
        for col in cols:
            if col in ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'valence']:
                features[col] = float(request.form[col])
            else:
                features[col] = int(request.form[col])

        input_array = dv.fit_transform(features)

        prediction = model.predict_proba(input_array)
    # Menemukan indeks dengan probabilitas tertinggi
        predicted_class_index = np.argmax(prediction)

        # Mengubah indeks menjadi nama genre musik
        genres = ['Classical', 'Country', 'Dance', 'Disco', 'Electronic', 'Hip-Hop', 'House', 'Jazz', 'Metal', 'Pop', 'R-N-B', 'Rock']
        predicted_genre = genres[predicted_class_index]

        return jsonify(prediction=predicted_genre)

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug = True)