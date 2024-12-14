import psycopg2 as pg

conn = pg.connect(
    host='localhost',
    database='aucbase',
    port=5432,
    user='postgres',
    password='pass98rSQL'
    )
cursor=conn.cursor()
