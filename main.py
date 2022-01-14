import streamlit as st
from pygame import mixer

mixer.init()

music = st.file_uploader("Choose a song.")

try:
    mixer.music.load(music)
except Exception:
    st.write("Please choose a song.")

if st.button("Play"):
    mixer.music.play()

if st.button("Stop"):
    mixer.music.stop()

if st.button("Resume"):
    mixer.music.unpause()

if st.button("Pause"):
    mixer.music.pause()
