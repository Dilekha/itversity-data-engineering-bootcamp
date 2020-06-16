import psycopg2

try:
    conn = psycopg2.connect("dbname='retail_dw' user='retail_user' host='34.94.114.182' password='itversity909090'")
except:
    print("I am unable to connect to the database")

cur = conn.cursor()
try:
    cur.execute("""SELECT * from t""")
except:
    print("I can't SELECT from t")

rows = cur.fetchall()
print("\nRows: \n")
for row in rows:
    print("   ", row)