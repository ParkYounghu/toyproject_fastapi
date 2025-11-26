```

{
  "task": "FastAPI 기반 공지사항 CRUD 기능 생성 및 기존 프로젝트 업데이트",
  "instructions": {
    "goal": "FastAPI + PostgreSQL(psycopg2) + Jinja2 + Bootstrap 5를 사용하여 '공지사항(Notice) CRUD 기능'을 구현한다.",
    "important_rules": [
      "main.py는 절대 전체 덮어쓰지 말고, 필요한 부분만 추가한다.",
      "이미 존재하는 파일은 기존 코드를 유지한 채 충돌 없는 부분만 추가한다.",
      "존재하지 않는 파일은 자동으로 새 파일로 생성한다.",
      "모든 파일은 VS Code에 바로 붙여넣으면 작동 가능한 전체 코드를 포함해야 한다.",
      "코드 누락 또는 생략 없이 완전한 작동 버전이어야 한다.",
      "templates/notice/ 경로 아래에 HTML 파일을 생성한다.",
      "UI는 모두 Bootstrap 5를 적용한다.",
      "CRUD 요소(Create, Read, Update, Delete)는 전부 포함되어야 한다.",
      "출력 시 각 파일은 Markdown 코드블럭으로 분리해서 제시한다."
    ]
  },
  "project_structure": {
    "create_or_update": [
      {
        "path": "main.py",
        "action": "update_only",
        "required_additions": [
          "from routes.notice import router as notice_router",
          "app.include_router(notice_router, prefix=\"/notice\")"
        ]
      },
      {
        "path": "routes/notice.py",
        "action": "create_if_missing",
        "content_description": "공지사항 CRUD 라우터 전체 구현 (목록, 작성, 수정, 삭제 포함)"
      },
      {
        "path": "templates/notice/base.html",
        "action": "create_if_missing",
        "content_description": "Bootstrap 5 공통 레이아웃"
      },
      {
        "path": "templates/notice/list.html",
        "action": "create_if_missing",
        "content_description": "공지사항 목록 페이지 (Read)"
      },
      {
        "path": "templates/notice/write.html",
        "action": "create_if_missing",
        "content_description": "공지사항 작성 페이지 (Create)"
      },
      {
        "path": "templates/notice/edit.html",
        "action": "create_if_missing",
        "content_description": "공지사항 수정 페이지 (Update)"
      },
      {
        "path": "templates/notice/detail.html",
        "action": "create_if_missing",
        "content_description": "공지사항 상세보기 페이지 (Read)"
      }
    ]
  },
  "output_format": {
    "type": "files",
    "description": "각 파일을 Markdown 코드블록으로 출력하고 경로를 명확하게 표시하라.",
    "codeblock_languages": ["python", "html"]
  }
}

```