import streamlit as st

# a = st.sidebar.radio('R:',[1,2])
st.title('Hi My Name is Phil!')
st.text("I'm interested in Quantum Computing")
st.image('./photo.png')
st.header("Heres a cool equation:")
st.latex(r''' e^{i\pi} + 1 = 0 ''')