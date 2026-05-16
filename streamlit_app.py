import streamlit as st
import streamlit.components.v1 as components

# Set the page title and layout to be wide
st.set_page_config(page_title="Huliot SO — Sales Order", layout="wide")

# Open and read your HTML file
try:
    with open("huliot_so_app.html", "r", encoding="utf-8") as f:
        html_source_code = f.read()
        
    # Display the HTML inside the Streamlit app
    # You can change the height number if it gets cut off
    components.html(html_source_code, height=800, scrolling=True)

except FileNotFoundError:
    st.error("Could not find the file 'huliot_so_app.html'. Please make sure it is in the same folder.")
