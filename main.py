# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 15:57:01 2021

@author: noopa
"""


import os


# Keras
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer


#Saved model weights
MODEL_PATH = 'model_vgg.h5'

# Load your trained model
model =load_model(MODEL_PATH)
model.make_predict_function()

# Define a flask app
app = Flask(__name__)
        
def model_predict(img_path, model):
    image = load_img(img_path, target_size=(224, 224))
    
    # convert the image pixels to a numpy array
    image = img_to_array(image)
    # reshape data for the model
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    # prepare the image for the VGG model
    image = preprocess_input(image)
    preds = model.predict(image)
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
    app.run(debug=False, threaded=False, use_reloader=False)



