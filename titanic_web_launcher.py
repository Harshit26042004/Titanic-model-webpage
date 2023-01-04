# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
import streamlit as sl

load_depmod = pickle.load(open('deployer.sav','rb'))

def depfunc(input_data):
    input_dupdata = np.asarray(input_data)
    input_mod_data = input_dupdata.reshape(1,-1)
    predictor = load_depmod.predict(input_mod_data)
    print(predictor)
    
    if(predictor[0]==1):
        return "Survived"
    else:
        return "not survived"
    
def main():
    sl.title("Titanic survivor predictor")
    
    pclass=sl.text_input("Passenger class")
    age=sl.slider("select your Age",1,100)
    sl.text(age)
    fare=sl.text_input("Fare")
    female=sl.text_input("Female")
    male=sl.text_input("male")
    
    depl=""
    
    if(sl.button("Predict the survivity")):
        depl=depfunc([pclass,age,fare,female,male])
        
        
    if(depl=="Survived"):
        sl.success(depl)
    else:
        sl.error(depl)
    
    
if __name__=='__main__':
    main()
