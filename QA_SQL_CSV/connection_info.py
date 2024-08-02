from psycopg2 import connect  #postgre 연결용
from langchain.sql_database import SQLDatabase
# connection 생성
def postgre_con(dbname, IP, PORT, ID, PW):
    uri = f"postgresql+psycopg2://{ID}:{PW}@{IP}:{PORT}/{dbname}"
    postgre_connection = SQLDatabase.from_uri(uri,
                                              schema='gfdata', 
                                              include_tables = ['gis_con_data', 'electionmap_21'])
    return postgre_connection

db = postgre_con('geondb', '10.0.3.13', 5432, 'gf', 'gfuser1!')