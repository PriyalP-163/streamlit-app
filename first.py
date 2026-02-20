import streamlit as st
import pandas as pd
import numpy as np

st.title("My First Streamlit App")
st.write("Hello, this is my first Streamlit app!")
st.text("Let's start ")

#Creating Charts using pandas and numpy
df=pd.DataFrame(np.random.randn(10, 2), columns=['A', 'B'])
st.line_chart(df)
st.bar_chart(df)

# Slidebar, image and video
st.sidebar.title("Sidebar")
st.image("https://www.shutterstock.com/image-photo/sun-sets-behind-mountain-ranges-600nw-2479236003.jpg", width=400, caption="Beautiful Sunset")
st.video("https://www.youtube.com/watch?v=3ScAXwLEvB0&list=RD3ScAXwLEvB0&start_radio=1")

#file upload (csv)
uploaded_file=st.file_uploader("Choose a file",type='csv')
if uploaded_file:
    df=pd.read_csv(uploaded_file)
    st.write(df)

#Taking user input
name=st.text_input("Enter your name")
st.write(f"Hello, {name}!")    

# Text and markdown formatting
st.header ("This is a header"  )
st.subheader("This is a subheader")
st.markdown("This is **bold** text and this is **italic** text, 'code', [line](https://streamlit.io)")
st.code("for i in range(5):\n    print(i)", language="python")

st.text_input("what's your name?")
st.text_area("Tell us about yourself")
st.number_input("Enter a number", min_value=0, max_value=100, value=50)
st.date_input("Select a date")
st.slider("Select a range", 0, 100, (25, 75))
st.selectbox("Choose a fruit", ["Grapes", "Apple", "Mango", "Banana"])
st.multiselect("Select topings", ["chocolate", "sprinkles", "Chocolate Chips"])
st.radio("Choose a color", ["Red", "Green", "Blue"])
st.checkbox("I agree to the terms and conditions ")

#Matplotlib Integration
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot([1,2,3], [4,5,6])
st.pyplot(fig)

