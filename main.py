from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

# static 폴더를 /static 경로에 마운트
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 템플릿 설정
templates = Jinja2Templates(directory="templates")

# 목 데이터
products_data = [
    {"name": "Laptop", "price": 1200, "tags": ["electronics", "computer"]},
    {"name": "Smartphone", "price": 800, "tags": ["electronics", "mobile"]},
    {"name": "Book", "price": 25, "tags": ["reading", "education"]},
    {"name": "Headphones", "price": 150, "tags": ["electronics", "audio"]},
]

user_data = {"name": "John Doe", "age": 30}

user_list_data = [
    {"name": "Alice", "age": 25, "city": "Seoul"},
    {"name": "Charlie", "age": 35, "city": "New York"},
]

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    루트 경로('/') 요청 시 main.html 템플릿을 렌더링합니다.
    """
    return templates.TemplateResponse("main.html", {"request": request})

@app.get("/10_jinja2", response_class=HTMLResponse)
async def show_products(request: Request):
    """
    /10_jinja2 경로 요청 시 10_jinja2.html 템플릿을 렌더링합니다.
    - `products` 데이터를 템플릿에 전달합니다.
    """
    return templates.TemplateResponse("10_jinja2.html", {"request": request, "products": products_data})

@app.get("/main_context", response_class=HTMLResponse)
async def show_main_context(request: Request):
    """
    /main_context 경로 요청 시 main_context.html 템플릿을 렌더링합니다.
    - `title`, `items`, `user` 데이터를 템플릿에 전달합니다.
    """
    context = {
        "request": request,
        "title": "Jinja2 Context Example",
        "items": ["Item 1", "Item 2", "Item 3"],
        "user": user_data
    }
    return templates.TemplateResponse("main_context.html", context)

@app.get("/shotdocs", response_class=HTMLResponse)
async def show_shotdocs(request: Request):
    """
    /shotdocs 경로 요청 시 shotdocs.html 템플릿을 렌더링합니다.
    """
    return templates.TemplateResponse("shotdocs.html", {"request": request})

@app.get("/users/list", response_class=HTMLResponse)
async def show_user_list(request: Request):
    """
    /users/list 경로 요청 시 users/list.html 템플릿을 렌더링합니다.
    - `user_list` 데이터를 템플릿에 전달합니다.
    """
    return templates.TemplateResponse("users/list.html", {"request": request, "user_list": user_list_data})

# uvicorn main:app --reload
# 위 명령어로 서버를 실행할 수 있습니다.
