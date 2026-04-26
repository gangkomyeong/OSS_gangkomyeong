import streamlit as st
import time

# [설정] 페이지 타이틀 및 아이콘
st.set_page_config(page_title="자취생 생존 테스트", page_icon="🏠")

# [필수 조건 1] 첫 화면 학번 및 이름 표시
def show_header():
    st.title("자취생 생존 능력 테스트")
    st.markdown("### 당신은 혼자서도 잘 살 수 있을까요?")
    
    st.sidebar.header("과제 제출 정보")
    st.sidebar.info("학번: 2022204074  \n이름: 고강명")
    st.divider()

# [필수 조건 3] 캐싱 기능 구현
@st.cache_data
def load_quiz_data():
    # 데이터 로딩 지연 시뮬레이션
    time.sleep(1.5) 
    return [
        {
            "id": 1,
            "question": "수박 껍질은 어떤 쓰레기로 분류해야 할까요?",
            "options": ["일반 쓰레기", "음식물 쓰레기", "대형 폐기물"],
            "answer": "음식물 쓰레기",
            "explanation": "동물이 먹을 수 있느냐가 기준입니다. 수박 껍질은 부드러워 음식물 쓰레기지만, 딱딱한 달걀 껍데기나 밤 껍질은 일반 쓰레기입니다."
        },
        {
            "id": 2,
            "question": "남아서 딱딱해진 배달 피자를 촉촉하게 데우는 방법은?",
            "options": ["그냥 렌지에 5분 돌린다", "물 한 잔과 함께 렌지에 돌린다", "냉동실에 넣었다가 그대로 먹는다"],
            "answer": "물 한 잔과 함께 렌지에 돌린다",
            "explanation": "컵에 물을 담아 함께 돌리면 수증기가 발생해 피자가 촉촉해집니다."
        },
        {
            "id": 3,
            "question": "옷에 묻은 볼펜 자국을 지우는 데 효과적인 것은?",
            "options": ["주방세제", "물파스", "식초"],
            "answer": "물파스",
            "explanation": "물파스의 알코올 성분이 볼펜의 유성 성분을 녹여줍니다."
        },
        {
            "id": 4,
            "question": "냉장고에서 냄새가 날 때 탈취제로 쓰기 가장 좋은 것은?",
            "options": ["다 쓴 소주병", "말린 커피 찌꺼기", "젖은 행주"],
            "answer": "말린 커피 찌꺼기",
            "explanation": "커피 찌꺼기는 탈취 효과가 뛰어나지만, 반드시 바짝 말려서 넣어야 곰팡이가 생기지 않습니다."
        },
        {
            "id": 5,
            "question": "배달 용기에 밴 빨간 양념 얼룩을 지우는 가장 쉬운 방법은?",
            "options": ["햇빛에 말리기", "세제로 10번 닦기", "그냥 버리기"],
            "answer": "햇빛에 말리기",
            "explanation": "햇빛의 자외선이 고추기름의 성분을 분해하여 얼룩을 없애줍니다."
        },
        {
            "id": 6,
            "question": "수건에서 쉰내가 날 때 세탁 시 추가하면 좋은 것은?",
            "options": ["식초", "설탕", "간장"],
            "answer": "식초",
            "explanation": "마지막 헹굼 단계에서 식초를 조금 넣으면 살균 및 탈취 효과가 있습니다."
        },
        {
            "id": 7,
            "question": "라면을 가장 맛있게 끓이는 정석 방법은?",
            "options": ["스프 먼저 넣기", "면 먼저 넣기", "뒷면 레시피대로 끓이기"],
            "answer": "뒷면 레시피대로 끓이기",
            "explanation": "제조사 연구원들이 수만 번 테스트하여 만든 최적의 가이드를 따르는 것이 최고입니다."
        }
    ]

# 세션 상태 초기화 (로그인 및 퀴즈 상태 관리)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_name = ""

show_header()

# [필수 조건 2] 로그인 기능
if not st.session_state.logged_in:
    st.subheader("🔐 테스트 시작을 위해 로그인해주세요")
    with st.form("login_form"):
        # 간단한 아이디/비번 기반 로그인
        user_id = st.text_input("아이디 (학번)", placeholder="학번을 입력하세요")
        user_pw = st.text_input("비밀번호", type="password", placeholder="초기 비밀번호: 1234")
        login_btn = st.form_submit_button("로그인")
        
        if login_btn:
            if user_pw == "1234":
                st.session_state.logged_in = True
                st.session_state.user_name = user_id
                st.success(f"{user_id}님 로그인 성공!")
                st.rerun()
            else:
                st.error("비밀번호가 틀렸습니다. (힌트: 1234)")
    st.warning("로그인 후 퀴즈 콘텐츠가 활성화됩니다.")
    st.stop()

# --- 로그인 후 화면 ---

# [필수 조건 4] 퀴즈 기능
st.sidebar.success(f"접속 중: {st.session_state.user_name}")
if st.sidebar.button("로그아웃"):
    st.session_state.logged_in = False
    st.rerun()

st.info("💡 캐싱 기능이 적용되어 데이터를 불러오는 속도가 최적화되었습니다.")

# 데이터 로드 (캐싱 적용됨)
quiz_data = load_quiz_data()
user_answers = {}

with st.form("survival_quiz"):
    st.subheader("생존 상식 문제")
    for q in quiz_data:
        st.write(f"**Q{q['id']}. {q['question']}**")
        user_answers[q['id']] = st.radio(
            f"선택지 (Q{q['id']})", 
            q['options'], 
            label_visibility="collapsed",
            key=f"ans_{q['id']}"
        )
        st.write("") # 간격 조절
    
    submit_btn = st.form_submit_button("나의 생존 지수 확인하기")

# 결과 출력
if submit_btn:
    score = 0
    st.divider()
    st.subheader("테스트 결과")
    
    for q in quiz_data:
        if user_answers[q['id']] == q['answer']:
            score += 1
            st.write(f"**Q{q['id']}**: 정답!")
        else:
            st.write(f"**Q{q['id']}**: 오답 (정답: {q['answer']})")
            st.caption(f"해설: {q['explanation']}")
    
    # 최종 등급 계산
    st.markdown("---")
    final_score = score
    total = len(quiz_data)
    
    st.metric("맞춘 개수", f"{final_score} / {total}")
    
    if final_score == total:
        st.balloons()
        st.success("**당신은 '자취의 신'입니다!** 완벽한 생존 능력을 갖추셨네요.")
    elif final_score >= 4:
        st.info("**'자취 우등생'입니다.** 큰 어려움 없이 독립 생활이 가능합니다.")
    else:
        st.warning("**'자취 새내기'군요.** 위 해설들을 읽고 생존 지식을 보충하세요!")