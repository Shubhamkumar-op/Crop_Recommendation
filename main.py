# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pickle
import numpy as np
import scipy.sparse.linalg
import streamlit as st

loaded_model = pickle.load(open("crop_model.pkl",'rb'))





def predict(N, P, K, temperature, humidity, pH, rainfall):
    input_value = np.array([[N, P, K, temperature, humidity, pH, rainfall]])
    
    prediction = loaded_model.predict(input_value)
    
    pred = prediction[0]

    if pred == 1:
        print("Rice is the best crop to be cultivated right there")
    elif pred == 2:
        print("Maize is the best crop to be cultivated right there")
    elif pred == 3:
        print("Jute is the best crop to be cultivated right there")
    elif pred == 4:
        print("Cotton is the best crop to be cultivated right there")
    elif pred == 5:
        print("Coconut is the best crop to be cultivated right there")
    elif pred == 6:
        print("Papaya is the best crop to be cultivated right there")
    elif pred == 7:
        print("Orange is the best crop to be cultivated right there")
    elif pred == 8:
        print("Apple is the best crop to be cultivated right there")
    elif pred == 9:
        print("Muskmelon is the best crop to be cultivated right there")
    elif pred == 10:
        print("Watermelon is the best crop to be cultivated right there")
    elif pred == 11:
        print("Grapes is the best crop to be cultivated right there")
    elif pred == 12:
        print("Mango is the best crop to be cultivated right there")
    elif pred == 13:
        print("Banana is the best crop to be cultivated right there")
    elif pred == 14:
        print("Pomegranate is the best crop to be cultivated right there")
    elif pred == 15:
        print("Lentil is the best crop to be cultivated right there")
    elif pred == 16:
        print("Blackgram is the best crop to be cultivated right there")
    elif pred == 17:
        print("Mungbean is the best crop to be cultivated right there")
    elif pred == 18:
        print("Mothbeans is the best crop to be cultivated right there")
    elif pred == 19:
        print("Pigeonpeas is the best crop to be cultivated right there")
    elif pred == 20:
        print("Kidneybeans is the best crop to be cultivated right there")
    elif pred == 21:
        print("Chickpea is the best crop to be cultivated right there")
    elif pred == 22:
        print("Coffee is the best crop to be cultivated right there")
    else:
        print("Sorry, we could not determine the best crop to be cultivated with the provided data.")
    
def main():
    st.title('Crop Recommendation Web app')
    
    
    N = st.slider('Nitrogen', 0, 140)
    P = st.slider('Phosphorus', 5, 145)
    K = st.slider('Potassium', 5, 205)
    temperature = st.slider('Temperature', 8.83, 44.00)
    humidity = st.slider('Humidity', 14.00, 100.00)
    pH = st.slider('pH', 3.50, 10.00)
    rainfall = st.slider('Rainfall', 20.00, 300.00)
   
     
   # code for prediction
    pred = ''

    if st.button('Best crop to be cultivated right there'):
        input_value = np.array([[N, P, K, temperature, humidity, pH, rainfall]])
        
        prediction = loaded_model.predict(input_value)
        
        pred = prediction[0]

        if pred == 1:
            print("Rice is the best crop to be cultivated right there")
        elif pred == 2:
            print("Maize is the best crop to be cultivated right there")
        elif pred == 3:
            print("Jute is the best crop to be cultivated right there")
        elif pred == 4:
            print("Cotton is the best crop to be cultivated right there")
        elif pred == 5:
            print("Coconut is the best crop to be cultivated right there")
        elif pred == 6:
            print("Papaya is the best crop to be cultivated right there")
        elif pred == 7:
            print("Orange is the best crop to be cultivated right there")
        elif pred == 8:
            print("Apple is the best crop to be cultivated right there")
        elif pred == 9:
            print("Muskmelon is the best crop to be cultivated right there")
        elif pred == 10:
            print("Watermelon is the best crop to be cultivated right there")
        elif pred == 11:
            print("Grapes is the best crop to be cultivated right there")
        elif pred == 12:
            print("Mango is the best crop to be cultivated right there")
        elif pred == 13:
            print("Banana is the best crop to be cultivated right there")
        elif pred == 14:
            print("Pomegranate is the best crop to be cultivated right there")
        elif pred == 15:
            print("Lentil is the best crop to be cultivated right there")
        elif pred == 16:
            print("Blackgram is the best crop to be cultivated right there")
        elif pred == 17:
            print("Mungbean is the best crop to be cultivated right there")
        elif pred == 18:
            print("Mothbeans is the best crop to be cultivated right there")
        elif pred == 19:
            print("Pigeonpeas is the best crop to be cultivated right there")
        elif pred == 20:
            print("Kidneybeans is the best crop to be cultivated right there")
        elif pred == 21:
            print("Chickpea is the best crop to be cultivated right there")
        elif pred == 22:
            print("Coffee is the best crop to be cultivated right there")
        else:
            print("Sorry, we could not determine the best crop to be cultivated with the provided data.")
    
    st.success(pred)

if __name__ == '__main__':
    main()


