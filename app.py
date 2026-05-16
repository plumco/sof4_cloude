import streamlit as st
import streamlit.components.v1 as components

# You can update the title for this specific page
st.set_page_config(page_title="Customer Sales Report", layout="wide", initial_sidebar_state="collapsed")

# Hide Streamlit's default top header and completely remove all padding
st.markdown("""
    <style>
        /* Hide the Streamlit top menu bar */
        header[data-testid="stHeader"] {
            display: none !important;
        }
        /* Remove padding to push the app to the absolute edges */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
        }
    </style>
""", unsafe_allow_html=True)

try:
    # ⚠️ REPLACE THIS STRING WITH YOUR ACTUAL HTML FILE NAME ⚠️
    with open("YOUR_NEW_FILE_NAME.html", "r", encoding="utf-8") as f:
        html_source_code = f.read()
        
    # Increase height if it cuts off at the bottom, and keep scrolling=False
    components.html(html_source_code, height=1200, scrolling=False)

except FileNotFoundError:
    st.error("Could not find the file. Please make sure it is in the same folder.")
