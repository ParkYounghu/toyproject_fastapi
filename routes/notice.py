from fastapi import APIRouter, Request, Depends, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from services.db import get_db_connection
import psycopg2
from psycopg2.extras import DictCursor

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# 데이터베이스 연결 의존성
def get_db():
    conn = get_db_connection()
    try:
        yield conn
    finally:
        conn.close()

@router.get("/list", response_class=HTMLResponse)
async def get_notice_list(request: Request, db: psycopg2.extensions.connection = Depends(get_db)):
    """
    공지사항 목록을 조회합니다.
    """
    cursor = db.cursor(cursor_factory=DictCursor)
    cursor.execute("SELECT id, title, TO_CHAR(created_at, 'YYYY-MM-DD HH24:MI') as created_at FROM notice ORDER BY id DESC;")
    notices = cursor.fetchall()
    cursor.close()
    return templates.TemplateResponse("notice/list.html", {"request": request, "notices": notices})

@router.get("/write", response_class=HTMLResponse)
async def get_write_form(request: Request):
    """
    공지사항 작성 폼을 반환합니다.
    """
    return templates.TemplateResponse("notice/write.html", {"request": request})

@router.post("/write", response_class=RedirectResponse)
async def post_notice(
    request: Request,
    title: str = Form(...),
    content: str = Form(...),
    db: psycopg2.extensions.connection = Depends(get_db)
):
    """
    새 공지사항을 데이터베이스에 추가합니다.
    """
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO notice (title, content) VALUES (%s, %s);", (title, content))
        db.commit()
    except psycopg2.Error as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()
    return RedirectResponse(url="/notice/list", status_code=303)

@router.get("/{notice_id}", response_class=HTMLResponse)
async def get_notice_detail(request: Request, notice_id: int, db: psycopg2.extensions.connection = Depends(get_db)):
    """
    특정 공지사항의 상세 내용을 조회합니다.
    """
    cursor = db.cursor(cursor_factory=DictCursor)
    cursor.execute("SELECT id, title, content, TO_CHAR(created_at, 'YYYY-MM-DD HH24:MI') as created_at FROM notice WHERE id = %s;", (notice_id,))
    notice = cursor.fetchone()
    cursor.close()
    if not notice:
        raise HTTPException(status_code=404, detail="Notice not found")
    return templates.TemplateResponse("notice/detail.html", {"request": request, "notice": notice})

@router.get("/edit/{notice_id}", response_class=HTMLResponse)
async def get_edit_form(request: Request, notice_id: int, db: psycopg2.extensions.connection = Depends(get_db)):
    """

    공지사항 수정 폼을 반환합니다.
    """
    cursor = db.cursor(cursor_factory=DictCursor)
    cursor.execute("SELECT id, title, content FROM notice WHERE id = %s;", (notice_id,))
    notice = cursor.fetchone()
    cursor.close()
    if not notice:
        raise HTTPException(status_code=404, detail="Notice not found")
    return templates.TemplateResponse("notice/edit.html", {"request": request, "notice": notice})

@router.post("/edit/{notice_id}", response_class=RedirectResponse)
async def post_edit_notice(
    request: Request,
    notice_id: int,
    title: str = Form(...),
    content: str = Form(...),
    db: psycopg2.extensions.connection = Depends(get_db)
):
    """
    특정 공지사항을 수정합니다.
    """
    cursor = db.cursor()
    try:
        cursor.execute("UPDATE notice SET title = %s, content = %s WHERE id = %s;", (title, content, notice_id))
        db.commit()
    except psycopg2.Error as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()
    return RedirectResponse(url=f"/notice/{notice_id}", status_code=303)

@router.post("/delete/{notice_id}", response_class=RedirectResponse)
async def delete_notice(request: Request, notice_id: int, db: psycopg2.extensions.connection = Depends(get_db)):
    """
    특정 공지사항을 삭제합니다.
    """
    cursor = db.cursor()
    try:
        cursor.execute("DELETE FROM notice WHERE id = %s;", (notice_id,))
        db.commit()
    except psycopg2.Error as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()
    return RedirectResponse(url="/notice/list", status_code=303)
