import streamlit as st

#using object notation
add_selectbox=st.sidebar.selectbox(
    "how would you like to be contacted?",
    ("Email","Home phone","Mobile phone")
)

#using "with" notation
with st.sidebar:
    add_radio=st.radio(
        "choose a shipping method",
        ("standard (5-15 days)","express(2-5 days)")
    )
    name=st.text_input("enter customer name:")