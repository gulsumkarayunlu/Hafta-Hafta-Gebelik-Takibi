import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="Hafta Hafta Gebelik Rehberi", page_icon="👶", layout="wide")

HTML_PATH = os.path.join(os.path.dirname(__file__), "gebelik_site.html")

with open(HTML_PATH, "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=1400, scrolling=True)