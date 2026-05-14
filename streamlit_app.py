import streamlit as st
import streamlit.components.v1 as components

# Set page to wide mode to fit your HTML content
st.set_page_config(layout="wide")

# Read your HTML file
with open("huliot_so_app.html", 'r', encoding='utf-8') as f:
    html_content = f.read()

# Render the HTML in the app
components.html(html_content, height=800, scrolling=True)