import streamlit as st

col1,col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Himanshu")
    content = """
    Hi, Iam Hiamnshu! Himanshu Rana graduated 
    with a B.Tech degree in 2022. 
    After graduation, he completed a course 
    in Data Science and Machine Learning. 
    He is now equipped with skills to pursue 
    opportunities in the tech industry.
"""  
    st.write()