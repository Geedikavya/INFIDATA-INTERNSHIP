import streamlit as st

st.title("Online banking")
#sidebar
st.sidebar.title("Welcome to SBI")
choice=st.sidebar.selectbox('create your account',('None','create account'))
selected_status=st.sidebar.selectbox('select',options=['None','Deposit','Withdraw','Display'])

if choice=='create account':
    name=st.text_input("Name")
    id=st.number_input("Customer id")
    branch=st.text_input("Branch")
    initial=st.number_input("Initial amount")
if selected_status=='Deposit':
    dep = st.number_input("enter an amount to deposit:")
    balance = initial + dep

    st.write("updated balance after deposit:", balance)
elif selected_status=='Withdraw':
    withdraw = st.number_input("enter an amount to withdraw:")
    if (initial >= withdraw):
        balance = initial - withdraw
        st.write("updated balance after withdraw:", balance)
    else:
        st.warning("insufficient balance")
elif selected_status=='Display':
    st.write("Name is:", name)
    st.write("customer id is:", id)
    st.write("branch is:", branch)
    st.write("initial amount is:", initial)




