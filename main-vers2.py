# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 15:57:01 2021

@author: noopa
"""

import pickle
import numpy as np
import os


# Keras
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
from keras.applications.vgg19 import preprocess_input
from keras.applications.vgg19 import decode_predictions
from keras.applications.vgg19 import VGG16
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer


#Saved model weights
VGG_PATH = 'vgg19_xgb_model.pkl' #'model_vgg.h5'
# XGB_PATH = 'xgb_model.pkl'

# Load your trained model
with open(VGG_PATH, 'rb') as file:
    xgb =pickle.load(VGG_PATH)

vgg19 = tf.keras.applications.VGG19(include_top=False, weights='imagenet',input_shape=(224,224,3))
vgg19.trainable=False

# model.make_predict_function()

# Define a flask app
app = Flask(__name__)
        
def model_predict(img_path, model):

    # Preprocess the image
    img = load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array_expanded = np.expand_dims(img_array, axis=0)
    img_preprocessed = preprocess_input(img_array_expanded)

    # Feature Extraction
    features = vgg19.predict(img_preprocessed)

    # Flatten the features
    features_flat = features.reshape(1, -1)

    # Make a prediction
    preds = xgb.predict(features_flat)

    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)
        
        # convert the probabilities to class labels
        label = decode_predictions(preds)
        # retrieve the most likely result, e.g. highest probability
        label=label[0][0] 
       #result=label[1]
        result='%s( %.2f%%)' % (label[1],label[2]*100)

        return result
    return None

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, threaded=False, use_reloader=False)



