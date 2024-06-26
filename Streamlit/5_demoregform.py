import streamlit as st
import datetime

#giving a title
st.title('Registration Form')

#creating a form
my_form=st.form(key='form')

#creating input fields
fname=my_form.text_input('First Name:')
lname=my_form.text_input('Last Name:')
email=my_form.text_input('Email:')

#creating radio button
gender=my_form.radio('Gender',('Male','Female'))

#creating slider
age=my_form.slider('Age:',1,70)

#creating date picker
bday=my_form.date_input('Enter Birthdate:',min_value=datetime.date(1980,1,1))

#creating text area
address=my_form.text_area('Enter Address:')

file=my_form.file_uploader('Upload your resume')

#creating a submit button
submit=my_form.form_submit_button('Submit')

#the following gets updated after clicking on submit,printing the details of the fields that are submitted
st.write('Name is:'+fname+' ',lname)
st.write('Email is:',email)
st.write('Gender is:',gender)
st.write('Age is:',age)
st.write('Birthday is:',bday)
st.write('Address is:',address)
st.success(file)


