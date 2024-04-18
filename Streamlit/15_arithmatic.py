import streamlit as st

if 'clicked1' not in st.session_state:          #for add
    st.session_state.clicked1=False

if 'clicked2' not in st.session_state:          #for sub
    st.session_state.clicked2=False

def click_button1():                            #for add
    st.session_state.clicked1=True
    st.write('Add button clicked1!')

def click_button2():                            #for sub
    st.session_state.clicked2=True
    st.write('Add button clicked2!')

st.button('ADD',on_click=click_button1)
st.button('SUB',on_click=click_button2)

if(st.session_state.clicked1):
    #the message and nested widget will remain on the page
    st.title("Subtraction program")
    n1=st.number_input("enter n1:")
    n2=st.number_input("enter n2:")
    sum=n1+n2
    st.info("addition of 2 int numbers:")
    st.success(sum)

if(st.session_state.clicked2):
    #the message and nested widget will remain on the page
    st.title("Additon program")
    n1=st.number_input("enter n1:")
    n2=st.number_input("enter n2:")
    sub=n1-n2
    st.info("subtraction of 2 int numbers:")
    st.success(sub)