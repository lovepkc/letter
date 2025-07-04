import streamlit as st
import time

import config

if 'show_video_letter' not in st.session_state:
    st.session_state.show_video_letter = False

@st.dialog("영상 편지")
def show_dlg_video_letter():
    st.subheader("답장 영상")
    st.video("test.mp4", format="video/mp4", autoplay=True)  

st.title("영상 편지")
st.markdown(config.CI, unsafe_allow_html=True)
st.markdown(config.FONT, unsafe_allow_html=True)

st.subheader("편지 쓰기")
txt_letter = st.text_area(label="그리움을 담아 정성스럽게 편지를 작성해 주세요.", 
                          value=config.LETTER, 
                          height=180, 
                          max_chars=300)

if st.button("편지 보내기"):
    st.session_state.show_video_letter = True
    time.sleep(3)
    
    st.subheader(":mailbox_with_mail: 답장이 도착했습니다.")

if st.session_state.show_video_letter:

    if st.button("답장 확인"):
        time.sleep(2)
        show_dlg_video_letter()