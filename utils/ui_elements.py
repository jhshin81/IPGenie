# utils/ui_elements.py

import streamlit as st
from PIL import Image
import base64

# 이미지 로드 함수
def load_images():
    return {
        "icon": Image.open("./images/icon.png"),
        "main": Image.open("./images/main.png"),
        "sponsor": Image.open("./images/sponsor.png"),
    }

# 스타일 적용 함수
def set_styles():
    st.markdown("""
        <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
        /* 기타 스타일 */
        </style>
        """, unsafe_allow_html=True)

# 예시 질문 표시 함수
def display_example_questions():
    example_questions = [
        "글로벌 배터리 시장 동향에 대해 알려줘!",
        "마이크로소프트의 특허관련 최근 이슈는 뭐야?",
    ]
    st.markdown("<div class='section-title'>예시 질문들:</div>", unsafe_allow_html=True)
    cols = st.columns(2)
    for i, question in enumerate(example_questions):
        cols[i % 2].markdown(f"<div class='suggestion-item'>{question}</div>", unsafe_allow_html=True)

# 푸터 표시 함수
def display_footer():
    sponsor_base64 = get_base64_image("./images/sponsor.png")
    st.markdown(f"""
        <style>
        .footer {{
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
            text-align: center;
            padding: 10px;
            font-size: 14px;
            color: #555;
        }}
        .footer img {{
            width: 250px;
            vertical-align: middle;
            margin: 0 10px;
        }}
        </style>
        <div class="footer">
            © 2024 IPGenie | Created by IPdaily & Wert Intelligence <br>
            <img src="data:image/png;base64,{sponsor_base64}" alt="Sponsor">
        </div>
        """, unsafe_allow_html=True)

# Base64 인코딩된 이미지 생성 함수
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

