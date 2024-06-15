from sqlalchemy import text
from sqlalchemy.orm import Session

def delete_stats_info(s:Session, data):
    query = """
    DELETE 
    FROM stats 
    WHERE id = :id
    """

    s.execute(text(query), {"id": data.id})
    s.commit()