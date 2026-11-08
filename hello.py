from numpy import select
import streamlit as st
st.header("shapes calculations")
with st.sidebar:
    shape = st.selectbox("Select a shape", ["Circle", "Rectangle"])
print(shape)
if shape == "Circle":
    radius = st.number_input("radius", min_value=0, max_value=100, step=1)
    area = 3.14 * radius * radius
    perimeter = 2 * 3.14 * radius

if shape == "Rectangle":
    height = st.number_input("height", min_value=0, max_value=100, step=1)
    width = st.number_input("width", min_value=0, max_value=100, step=1)
    area = height * width       
    perimeter = 2 * (height + width)
compute = st.button("compute area and perimeter")
if compute:
    st.write("Area:", area)
    st.write("Perimeter:", perimeter)
    st.sidebar.title("configuration")