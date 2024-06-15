from sqlalchemy import text
from sqlalchemy.orm import Session
#функция для сбора имён компаний из базы данных
def fetch_company_info(s: Session):
    query= """
    SELECT *
    FROM companies
    """
    rows = s.execute(text(query))
    #собираем все имена компаний в "строчку", rows, чтобы потом её вывести в главный код
    return rows