# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pickle
import numpy as np
import scipy.sparse.linalg
import streamlit as st
from streamlit_option_menu import option_menu

loaded_model = pickle.load(open("crop_model.pkl",'rb'))
soil_model = pickle.load(open("soil_fertility.pkl",'rb'))


with st.sidebar:
    selected = option_menu('Crop Recommendation Web app',
                           ['Crop Recommendation system','Soil Fertility Check'],
                           default_index = 0)


    
def main():
    
    
    if (selected == 'Crop Recommendation system'):
        st.title("Crop Recommendation System")
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
        
    if (selected == 'Soil Fertility Check'):
        st.title("Soil Fertility Check")
        
        col1,col2,col3,col4= st.columns(4)
        
        with col1:
            pH = st.text_input('pH')
    
        with col2:
            EC =st.text_input("EC")
    
        with col3:
            OC = st.text_input('OC')
    
        with col4:
            OM = st.text_input('OM')
    
        with col1:
            N = st.text_input('N')
    
        with col2:
            P = st.text_input('P')
    
        with col3:
            K = st.text_input('K')
    
        with col4:
            Zn = st.text_input('Zn')
    
        with col1:
            Fe = st.text_input('Fe')
    
        with col2:
            Cu = st.text_input('Cu')
    
        with col3:
            Mn = st.text_input('Mn')
    
        with col4:
            Sand = st.text_input('Sand')
    
        with col1:
            Silt = st.text_input('Silt')
            
        with col2:
            Clay = st.text_input('Clay')
            
        with col3:
            CaCO3 = st.text_input('CaCO3')
            
        with col4:
            CEC = st.text_input('CEC')
        
        
        soil_fertility = ''
        
        
        if st.button('Soil Test Result'):
            input_value = np.array([[pH,EC,OC,OM,N,P,K,Zn,Fe,Cu,Mn,Sand,Silt,Clay,CaCO3,CEC]])
            
            s_pred = soil_model.predict(input_value)
            
            soil_fertility = s_pred[0]
            
            if (soil_fertility == 0):
                soil_fertility = 'The soil is fertile'
            else:
                soil_fertility = 'The soil is not Fertile'
    
        st.success(soil_fertility)
        
        
        
if __name__ == '__main__':
    main()
