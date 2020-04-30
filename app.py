# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 12:32:47 2019

@author: BABI
"""
import numpy  as np
import pandas as pa
import matplotlib.pyplot as plt
import seaborn as sn
import pickle 
from flask import Flask,jsonify,request,render_template

app = Flask(__name__)

model = pickle.load(open('Random_Forest_model','rb'))
x_test = pickle.load(open('x_test','rb'))

@app.route('/')
def home():
    return render_template('Breast_Cancer_Prediction.html')


@app.route('/predict',methods=["POST"])
def predict():
    radius_mean = float(request.form['radius_mean'])
    texture_mean = int(request.form['texture_mean'])
    perimeter_mean = int(request.form['perimeter_mean'])
    area_mean = int(request.form['area_mean'])
    smoothness_mean = int(request.form['smoothness_mean'])
    compactness_mean = int(request.form['compactness_mean'])
    concavity_mean = int(request.form['concavity_mean'])
    concavity_mean = int(request.form['symmetry_mean'])
    symmetry_mean = int(request.form['radius_se'])
    symmetry_mean = int(request.form['texture_se'])
    symmetry_mean = int(request.form['perimeter_se'])
    symmetry_mean = int(request.form['area_se'])
    symmetry_mean = int(request.form['smoothness_se'])
    symmetry_mean = int(request.form['compactness_se'])
    symmetry_mean = int(request.form['concavity_se'])
    symmetry_mean = int(request.form['symmetry_se'])
    
    test_data = pa.DataFrame({'radius_mean':preg,'texture_mean':glucose,'perimeter_mean':pressure,'area_mean':skin,
                              'smoothness_mean':smoothness,'compactness_mean':compactness,'concavity_mean':concavity,'symmetry_mean':symmetry,'radius_se':radius,
 'texture_se':texture,'perimeter_se':perimeter,'area_se':area,'smoothness_se':smoothness,'compactness_se':compactness,
  'concavity_se':concavity, 'symmetry_se':symmetry},index=[0])                              
                      
    

    x_test= scaler.transform(x_test)

    predict = model.predict(x_test)
    
    if (predict == 0):
        return render_template('Breast_Cancer_Prediction.html',prediction_text='You dont have {}'.format('Cancer'))
    else:
        return render_template('Breast_Cancer_Prediction.html',prediction_text='You have {}'.format('Non Cancer'))
            
if __name__ == "__main__":
    app.run(debug=True)        