import streamlit as st
from pygame import mixer

mixer.init()

music = input("C:/Users/ASUS/Desktop/web app/pages/topic_sum.wav")

try:
    mixer.music.load(music)
except Exception:
    st.write("please choose a song")

if st.button("play"):
    mixer.music.play()

if st.button("stop"):
    mixer.music.stop()

if st.button("Resume"):
    mixer.music.unpause

if st.button("Pause"):
    mixer.music.pause()
    