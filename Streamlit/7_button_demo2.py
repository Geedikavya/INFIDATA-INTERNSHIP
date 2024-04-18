import streamlit as st

if'clicked' not in st.session_state:
    st.session_state.clicked=False

def click_button():
    st.session_state.clicked=True
    st.write('Button clicked!')

st.button('click me',on_click=click_button)

if st.session_state.clicked:
    # the message and nested widget will remain on the page
    st.title("hello user....!")
    st.slider('Select a value')
    st.info("demo")
