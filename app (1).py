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
y_test = pickle.load(open('y_test','rb'))

@app.route('/')
def home():
    return render_template('Cancer_prediction.html')


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
                              'smoothness_mean':BMI,'compactness_mean':Diabetes_pedigree,'concavity_mean':age,'symmetry_mean':age,'radius_se':age,'texture_se':age,'perimeter_se':age,'area_se':age,'smoothness_se':age,'compactness_se':age,'concavity_se':age,'symmetry_se'},index=[0])
    

    y_test= scaler.transform(y_test)

    predict = model.predict(y_test)
    
    if (predict == 0):
        return render_template('Cancer_prediction.html',prediction_text='You dont have {}'.format('Cancer'))
    else:
        return render_template('Cancer_prediction.html',prediction_text='You have {}'.format('Non Cancer'))
            
if __name__ == "__main__":
    app.run(debug=True)        