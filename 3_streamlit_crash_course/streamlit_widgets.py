from distutils.command.upload import upload
import streamlit as st
import os

st.title("Input Widgets")

# Button
st.header("Button")
button = st.button("Button") # return true or false
if button:
    st.write("You pressed on Button")

# Checkbox (Toggle Button)
st.header("Checkbox")
checkbox = st.checkbox("Do you want to agree ?") # return true or false
if checkbox:
    st.write("You checked the box")

else:
    st.write("You Unchecked")

st.header("Radio Button")
# Radio Button
# from list of value, radio button give use to select one
# value
options = ("India", "USA", "UK", "Australia")
radio_button = st.radio("What is your Favorite Country", options) # return an element in a list/tuple
st.write("You Favourite country is", radio_button)

st.header("Select Box")
# Select Box
options = ("Email", "Phone", "WhatsApp")
select_box = st.selectbox("How would you like to contact", options, index=1)
st.write("You prefered mode of communication is", select_box)

# Slider
st.header("Slider")
slider_range = st.slider("How old are you ?",
                         min_value=1, max_value=100, step=1, value=20)
st.write("You age is", slider_range)

# Text Inputs
st.header("Text Inputs")
name = st.text_input("Enter your Name")
st.write("You name is", name)

age = st.number_input("Enter you age", min_value=1,
                      max_value=100, step=1, value=25)
st.write("You age is", age)

# Upload File
st.header("File Upload")
upload_file = st.file_uploader("Chose a File")

if upload_file is not None:
    st.success("File uploaded succesfully")
    details = {"File Name": upload_file.name,
               "File Type": upload_file.type,
               "File Size(bytes)": upload_file.size}

    st.json(details)   

    # save the file
    path = os.path.join("./upload", upload_file.name)
    with open(path, mode="wb") as f:
        f.write(upload_file.getbuffer())
        st.success("File Saved Successfully")
            