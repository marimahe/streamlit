import streamlit as st

st.title('🤖 Mahi Lab 🔭🚀')

st.write('Hello world! this is my first streamlit app')
st.info('this is an experiment')
#st.balloons()
#st.snow()
st.toast("Warming up...")
st.error("Error message")
st.button("Done")


# Two equal columns:
col1, col2 = st.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")

# Three different columns:
col1, col2, col3 = st.columns([3, 1, 1])
# col1 is larger.

# Bottom-aligned columns
col1, col2 = st.columns(2, vertical_alignment="bottom")

# You can also use "with" notation:
with col1:
    st.radio("Select one:", [1, 2])
  
st.button("Click me")
#st.download_button("Download file", data)
st.feedback("thumbs")
#st.link_button("Go to gallery", url)
#st.page_link("app.py", label="Home")
#st.data_editor("Edit data", data)
st.checkbox("I agree")
st.toggle("Enable")
st.radio("Pick one", ["cats", "dogs"])
st.selectbox("Pick one", ["cats", "dogs"])
st.multiselect("Buy", ["milk", "apples", "potatoes"])
st.slider("Pick a number", 0, 100)
st.select_slider("Pick a size", ["S", "M", "L"])
st.text_input("First name")
st.number_input("Pick a number", 0, 10)
st.text_area("Text to translate")
st.date_input("Your birthday")
st.time_input("Meeting time")
st.file_uploader("Upload a CSV")
st.camera_input("Take a picture")
st.color_picker("Pick a color")
