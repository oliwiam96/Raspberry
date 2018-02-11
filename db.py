import sqlite3
import time
import datetime
import random

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS pomiary(Czas_pomiaru TEXT, Temperatura_powietrza REAL, Wilgotnosc_powietrza REAL, Wilgotnosc_gleby BOOLEAN, Opady BOOLEAN)')
    conn.commit()
    
def insert():
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(time)
    temp_p = random.randrange(0,10)
    wilg_p = random.randrange(0,10)
    wilg_g = random.randrange(0,1)
    opady = random.randrange(0,2)
    c.execute("INSERT INTO pomiary(Czas_pomiaru, Temperatura_powietrza, Wilgotnosc_powietrza, Wilgotnosc_gleby, Opady) VALUES(?, ?, ?, ?, ?)", (time, temp_p, wilg_p, wilg_g, opady))
    conn.commit()
    
def select():
    c.execute("SELECT * FROM pomiary")
    data = c.fetchall()
    print(data)


conn = sqlite3.connect('pomiary.db')
c = conn.cursor()


    
print("hello world")
#create_table()
#insert()
#insert()
#insert()
select()


c.close()
conn.close()