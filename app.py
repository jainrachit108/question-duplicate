import streamlit as st
import model_training
import pickle

model = pickle.load(open('model.pkl', 'rb'))

st.header('Enter questions to check if they are duplicate')

ques1 = st.text_input('Enter question 1')
ques2 = st.text_input('Enter question 2')

if st.button('Check'):
    data = model_training.query_point_creator(ques1, ques2)
    result = model.predict(data)[0]
    
    if result:
        st.header('They are duplicate questions')
    else:
        st.header('They are similar questions')