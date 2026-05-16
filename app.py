import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Huliot SO — Sales Order", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        header[data-testid="stHeader"] { display: none !important; }
        .block-container { padding: 0rem !important; }
    </style>
""", unsafe_allow_html=True)

try:
    # Notice the 4 spaces before "with"!
    with open("huliot_so_app.html", "r", encoding="utf-8") as f:
        html_source_code = f.read()
        
    components.html(html_source_code, height=1200, scrolling=False)

except FileNotFoundError:
    # Notice the 4 spaces before "st.error"!
    st.error("Could not find the HTML file. Please make sure the file name matches exactly.")
