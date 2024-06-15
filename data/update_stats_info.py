from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
#функция для вывода всех данных о компаний по полученном айди
def update_stats_info(s:Session,data, init_data):
    query="""
    UPDATE stats
    SET rating = :rat, clients = :cl, profit = :prf, age = :ag, cover = :cvr
    WHERE id = :id            
    """

    #список сокращений и ссылок для значений из нашей базы данных
    s.execute(text(query),{
        "rat":data['rating'],
        "cl":data['clients'],
        "prf":data['profit'],
        "ag":data['age'],
        "cvr":data['cover'],
        "id":init_data.id,
    })
    s.commit()