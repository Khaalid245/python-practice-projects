import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Khalid Abdillahi")
    content= """
    Khalid Abdirahman Abdillahi is a dedicated educator and software engineering student passionate 
    about improving education in Somalia. He builds free tech learning platforms to empower youth 
    and underserved communities. Khalid blends technical skills with a strong social 
    mission to drive positive change
    """
    st.info(content)

content2 ="""
below you can find some of the apps I have built in python feel free to contact me.
"""
st.write(content2)


col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv",sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[source code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[source code]({row['url']})")


