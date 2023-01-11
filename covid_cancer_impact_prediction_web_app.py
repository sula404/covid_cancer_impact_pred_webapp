# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 00:26:04 2023

@author: Dilshan Withanage
"""

import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


loaded_model = pickle.load(open('lc-predict.sav', 'rb'))


def lc_dtct(input_data):
    input_data_as_numpy_array = np.asarray(input_data, dtype=float)

    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]== 0):
      return 'This person does not have an impact of COVID-19 on Liver Cancer'
    else:
      return 'This person has an impact of COVID-19 on Liver Cancer'
      

def main():
    
    st.header('PredXpert©️')
    
    st.subheader('COVID-19 Impact on Liver Cancer Predictor')
    
    with st.sidebar:
        
        selected = option_menu('Developer',
                              
                              ['D.S.P.WITHANAGE',
                               '2019521460115'],
                              icons=['person-circle'],default_index=-1)
    
  
    Bleed = st.text_input('Spontaneous Tumour Haemorrhage [ "Yes" = 1 / "No" = 0 / "NA" = 0 ]')
    Age = st.text_input('Age of the patitent')
    Gender = st.text_input('Gender [ "Male" = 1 / "Female" = 0 ]')
    Cirrhosis = st.text_input('Underlying Liver Disease [ "Yes" = 1 / "No" = 0 / "NA" = 0 ]')
    Size = st.text_input('Tumour Diameter in Millimeters(mm) [ "NA" = 0 ]')
    HCC_TNM_Stage = st.text_input('Hepatocellular Carcinoma Tumour Node Metastasis Stage [ "I" = 1 / "II" = 2 / "IIIA+IIIB" = 3 / "IV" = 4 / "NA" = 0 ]')
    HCC_BCLC_Stage = st.text_input('Hepatocellular Carcinoma Barcelona Clinic for Liver Cancer Stage [ 0 / "A" = 1 / "B" = 2 / "C" = 3 / "D" = 4 / "NA" = 0 ]')
    PS = st.text_input('Performance Status [0, 1, 2, 3, 4]')
    Prev_known_cirrhosis = st.text_input('Previous known Cirrhosis [ "Yes" = 1 / "No" = 0 / "NA" = 0 ]')
    
    
    dtct = ''
    
    
    if st.button('Predict COVID-19 Impact on Liver Cancer'):
        dtct = lc_dtct([Bleed,Age,Gender,Cirrhosis,Size,HCC_TNM_Stage,HCC_BCLC_Stage,PS,Prev_known_cirrhosis])
        
    st.success(dtct)
    
    
   
if __name__ == '__main__':
    main()
