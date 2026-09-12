"""Streamlit launcher for the AURA Studio single-page application."""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

BASE_DIR = Path(__file__).resolve().parent
BUNDLE_PATH = BASE_DIR / "index.html"

st.set_page_config(
    page_title="AURA Studio — Spatial Drawing & Gesture Control",
    page_icon=str(BASE_DIR / "favicon.svg"),
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        html, body {
            margin: 0 !important;
            padding: 0 !important;
            background: #09090b !important;
            overflow: hidden !important;
        }
        [data-testid="stAppViewContainer"],
        [data-testid="stMain"],
        [data-testid="block-container"] {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }
        section[data-testid="stSidebar"],
        [data-testid="collapsedControl"],
        header,
        footer {
            display: none !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

if not BUNDLE_PATH.exists():
    st.error("AURA Studio bundle is missing. Run `python build.py` from the project folder first.")
    st.stop()

html = BUNDLE_PATH.read_text(encoding="utf-8")
components.html(html, height=1000, scrolling=False)
