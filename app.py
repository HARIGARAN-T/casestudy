# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 16:37:22 2021

@author: hari
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st 
import base64

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return



pickle_in = open("linear.pkl","rb")
regressor=pickle.load(pickle_in)



def predict(a):
    prediction=regressor.predict(a)
    print(prediction)
    return prediction

def main():
    st.title("Order Value of food - Prediction App")

    set_png_as_page_bg('pic2.png')
    col1, col2 = st.columns(2)
    with col1:
        restaturantid = st.selectbox("RestaturantID",[  2,   3,   4,   5,   6,   7,   8,   9,  10,  12,  13,  14,  15,
        16,  18,  19,  20,  21,  23,  25,  26,  27,  28,  29,  30,  31,
        32,  34,  36,  37,  38,  39,  41,  43,  44,  45,  46,  47,  48,
        49,  50,  53,  54,  55,  57,  58,  59,  62,  63,  64,  66,  68,
        69,  70,  71,  72,  76,  77,  78,  79,  80,  81,  83,  84,  86,
        87,  88,  89,  90,  91,  92,  93,  94,  95,  96,  97,  98,  99,
       100, 101, 104, 105, 106, 107, 109, 111, 112, 114, 115, 116, 120,
       121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 135,
       137, 138, 139, 140, 142, 143, 147, 148, 150, 151, 154, 155, 156,
       158, 159, 160, 161, 162, 163, 165, 166, 168, 169, 170, 172, 174,
       175, 176, 177, 178, 179, 181, 182, 183, 185, 186, 187, 188, 190,
       191, 194, 195, 196, 197, 200, 201, 205, 207, 209, 210, 211, 212,
       213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225,
       226, 227, 228, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241,
       242, 243, 245, 246, 247, 248, 249, 250, 251, 252, 253, 255, 256,
       257, 258, 259, 260, 262, 263, 264, 265, 266, 267, 268, 269, 270,
       271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283,
       284, 288, 289, 292, 294, 295, 296, 297, 298, 300, 301, 302, 303,
       304, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317,
       318, 319, 320, 321, 322, 324, 325, 326, 328, 329, 330, 331, 332,
       333, 334, 335, 337, 338, 339, 340, 341, 342, 343, 345, 346, 347,
       348, 349, 350, 351, 352, 353, 355, 356, 357, 358, 360, 361, 362,
       363, 367, 369, 370, 371, 372, 373, 379, 380, 383, 388, 389, 390,
       393, 397, 400, 401, 407, 408, 409])
        superorder= st.selectbox("SuperOrder",["True","False"])
        amountoftip = st.text_input("Amount of tip - customer wishes to give","  ")
    with col2:
        deliveryregion= st.selectbox("Deliveryregion",['Bengaluru','Delhi','Mumbai'])
        date= st.selectbox("DATE",[1,2,3,4,5,6,7,8,9,10,11,12,13,14,
                                15,16,17,18,19,18,19,20,21,22,23,24,25,
                                26,27,28,29,30,31])
        time= st.selectbox("Time",['Early_Morning','Morning','Afternoon','Late_Night'])
   
    if    deliveryregion ==  'Bengaluru':
        Bengaluru = 1
        Delhi = 0
        Mumbai = 0
    elif deliveryregion == 'Delhi':
        Bengaluru = 0
        Delhi = 1
        Mumbai = 0
    else :
        Bengaluru = 0
        Delhi = 0
        Mumbai = 1
        
    if superorder == "True":
        true=1
        false=0
    else:
         true=0
         false=1
    if time == 'Early_Morning':
        AFTERNOON =0
        Early_Morning=1
        LATE_NIGHT=0
        MORNING=0
    elif time == 'Morning':
        AFTERNOON =0
        Early_Morning=0
        LATE_NIGHT=0
        MORNING=1
    elif time == 'Afternoon':
        AFTERNOON =1
        Early_Morning=0
        LATE_NIGHT=0
        MORNING=0
    else:
        AFTERNOON =0
        Early_Morning=0
        LATE_NIGHT=1
        MORNING=0
    d=[[restaturantid,amountoftip,date,Bengaluru,Delhi,Mumbai,AFTERNOON,Early_Morning,
          LATE_NIGHT,MORNING,false,true]]
    data =pd.DataFrame(d, columns=[['Restaurant ID','Amount of tip','Date','Bengaluru',
               'Delhi', 'Mumbai',     'AFTERNOON', 'EARLY MORNING',
          'LATE NIGHT','MORNING','False','True']])
 
    result=""
    if st.button("Predict"):
        result=predict(data)
    st.success('The output is {}'.format(result))
   
if __name__=='__main__':
    main()
