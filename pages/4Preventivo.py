import streamlit as st
from services.connect import preventivo


try:
    logado = st.session_state['Login']
except:
    st.switch_page('./Login.py')


st.title('Pedidos Pendentes')

st.dataFrame(preventivo(st.session_state['Usuário']))
