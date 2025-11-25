[gemini model = pro]

input_file="templates/*.html

당신은 FastAPI 프로젝트 자동 생성기 역할을 합니다.

입력 파일은 모두 제가 만든 웹사이트의 HTML, CSS, JS입니다.
이 코드들을 기반으로 FastAPI 서버 전체 구조를 자동 구성해주세요.

### 목표
1. 입력된 HTML 파일들은 templates/ 폴더에 그대로 유지하며 Jinja2 템플릿으로 사용.
2. CSS/JS/이미지는 static/ 폴더에서 제공.
3. root("/") 요청 시 메인 HTML 파일을 렌더링하도록 main.py 생성.
4. HTML 안에 여러 페이지가 있다면, 파일명 기준으로 자동 라우팅 생성:
   - 예: about.html → /about
   - 예: dashboard.html → /dashboard
5. FastAPI_best_practices에 맞게 코드 구조를 생성:
   - from fastapi import FastAPI, Request
   - from fastapi.templating import Jinja2Templates
   - from fastapi.staticfiles import StaticFiles
   - app = FastAPI()
   - app.mount("/static", StaticFiles(directory="static"), name="static")
6. HTML 내 form(action="/something") 이 있으면 자동으로 FastAPI 라우터 생성.
7. JS에서 fetch("/api/...") 호출이 있다면 그에 맞는 API 엔드포인트도 생성.
8. 파일 경로, 폴더 구조, 템플릿 매핑을 오류 없이 생성.

### 출력 형태
- 완전한 main.py 코드만 생성
- 모든 라우터가 동작하도록 import 포함
- 누락 또는 가정 없이 실행 가능한 완성본 코드

이제 위의 요구사항을 기반으로 main.py를 완성된 상태로 생성하세요.
