from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
#функция для вывода определённых компаний с помощью интерфейса программы
#по умолчанию программа выводит все компании сразу
def fetch_stats_info(s:Session,company_id):
    query= """
    SELECT *
    FROM stats
    WHERE (:cid = 0 OR company_id = :cid)
    ORDER BY company_id
    """
    rows = s.execute(text(query), {"cid":company_id})
    #собирает заданное айди компании(по умолчанию все сразы)
    #чтобы занести их в строчку для использования в главном коде
    return rows