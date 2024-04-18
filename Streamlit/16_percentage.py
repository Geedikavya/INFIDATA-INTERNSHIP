import streamlit as st

n=st.number_input("enter the percentage of the student")
if(n>90):
    st.info("grade A")
elif(n>80 and n<=90):
    st.info("grade B")
elif(n>=60 and n<=80):
    st.info("grade C")
else:
    st.info("grade D")
    