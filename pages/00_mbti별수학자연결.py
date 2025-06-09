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

# 배경음악 (저작권 문제 없는 무료 사운드)
st.markdown("""
<audio controls loop>
  <source src="https://cdn.pixabay.com/midi/2020/07/21/background-meditation-12942.mp3" type="audio/mpeg">
죄송해요, 브라우저가 오디오를 지원하지 않아요.
</audio>
""", unsafe_allow_html=True)

# 제목과 안내
st.title("🔍 MBTI 기반 수학자 성격 매칭")
st.markdown("MBTI를 골라보세요 😊 당신과 닮은 수학자를 알려드릴게요!")

# MBTI 선택
mbti_list = ["INTJ","INTP","ENTP","ENTJ","INFJ","INFP","ENFP","ENFJ",
             "ISTJ","ISFJ","ESTJ","ESFJ","ISTP","ISFP","ESTP","ESFP"]
selected = st.selectbox("📌 당신의 MBTI를 골라주세요:", ["-- 선택 --"]+mbti_list)

# MBTI → 수학자 매핑
mbti_math = {
  "INTJ": {"name":"에바 카르단(É.카르단)", "img":"https://upload.wikimedia.org/.../Cardan.jpg",
           "theorem":"카르단의 공식 (삼차방정식 해법)", "desc":"체계적이고 전략적인 당신과 잘 어울려요."},
  "INTP": {"name":"앨버트 아인슈타인", "img":"https://upload.wikimedia.org/.../Einstein.jpg",
           "theorem":"E = mc²", "desc":"호기심 많고 이론적인 당신!"}, 
  "ENTP": {"name":"존 폰 노이만", "img":"https://upload.wikimedia.org/.../Neumann.jpg",
           "theorem":"게임 이론", "desc":"창의적이고 아이디어 넘치는 당신"},
  "ENTJ": {"name":"카를 가우스", "img":"https://upload.wikimedia.org/.../Gauss.jpg",
           "theorem":"1+2+…+n = n(n+1)/2", "desc":"논리적 리더십의 대표주자"},
  "INFJ": {"name":"블레즈 파스칼", "img":"https://upload.wikimedia.org/.../Pascal.jpg",
           "theorem":"파스칼의 삼각형", "desc":"깊이 생각하는 당신에게 딱!"},
  "INFP": {"name":"피에르 드 페르마", "img":"https://upload.wikimedia.org/.../Fermat.jpg",
           "theorem":"페르마의 소정리", "desc":"상상력과 이상을 사랑하는 당신"},
  "ENFP": {"name":"스리니바사 라마누잔", "img":"https://upload.wikimedia.org/.../Ramanujan.jpg",
           "theorem":"무한급수", "desc":"감성과 직관이 뛰어난 당신"},
  "ENFJ": {"name":"마리아 미르자코바", "img":"https://upload.wikimedia.org/.../Mirzakhani.jpg",
           "theorem":"측지선과 곡면 연구", "desc":"공감력과 리더십이 빛나는 당신"},
  "ISTJ": {"name":"유클리드", "img":"https://upload.wikimedia.org/.../Euclid.jpg",
           "theorem":"기하학 기본 공리", "desc":"체계적이고 규칙적인 당신"},
  "ISFJ": {"name":"에밀리 두 샤틀리에", "img":"https://upload.wikimedia.org/.../Chatelet.jpg",
           "theorem":"물리·수학 통섭", "desc":"헌신적이고 책임감 있는 당신"},
  "ESTJ": {"name":"라이프니츠", "img":"https://upload.wikimedia.org/.../Leibniz.jpg",
           "theorem":"미분적분학 공동 발견", "desc":"실용적이고 추진력 있는 당신"},
  "ESFJ": {"name":"에이다 러브레이스", "img":"https://upload.wikimedia.org/.../Ada_Lovelace.jpg",
           "theorem":"세계 최초 프로그램", "desc":"사람을 생각하는 따뜻한 당신"},
  "ISTP": {"name":"에바리스트 갈루아", "img":"https://upload.wikimedia.org/.../Galois.jpg",
           "theorem":"갈루아 이론", "desc":"직관력 있고 도전적인 당신"},
  "ISFP": {"name":"소피 제르맹", "img":"https://upload.wikimedia.org/.../Sophie_Germain.jpg",
           "theorem":"제르맹 소수", "desc":"내성적이지만 열정적인 당신"},
  "ESTP": {"name":"앨런 튜링", "img":"https://upload.wikimedia.org/.../Turing.jpg",
           "theorem":"튜링 기계", "desc":"실용적 해결 능력 천재"},
  "ESFP": {"name":"헬레나 리비트", "img":"https://upload.wikimedia.org/.../Henrietta_L.jpg",
           "theorem":"리비트의 변화율 관찰", "desc":"직감 있고 사람을 즐겁게 하는 당신"}
}

# 결과
if selected in mbti_math:
    d = mbti_math[selected]
    st.header(f"👉 당신과 닮은 수학자: **{d['name']}**")
    st.image(d["img"], width=250)
    st.markdown(f"**설명**: {d['desc']}")
    st.markdown(f"**대표 정리**: {d['theorem']}")
    st.markdown("✉️ 수학자에게 전하고 싶은 말이나 느낀 점을 적어보세요:")
    letter = st.text_area("📩 편지 작성", height=100)
    if st.button("전송하기"):
        st.success("성공적으로 전송했어요! 👍")
        st.write("당신의 편지:")
        st.write(letter)
elif selected != "-- 선택 --":
    st.warning("해당 MBTI에 대한 정보는 곧 준비할게요.")
