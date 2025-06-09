import streamlit as st
import time

st.title("🍽️ MBTI별 저녁 메뉴 추천 서비스")
st.markdown("각 글자를 골라서 당신의 MBTI를 완성해 보세요! 😋")

# 1글자씩 선택 (기본값 None으로 설정)
first = st.radio("1번째 글자: E or I?", ('E', 'I'), index=None, horizontal=True)
second = st.radio("2번째 글자: N or S?", ('N', 'S'), index=None, horizontal=True)
third = st.radio("3번째 글자: F or T?", ('F', 'T'), index=None, horizontal=True)
fourth = st.radio("4번째 글자: J or P?", ('J', 'P'), index=None, horizontal=True)

# 선택 글자 확인
selected_letters = [first, second, third, fourth]

if None not in selected_letters and all(selected_letters):
    selected_mbti = "".join(selected_letters)
    st.write("⏳ 추천 메뉴를 준비 중입니다...")
    time.sleep(2)  # 2초 딜레이

    mbti_menu = {
        "INTJ": ("그릴 치킨 샐러드 🥗🍗", "건강하고 깔끔한 한 끼를 원한다면!"),
        "INTP": ("수제 버거와 감자튀김 🍔🍟", "창의적인 맛의 조합, 실험정신 가득!"),
        "ENTP": ("매콤 떡볶이와 튀김 세트 🌶️🍤", "활기차고 즐거운 저녁을 원한다면!"),
        "ENTJ": ("스테이크와 와인 🍷🥩", "리더의 품격 있는 메뉴!"),
        "INFJ": ("크림 파스타와 샐러드 🍝🥗", "부드럽고 깊은 맛을 즐기고 싶다면!"),
        "INFP": ("비건 볼로네제 파스타 🍝🌱", "감성 가득, 자연을 생각한 메뉴"),
        "ENFP": ("바비큐 폭립과 콜슬로 🍖🥗", "열정 넘치는 맛과 분위기!"),
        "ENFJ": ("치킨 카레와 난 🍛🍗", "따뜻하고 정겨운 한 끼!"),
        "ISTJ": ("된장찌개와 밥 🍲🍚", "전통적인 맛을 선호한다면!"),
        "ISFJ": ("김치찌개와 삼겹살 🍖🥢", "정성 가득한 집밥 스타일!"),
        "ESTJ": ("갈비찜과 밥 🍖🍚", "튼튼하고 든든한 한 끼!"),
        "ESFJ": ("제육볶음과 상추쌈 🌶️🥬", "사교적이고 맛있는 메뉴!"),
        "ISTP": ("초밥 세트 🍣", "깔끔하고 신선한 맛!"),
        "ISFP": ("양송이 리조또 🍄🍚", "감성적이고 부드러운 맛!"),
        "ESTP": ("피자와 맥주 🍕🍺", "즉흥적이고 즐거운 분위기!"),
        "ESFP": ("치즈 돈까스와 샐러드 🧀🍤", "활발하고 맛있는 한 끼!"),
    }

    if selected_mbti in mbti_menu:
        menu, desc = mbti_menu[selected_mbti]
        st.balloons()
        st.header(f"🍽️ 당신의 MBTI: **{selected_mbti}**")
        st.subheader(f"오늘의 추천 메뉴: **{menu}**")
        st.markdown(f"✨ {desc}")
    else:
        st.error("😅 아직 준비 중인 MBTI입니다!")
else:
    st.info("🔎 4글자를 모두 선택해주세요!")
