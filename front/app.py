import streamlit as st
import requests

# 페이지 설정
st.set_page_config(page_title="사이드 프로젝트 추천기", page_icon=" ", layout="centered")

st.title("나에게 맞는 사이드 프로젝트 & 기술 스택 추천")
st.write("몇 가지 질문에 답하면, 이번 학기 혹은 방학 때 도전하기 좋은 프로젝트 주제와 추천 기술 스택을 알려 드립니다!")

st.markdown("---")

# 1. 사용자 입력 받기
experience = st.radio(
    "1. 당신의 개발 경험 수준은 어느 정도인가요?",
    ("초보자", "전공자/경험자")
)

main_interest = st.selectbox(
    "2. 가장 관심 있는 분야를 선택해 주세요.",
    ("웹 서비스", "데이터 분석/AI", "앱(모바일)")
)

dev_time = st.slider(
    "3. 일주일에 프로젝트에 투자할 수 있는 시간은?",
    min_value=2, max_value=20, value=5, step=1
)

st.markdown("---")

# 2. 추천 요청 버튼
if st.button("✨ 나에게 맞는 프로젝트 추천받기"):
    
    # FastAPI 백엔드 주소 (★본인의 AWS EC2 퍼블릭 IP로 반드시 변경하세요★)
    # 로컬 테스트 시에는 http://localhost:8000/recommend 사용 가능
    BACKEND_URL = "http://localhost:8000/recommend" 
    
    # 백엔드로 보낼 데이터 구성
    payload = {
        "experience": experience,
        "main_interest": main_interest,
        "dev_time": dev_time
    }
    
    with st.spinner("FastAPI 백엔드 엔진에서 추천 결과를 생성 중입니다..."):
        try:
            # 3. FastAPI에 POST 요청 보내기
            response = requests.post(BACKEND_URL, json=payload, timeout=5)
            
            if response.status_code == 200:
                result = response.json()
                
                # 4. 결과 출력하기
                st.success("맞춤 추천 결과가 도착했습니다!")
                
                st.subheader(f"추천 주제: {result['project_title']}")
                
                st.markdown(f"**추천 기술 스택:** `{result['recommended_stack']}`")
                
                st.info(f"**상세 설명 및 가이드:**\n{result['description']}")
                
                # FastAPI와 통신했음을 증명하는 디버그용 안내 (교수님 확인용)
                st.caption("⚡ Status: FastAPI 서버로부터 JSON 데이터를 정상적으로 수신했습니다.")
                
            else:
                st.error(f"백엔드 서버 에러가 발생했습니다. (Status Code: {response.status_code})")
        except requests.exceptions.ConnectionError:
            st.error("FastAPI 백엔드 서버에 연결할 수 없습니다. 서버 주소(IP)나 포트, Docker 실행 여부를 확인하세요.")