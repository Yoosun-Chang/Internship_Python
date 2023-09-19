import psycopg

conn = psycopg.connect(host="localhost",
                        port="5432",
                        user="postgres",
                        password="0815",
                        database="postgres",
 )

cur = conn.cursor()

cur.execute("""
    CREATE TABLE POI2 (
        id SERIAL PRIMARY KEY,
        latitude FLOAT,
        longitude FLOAT,
        name VARCHAR(10),
        category INT
    )
""")

conn.commit()

conn.close()


