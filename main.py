import streamlit as st

# 처음효과
st.snow()
st.image("https://media.giphy.com/media/3ohs4BSacFKI7A717y/giphy.gif")
st.markdown("""
<div style='text-align: center; font-size: 24px; color: #1f77b4; animation: blinker 1s linear infinite;'>
  ✨ 당신과 닮은 수학자는 누구일까요? ✨
</div>
<style>
@keyframes blinker {
  50% { opacity: 0; }
}
</style>
""", unsafe_allow_html=True)

st.title("🔍 MBTI 기반 수학자 성격 매칭")
st.markdown("MBTI를 선택하세요 😊 당신과 닮은 수학자가 나타납니다!")

mbti_list = ["INTJ","INTP","ENTP","ENTJ","INFJ","INFP","ENFP",
             "ENFJ","ISTJ","ISFJ","ESTJ","ESFJ","ISTP","ISFP","ESTP","ESFP"]

selected = st.selectbox("📌 당신의 MBTI를 골라주세요:", ["-- 선택 --"] + mbti_list)

mbti_math = {
    "INTJ": {
        "name": "에바 카르단",
        "theorem": "삼차방정식 해법 (카르단 공식)",
        "desc": "체계적이고 전략적인 당신과 잘 어울려요.",
    },
    "INTP": {
        "name": "앨버트 아인슈타인",
        "theorem": "E = mc²",
        "desc": "호기심 많고 이론적인 당신!",
    },
    "ENTP": {
        "name": "존 폰 노이만",
        "theorem": "게임 이론",
        "desc": "창의적이고 아이디어 넘치는 당신",
    },
    "ENTJ": {
        "name": "에밀리 노터",
        "theorem": "노터 정리",
        "desc": "리더십 있고 목표 지향적인 당신!",
    },
    "INFJ": {
        "name": "칼 프리드리히 가우스",
        "theorem": "가우스 소거법",
        "desc": "통찰력 있고 신비로운 당신과 닮았어요.",
    },
    "INFP": {
        "name": "소피 제르맹",
        "theorem": "탄성 이론 기초",
        "desc": "감성적이고 창의적인 당신",
    },
    "ENFP": {
        "name": "라마누잔",
        "theorem": "라마누잔 항등식",
        "desc": "열정적이고 독창적인 당신!",
    },
    "ENFJ": {
        "name": "에바 카를레슨",
        "theorem": "최적화 이론",
        "desc": "사교적이고 따뜻한 당신!",
    },
    "ISTJ": {
        "name": "유클리드",
        "theorem": "유클리드 기하학",
        "desc": "논리적이고 신중한 당신",
    },
    "ISFJ": {
        "name": "메리 커리",
        "theorem": "방사능 연구 기초",
        "desc": "섬세하고 배려심 많은 당신",
    },
    "ESTJ": {
        "name": "피에르-시몽 라플라스",
        "theorem": "라플라스 변환",
        "desc": "현실적이고 조직적인 당신",
    },
    "ESFJ": {
        "name": "헨리에타 스완 리빅",
        "theorem": "유전학 연구 공헌",
        "desc": "친절하고 협력적인 당신!",
    },
    "ISTP": {
        "name": "리처드 파인만",
        "theorem": "파인만 다이어그램",
        "desc": "분석적이고 현실적인 당신",
    },
    "ISFP": {
        "name": "에밀리 뒤 샤틀레",
        "theorem": "뉴턴 역학 해석",
        "desc": "예술적이고 자유로운 당신",
    },
    "ESTP": {
        "name": "카를 프리드리히 가우스",
        "theorem": "가우스 분포",
        "desc": "즉흥적이고 행동적인 당신",
    },
    "ESFP": {
        "name": "피에르 드 페르마",
        "theorem": "페르마의 마지막 정리 (간단 버전)",
        "desc": "활발하고 낙천적인 당신!",
    }
}

if selected in mbti_math:
    d = mbti_math[selected]
    st.header(f"🧠 당신과 닮은 수학자: **{d['name']}**")
    st.markdown(f"**설명**: {d['desc']}")
    st.markdown(f"**대표 정리**: {d['theorem']}")

    st.markdown("✉️ 수학자에게 전하고 싶은 말이나 느낀 점을 적어보세요:")
    letter = st.text_area("📩 편지 작성", height=120)
    if st.button("전송하기"):
        st.success("성공적으로 전송했어요! 👍")
        st.write("✉️ 당신의 편지:")
        st.write(letter)
elif selected != "-- 선택 --":
    st.warning("😅 해당 MBTI 정보는 곧 준비할게요!")
