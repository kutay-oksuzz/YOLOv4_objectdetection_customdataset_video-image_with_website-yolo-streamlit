import streamlit as st



# will display text, dataframe, graph, images
st.write("Hello World")

# text formating
st.header("This is Header")
st.subheader("This is subheader")
st.caption('This is plain text')
st.text("This is planin text")

# markdown
st.markdown("""
# This is title
## This header
### subheader -1
#### subheader -2

simple plain text
for *italic* use asterisk
for **bold** format use two asterisk
""")

# status elements
# success
st.success("this message display text in green bacground")
# warning
st.warning("this message display text in yellow background")
# error
st.error("this message display text in red background")



# Display media
# images and videos
st.subheader("Display Image")

st.image("./media/mountains.webp", caption="mountains", width=500)

st.subheader("Display video")
video_file = open("./media/star.mp4", mode="rb").read()
st.video(video_file)