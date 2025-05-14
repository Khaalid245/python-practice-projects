import streamlit as st
import pandas

st.set_page_config(layout="wide")
st.title("The Best Company")

content = """
Alif Code Academy is a tech education platform that empowers youth in Somalia by offering 
free courses in programming, design, and digital skills. It aims to bridge 
the digital gap and foster innovation through accessible, high-quality learning resources
The academy also focuses on empowering women and underserved communities, promoting inclusive and 
equitable access to technology education.
"""

st.write(content)

st.title("our team")

col1, col2, col3 = st.columns(3)
df = pandas.read_csv("data1.csv")

# Handle the issue by stripping extra spaces from column names


with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row['role'])
        st.image("imaging/" + row['image'])


with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row['role'])
        st.image("imaging/" + row['image'])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row['role'])
        st.image("imaging/"+ row['image'])

