
import streamlit as st
col1,col2 = st.beta_columns(2)
st.sidebar.title("Data Import")
uploaded_file = st.sidebar.file_uploader("Choose a file")
st.sidebar.markdown("<b>Metadata<b>", unsafe_allow_html=True)
st.sidebar.text_input("Provide Report-Schedule")
st.sidebar.text_input("Provide Region Country")
st.sidebar.text_input("Provide Product")
st.sidebar.markdown("<b>User Inputs<b>", unsafe_allow_html=True)
st.sidebar.selectbox("Select Sheet","1")
st.sidebar.text_input("Provide Business Meta data Columns")
st.sidebar.text_input("Provide Source Lineage Group Columns")
st.sidebar.text_input("Provide Target Lineage Group Columns ")
col1.title("Source")
col1.text_input("Application Name/CSI")
col1.text_input("Dataset Types")
col1.text_input("Dataset Names")
col1.button("Recommend Datasets based on Table")
col2.title("Target")
col2.text_input("Application Name/CSI",key=1)
col2.text_input("Dataset Types",key=1)
col2.text_input("Dataset Names",key=2)
col2.button("Recommend Datasets based on Table",key=1)
st.markdown("<b>Export Options<b>", unsafe_allow_html=True)
st.button("Export to Excel Format")
st.button("Load into Data  Quality Manager")