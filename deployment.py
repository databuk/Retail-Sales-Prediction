import streamlit as st


import pandas as pd
import joblib
import numpy as np
from data_cleaner import clean_data


pipeline = joblib.load('sales_pipeline.joblib')

def collect_user_input():
    item_weight = st.number_input('Item Weight', min_value=0, max_value=50, value='min')
    item_fat_content =  st.selectbox('Item Fat Content', ['Regular', 'Low'])
    item_visibility = st.slider('Item Visibility', min_value=0.0, max_value=1.0, value=0.0, step=0.1)

    item_type = st.selectbox('Item Type', options=['Fruits and Vegetables', 'Household', 'Meat', 'Snack Foods',
        'Dairy', 'Others', 'Baking Goods', 'Soft Drinks', 'Hard Drinks',
        'Health and Hygiene', 'Breads', 'Canned', 'Frozen Foods',
        'Seafood', 'Starchy Foods', 'Breakfast'])
    item_mrp = st.number_input('Item MRP', min_value=0, max_value=500, value='min')
    outlet_size = st.selectbox('Outlet Size', options=['Medium', 'Small', 'High'])
    outlet_location = st.selectbox('Outlet Location Type', options=['Tier 1', 'Tier 2', 'Tier 3'])
    outlet_type = st.selectbox('Outlet Type', options=['Supermarket Type1', 'Grocery Store', 'Supermarket Type3',
        'Supermarket Type2'])
    input_data = pd.DataFrame([[item_weight, item_fat_content, item_visibility, item_type, item_mrp, 
                                  outlet_size, outlet_location, outlet_type]], columns=['item_weight', 'item_fat_content', 'item_visibility', 'item_type',
       'item_mrp', 'outlet_size', 'outlet_location_type', 'outlet_type'])
    return input_data
       

st.title('Retail Sales Prediction App')
st.write('Enter data to predict revenue')
input_data = collect_user_input()
if st.button('Predict'):
    with st.spinner('Calculating Prediction...'):
        prediction = pipeline.predict(input_data)
        st.success(f'The total sales revenue is ${int(np.round(prediction))}.')
