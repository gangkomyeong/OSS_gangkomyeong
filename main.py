from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()
FILE_NAME = "courses.json"

# Pydantic 모델: POST 요청 시 들어올 데이터의 유효성을 검증합니다.
class Course(BaseModel):
    course_name: str
    year: str
    semester: str
    grade: str

# JSON 파일을 읽어오는 헬퍼 함수
def read_courses():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

# JSON 파일에 데이터를 저장하는 헬퍼 함수
def write_courses(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# (1) GET /courses : 전체 수강기록 반환
@app.get("/courses")
def get_all_courses():
    courses = read_courses()
    return courses

# (2) POST /courses : 새로운 수강기록 추가
@app.post("/courses")
def add_course(course: Course):
    # 1. 기존 데이터 읽기
    courses = read_courses()
    
    # 2. 새 데이터 추가 (Pydantic 모델을 딕셔너리로 변환)
    new_course = course.model_dump()
    courses.append(new_course)
    
    # 3. 파일에 덮어쓰기
    write_courses(courses)
    
    return {"message": "수강기록이 성공적으로 추가되었습니다.", "data": new_course}