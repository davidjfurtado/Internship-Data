from flask import Flask,redirect,url_for,render_template,request
import os
import tensorflow.keras as keras
from PIL import Image
from tensorflow.keras.utils import load_img,img_to_array
import numpy as np
import keras.utils as image
from tensorflow.keras.applications.resnet import preprocess_input


    
    # This module is imported so that we can 
    # play the converted audio
import os
##WSGI Application
app=Flask(__name__)



images=os.path.join('static/pics')
app.config['UPLOAD_FOLDER']=images
model = keras.models.load_model("today_final_prediction_model.hdf5")
target_size = (460, 460)
pic=os.path.join(app.config['UPLOAD_FOLDER'],'logo.png')
pic2=os.path.join(app.config['UPLOAD_FOLDER'],'upload.png')
pic3=os.path.join(app.config['UPLOAD_FOLDER'],'anima.gif')
#decorater
@app.route('/')
def welcome():
    
   

    return render_template('new.html',user_image=pic)

@app.route('/click', methods=['POST'])
def test():
    
   

    return render_template('index.html',user_image=pic,new=pic2)
@app.route('/predict', methods=['POST'])
def new_data():
   
    input_data = request.form['fname']
    image = Image.open(input_data)
    image = image.resize(target_size)
    image_array = np.array(image)
    image_array = np.expand_dims(image_array, axis=0)
    # input_arr=np.expand_dims(input_arr,axis=0)
    y_predict=np.argmax(model.predict(image_array))
    if y_predict==0:
        newdata="The uploaded CT-Scan images has detected Adenocarcinoma cancer cell"
    elif y_predict==1:
            newdata="The uploaded CT-Scan images has detected Large Cell Carcinoma cancer cell"
    elif y_predict==2:
            newdata="The uploaded CT-Scan images has detected no cancer cell"
    else:
            newdata="The uploaded CT-Scan images has detected Squamous Cell Carcinoma cancer cell"


    return render_template('index.html', user_image=pic,new=pic2,model_output=newdata,ani=pic3)



if __name__=='main_':
    app.run(debug=True)