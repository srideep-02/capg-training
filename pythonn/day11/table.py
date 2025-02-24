import pymysql
def connect_db():
    try:
        conn=pymysql.connect(
            host="localhost",
            user="root",
            password="2004",
            database="mydatabase"
        )
        print("Connected to mysql successfully")
        return conn
    except pymysql.MySQLError as err:
        print(f"Error:{err}")
        return None
    
def create_database():
    try:
        conn=pymysql.connect(
            host="localhost",
            user="root",
            password="2004"
        )
        
        conn.cursor().execute("CREATE DATABASE IF NOT EXISTS mydatabase")
        conn.close()
    except pymysql.MySQLError as err:
        print(f"Error:{err}")
        
def create_table(conn):
    cursor=conn.cursor()
    cursor.execute("CRETAE TABLE IF NOT EXISTS customers (name VARCHAR(255),address VARCHAR(255))")
    cursor.close()
    
def insert_data(conn,name,address):
    cursor=conn.cursor()
    cursor.execute("INSERT INTO customers (name, address) VALUES (%s, %s)", (name,address) )
    conn.commit()
    conn.close()
    
def select_data(conn):
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM customers")
    result=cursor.fetchall()
    cursor.close()
    return result

def main():
    create_database()
    conn = connect_db()
    if conn is None:
        return
    create_table(conn)
    insert_data(conn,"sri", "kmr")
    insert_data(conn,"ram", "knr")
    insert_data(conn,"srav", "jgtl")
    insert_data(conn,"shiv", "sdpt")
    result = select_data(conn)
    for r in result:
        print(r)
        
    conn.close()
    
if __name__ == "__main__":
    main()        
    