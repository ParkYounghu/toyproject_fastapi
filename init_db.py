import psycopg2
from services.db import get_db_connection

def initialize_database():
    """
    데이터베이스 테이블을 초기화하고 샘플 데이터를 삽입합니다.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # "notice" 테이블이 없으면 생성
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS notice (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                content TEXT,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
            );
        """)

        # 테이블이 비어있는 경우에만 샘플 데이터 삽입
        cursor.execute("SELECT COUNT(*) FROM notice;")
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO notice (title, content) VALUES (%s, %s);", 
                           ('첫 번째 공지사항', '이것은 첫 번째 공지사항의 내용입니다.'))
            cursor.execute("INSERT INTO notice (title, content) VALUES (%s, %s);", 
                           ('두 번째 공지사항', '이것은 두 번째 공지사항의 내용입니다.'))
            print("샘플 데이터가 삽입되었습니다.")

        conn.commit()
        cursor.close()
        conn.close()
        print("데이터베이스 테이블이 성공적으로 준비되었습니다.")

    except psycopg2.Error as e:
        print(f"데이터베이스 초기화 중 오류 발생: {e}")

if __name__ == "__main__":
    initialize_database()
