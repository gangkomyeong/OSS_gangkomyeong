from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Side Project Tech Stack Recommender API")

# Streamlit에서 보낼 데이터 구조 정의
class UserInput(BaseModel):
    experience: str  # "초보자", "전공자/경험자"
    main_interest: str  # "웹 서비스", "데이터 분석/AI", "앱(모바일)"
    dev_time: int  # 주당 개발 가능 시간 (시간)

@app.get("/")
def read_root():
    return {"message": "FastAPI Recommendation Server is running!"}

@app.post("/recommend")
def get_recommendation(data: UserInput):
    # 매우 단순하지만 확실한 Rule-based 추천 로직
    # 1. 웹 서비스 관심
    if data.main_interest == "웹 서비스":
        if data.experience == "초보자":
            title = "초보자를 위한 간편 HTML/CSS & Python Flask 블로그 만들기"
            stack = "Python, Flask, 기본 HTML/CSS, Vanilla JS"
            desc = f"주당 {data.dev_time}시간 투자로 부담 없이 웹의 기초를 다질 수 있는 프로젝트입니다."
        else:
            title = "트렌디한 풀스택 웹 애플리케이션 (Next.js + FastAPI)"
            stack = "Next.js, FastAPI, PostgreSQL, Docker"
            desc = f"경험자가 도전하기 좋은 아키텍처입니다. {data.dev_time}시간 동안 밀도 있게 API 연동과 DB 설계를 경험해보세요."

    # 2. 데이터 분석 / AI 관심
    elif data.main_interest == "데이터 분석/AI":
        if data.experience == "초보자":
            title = "공공 데이터를 활용한 우리 동네 맛집 데이터 시각화 대시보드"
            stack = "Python, Pandas, Streamlit, Plotly"
            desc = f"복잡한 모델링 대신, {data.dev_time}시간 동안 데이터를 정제하고 직관적인 웹 대시보드로 시각화하는 재미를 느낄 수 있습니다."
        else:
            title = "LLM API를 활용한 맞춤형 AI 자소서 첨삭 챗봇"
            stack = "Python, LangChain, OpenAI API, FastAPI"
            desc = f"기존 경험을 살려 최신 AI API를 연동하고, {data.dev_time}시간 동안 프롬프트 엔지니어링과 백엔드 파이프라인을 구축합니다."

    # 3. 앱(모바일) 관심
    else:
        if data.experience == "초보자":
            title = "Flutter를 이용한 초간단 '오늘의 한 줄' 일기장 앱"
            stack = "Flutter, Dart, LocalStorage"
            desc = f"크로스 플랫폼의 강자 Flutter로 안드로이드와 iOS 앱을 동시에 빌드하며 {data.dev_time}시간 동안 UI/UX 기초를 배웁니다."
        else:
            title = "React Native + Firebase 실시간 배달/매칭 서비스"
            stack = "React Native, Expo, Firebase (Firestore, Auth)"
            desc = f"실시간 NoSQL 데이터베이스와 인증 기능을 결합하여, {data.dev_time}시간 동안 실제 서비스 수준의 MVP 앱을 개발합니다."

    return {
        "project_title": title,
        "recommended_stack": stack,
        "description": desc
    }