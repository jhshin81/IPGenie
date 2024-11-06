# main.py

import streamlit as st
from utils.ui_elements import load_images, set_styles, display_footer, display_example_questions
from utils.chat_chain import initialize_chain, add_message, print_messages, handle_user_input

# 초기 설정 및 이미지 로드
st.set_page_config(page_title="IP Genie", page_icon="./images/icon.png")
images = load_images()
st.image(images["main"], width=300)

# 스타일 적용
set_styles()

# UI - 사용자 입력 및 예시 질문 표시
user_input = st.text_input("IP Genie에게 궁금한 내용을 물어보세요!")
display_example_questions()

# 세션 상태 초기화 및 대화 처리
if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "chain" not in st.session_state:
    st.session_state["chain"] = initialize_chain()

# 사용자 입력 처리 및 응답 표시
print_messages()
if user_input:
    handle_user_input(user_input)

# 하단 푸터 표시
display_footer()
