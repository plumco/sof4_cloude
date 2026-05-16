import streamlit as st
import streamlit.components.v1 as components

# 1. Set to wide mode and hide the sidebar by default
st.set_page_config(page_title="Huliot SO — Sales Order", layout="wide", initial_sidebar_state="collapsed")

# 2. Hide Streamlit's default top header and completely remove all padding
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
    # 3. Make sure this exactly matches your HTML file name on GitHub!
    with open("preview GPT.html", "r", encoding="utf-8") as f:
        html_source_code = f.read()
        
    # 4. Height is increased and scrolling is FALSE to fix the double scrollbar
    components.html(html_source_code, height=1200, scrolling=False)

except FileNotFoundError:
    st.error("Could not find the HTML file. Please make sure the file name matches exactly.")
