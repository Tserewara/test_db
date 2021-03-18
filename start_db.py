import psycopg2
try:
    conn = psycopg2.connect("host=localhost dbname=blog")
    conn.close()
except psycopg2.OperationalError as ex:
    print("Connection failed: {0}".format(ex))
