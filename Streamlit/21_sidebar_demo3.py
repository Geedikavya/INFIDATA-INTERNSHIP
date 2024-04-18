import streamlit as st

st.sidebar.title("Reg form")
with st.form(key='form1'):
    with st.sidebar:
        user_word=st.text_input("enter a keyword")
        select_language=st.radio('Tweet language',('All','English','Hindi'))
        include_retweets=st.checkbox('Include retweets in data')
        num_of_tweets=st.number_input('minimum number of tweets',100)
        submitted1=st.form_submit_button(label='search Twitter')

st.write("keyword is:",user_word)
st.write("language is:",select_language)