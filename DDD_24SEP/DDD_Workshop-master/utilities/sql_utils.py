import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from utilities import PropertyReader as pr

engine = create_engine(URL(
    drivername=pr.get_property("sql", "drivername"),
    username=pr.get_property("sql", "username"),
    password=pr.get_property("sql", "password"),
    host=pr.get_property("sql", "host"),
    database=pr.get_property("sql", "database")
))


def get_sql_data(search_criteria):
    conn = engine.connect()
    data_frame = pd.read_sql(sql=search_criteria,
                             con=conn)
    conn.close()
    return data_frame


def sql_header(search_criteria):
    data = get_sql_data(search_criteria)
    header_list = data.columns.tolist()
    header_map = {}
    count = 0
    for column in header_list:
        header_map[column] = count
        count += 1
    return header_map
