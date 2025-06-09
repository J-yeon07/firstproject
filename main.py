import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="MBTI 영화 추천기 🎬", page_icon="🎥")

# 제목
st.title("🎬 MBTI별 수학·과학 영화 추천기 💡")
st.markdown("너의 MBTI로 🎭 취향 저격 🎯 영화 한 편 골라줄게! 과학과 수학의 세계로 ✨풍~덩✨")

# MBTI 리스트
mbti_list = [
    "INTJ", "INTP", "ENTP", "ENTJ",
    "INFJ", "INFP", "ENFP", "ENFJ",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 선택 박스에서 MBTI 선택
selected_mbti = st.selectbox("👇 아래에서 당신의 MBTI를 선택해주세요!", ["-- 선택하세요 --"] + mbti_list)

# MBTI 별 추천 영화 데이터
mbti_movies = {
    "INTJ": ("인터스텔라 🌌", "논리와 전략으로 우주를 건너는 당신에게 딱!"),
    "INTP": ("굿 윌 헌팅 🧠", "수학 천재의 고독과 따뜻한 성장, 당신이 주인공 같아!"),
    "ENTP": ("빅 히어로 🎈", "아이디어 넘치는 당신에게 딱인 테크+감성 시너지!"),
    "ENTJ": ("소셜 네트워크 🌐", "리더십 넘치는 당신, 젊은 CEO의 치열한 이야기 어때요?"),
    "INFJ": ("콘택트 🛸", "외계와의 소통, 인간의 감정과 과학의 만남을 좋아하는 당신에게!"),
    "INFP": ("월터의 상상은 현실이 된다 🌍", "내면의 꿈을 향해 수학적 상상력을 펼치는 여정!"),
    "ENFP": ("백 투 더 퓨처 ⏳", "시간여행처럼 에너지 넘치는 당신에게 추천!"),
    "ENFJ": ("히든 피겨스 🚀", "당신의 공감 능력, 사회적 정의감에 딱 맞는 과학 실화!"),
    "ISTJ": ("2001: 스페이스 오디세이 🛰️", "논리와 분석력의 끝판왕!"),
    "ISFJ": ("마션 🪐", "헌신적이고 현실적인 당신, 감동적인 생존 스토리 좋아하실 듯!"),
    "ESTJ": ("아이언맨 🦾", "효율적이고 카리스마 있는 당신, 기술의 끝을 보여줄게요!"),
    "ESFJ": ("페르마의 밀실 🔐", "추리와 팀워크가 중요한 수학 서스펜스!"),
    "ISTP": ("테넷 ⏱️", "복잡한 구조 속에서도 중심을 잡는 당신에게!"),
    "ISFP": ("월-E 🤖", "감성적이고 따뜻한 과학적 메시지가 있는 영화!"),
    "ESTP": ("루시 🧬", "즉흥적이고 모험을 좋아하는 당신, 뇌의 끝을 보자!"),
    "ESFP": ("쥬라기 월드 🦖", "스릴 넘치는 공룡 어드벤처, 무조건 신남 보장!"),
}

# 추천 영화 보여주기
if selected_mbti in mbti_movies:
    movie, desc = mbti_movies[selected_mbti]
    st.success(f"🎁 당신에게 추천하는 영화는 바로... **{movie}**!")
    st.markdown(f"📝 {desc}")
    st.balloons()
elif selected_mbti != "-- 선택하세요 --":
    st.warning("😥 알 수 없는 오류가 발생했어요. 다시 시도해주세요.")
