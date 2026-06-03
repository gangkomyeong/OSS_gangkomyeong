# 1. 가볍고 안정적인 Python 3.10 이미지를 베이스로 사용
FROM python:3.10

# 2. 컨테이너 내부의 작업 디렉토리를 /app으로 설정
WORKDIR /app

# 3. 라이브러리 설치를 위해 requirements.txt를 먼저 복사 후 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 현재 폴더의 모든 소스 코드(main.py 등)를 컨테이너 내부로 복사
COPY . .

# 5. Uvicorn을 사용해 FastAPI 앱 실행 (컨테이너 내부 포트는 8000으로 지정)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
