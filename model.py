# from flask import Flask,redirect,url_for,render_template,request
# app=Flask(__name__)
# from model import Model
# from flask import Flask,redirect,url_for,render_template,request
# import os
# import tensorflow.keras as keras
# from PIL import Image
# from tensorflow.keras.utils import load_img,img_to_array
# import numpy as np
# import keras.utils as image
# from tensorflow.keras.applications.resnet import preprocess_input

# model = keras.models.load_model("today_final_prediction_model.hdf5")
# target_size = (460, 460)
# @app.route('/', methods=['POST'])
# def predict():
#     # Retrieve the input data from the form
#     input_data = request.form['fname']
#     image = Image.open(input_data)
#     image = image.resize(target_size)
#     image_array = np.array(image)
#     image_array = np.expand_dims(image_array, axis=0)
#     # input_arr=np.expand_dims(input_arr,axis=0)
#     y_predict=np.argmax(model.predict(image_array))
#     if y_predict==0:
#         print("The CT_Scan detected Adenocarcinoma Cancer Cell")
#     elif y_predict==1:
#             print("The CT_Scan detected Large Cell Carcinoma Cancer Cell")
#     elif y_predict==2:
#             print("The CT_Scan detected Normal Cell")
#     else:
#             print("The CT_Scan detected Squamous Cell Carcinoma Cancer Cell")


#     # Call the model with the input data
    

#     # Return the model output to the HTML template
#     return render_template('index.html', model_output=y_predict)