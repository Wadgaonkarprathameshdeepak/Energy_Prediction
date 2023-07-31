import streamlit as st;
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn  as  sns
# from pydataset 
from PIL import Image


# ds = pd.read_csv("ml_data_set.csv")
#data = explore_data(ds)
image = Image.open('ml.png')
st.title("Home Waste Management")
menu = st.sidebar.image(image, caption='Sunrise by the mountains')
st.sidebar.write("India generates over 60 million tonnes of garbage daily, of which 75% is untreated and dumped in landfills, according to a report")
year = st.selectbox(
    "Year",(2010,2011,2012,2013,2014,2015,2016,2017,2018) 
    )
st.write('Year : ',year)

waste = st.selectbox(
    "Waste Type",('Food waste','Paper/Cardboard','Plastics','Construction Debris','Wood/Timber','Horticultural Waste','Ferrous Metal','Non-ferrous Metals','Used Slag','Sludge','Glass','Textile/Leather','Scrap Tyres','Others (stones, ceramics & rubber etc)'))
st.write('type : ',waste)
rate = st.number_input("Enter the recycling rate",max_value = 1.0000 , min_value = 0.0000)
button = st.button("Predict")
# <h1 class="text-center"> Home Waste Management of Aurangabad  </h1>
#  <option value="reeses-2">Wood/Timber</option> 
#         <option value="reeses-3">Horticultural5 Waste</option> 
#         <option value="reeses-4">Ferrous Metal</option> 
if button:
    val = 0.3  
    # check if the recycle rate is greater than 30%
    if rate >= val: 
        st.success("Energy Can Be Generated from ")
    else:
        st.success("Energy Cannot be Generated from ")





    
    
    

   