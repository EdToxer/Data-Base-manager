from sqlalchemy import text
from sqlalchemy.orm import Session

def insert_stats_info(s:Session, data):
    query = """
    INSERT INTO stats(company_id, rating, clients, profit, age, cover)
    VALUES (:cid, :rt, :cl, :pf, :ag, :cv)
    """

    s.execute(text(query), {
        "cid": data['company_id'],
        "rt": data['rating'],
        "cl": data['clients'],
        "pf": data['profit'],
        "ag": data['age'],
        "cv": data['cover']
    })
    s.commit()