import psycopg2
def table():
    conn=psycopg2.connect(dbname="postgres",user="postgres",password="shridevi01",host="localhost",port="5432")
    cursor=conn.cursor()
    cursor.execute('''create table employees(name text,age int,number int);''')
    print('done')
    conn.commit()
    conn.close()

def data():
    conn=psycopg2.connect(dbname="postgres",user="postgres",password="shridevi01",host="localhost",port="5432")
    cursor=conn.cursor()
    name=input("name")
    age=input("age")
    number=input("id")
    query='''insert into employees(name,age,number) values(%s,%s,%s)'''
    cursor.execute(query,(name,age,number))
    
    print('da')
    conn.commit()
    conn.close()
data()
