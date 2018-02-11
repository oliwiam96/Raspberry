from flask import Flask, render_template
import sqlite3


def select():
    c.execute("SELECT * FROM pomiary")
    data = c.fetchall()
    print(data)

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/halo')
def halo():
    conn = sqlite3.connect('../pomiary.db')
    c = conn.cursor()
    wynik = ""
    c.execute("SELECT * FROM pomiary ORDER BY Czas_pomiaru DESC LIMIT 10")
    data = c.fetchall()
    for row in data:
        print(row)
        wynik = wynik + str(row) + '\n' #nie dziala nowa linia i nie wiem za bardzo jak to naprawic, chyba w htmlu trzeba dodawac nowe linie za pomoca <br>
    #print(data)
    c.close()
    conn.close()
    
    return wynik
    #return str(data)

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name= name)


if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')
    
